from abc import ABC
from collections import defaultdict
from dataclasses import dataclass
from typing import List, Iterable, Tuple, Optional

import SPARQLWrapper
from SPARQLWrapper import JSON
from obolib.implementations.ubergraph.ubergraph import UbergraphProvider
from obolib.interfaces.basic_ontology_interface import BasicOntologyInterface, RELATIONSHIP_MAP, PRED_CURIE, ALIAS_MAP, \
    PREFIX_MAP
from obolib.resource import OntologyResource
from obolib.types import CURIE, URI
from obolib.vocabulary.vocabulary import IS_A
from rdflib import URIRef, RDFS

VAL_VAR = 'v'

@dataclass
class SparqlImplementation(BasicOntologyInterface):
    engine: SPARQLWrapper

    @classmethod
    def create(cls, resource: OntologyResource = None) -> BasicOntologyInterface:
        engine = UbergraphProvider.create_engine(resource)
        return SparqlImplementation(engine)

    def get_prefix_map(self) -> PREFIX_MAP:
        # TODO
        return {}

    #def store(self, resource: OntologyResource) -> None:
    #    SparqlBasicImpl.dump(self.engine, resource)

    def curie_to_uri(self, curie: CURIE, strict: bool = False) -> URI:
        if curie.startswith('http'):
            return curie
        pm = self.get_prefix_map()
        pfx, local_id = curie.split(':')
        if pfx in pm:
            return f'{pm[pfx]}{local_id}'
        else:
            return f'http://purl.obolibrary.org/obo/{pfx}_{local_id}'

    def uri_to_curie(self, uri: URI, strict=True) -> Optional[CURIE]:
        # TODO: do not hardcode OBO
        pm = self.get_prefix_map()
        for k, v in pm.items():
            if uri.startswith(k):
                return uri.replace(k,f'{v}:')
        if uri.startswith('http://purl.obolibrary.org/obo/'):
            uri = uri.replace('http://purl.obolibrary.org/obo/', "")
            return uri.replace('_',':')
        return uri

    def _query(self, query: str, prefixes: PREFIX_MAP = {}):
        sw = self.engine
        for k, v in prefixes.items():
            query = f'PREFIX {k}: <{v}>\n' + query
        print(f'Q={query}')
        sw.setQuery(query)
        sw.setReturnFormat(JSON)
        ret = sw.queryAndConvert()
        return ret["results"]["bindings"]

    def _triples(self, subject: CURIE = None, predicate: PRED_CURIE = None, object: PRED_CURIE = None, graph: CURIE = None) -> Iterable[Tuple]:
        vars = []
        def _urify_arg(arg: CURIE, name: str):
            if arg is None:
                vars.append(name)
                return f'?{name}'
            else:
                return f'<{self.curie_to_uri(arg)}>'
        subject_uri = _urify_arg(subject, 's')
        predicate_uri = _urify_arg(predicate, 'p')
        object_uri = _urify_arg(object, 'o')
        if graph is None:
            # do not include graph in select
            graph_uri = '?g'
        else:
            graph_uri = _urify_arg(graph, 'g')
        vars_str = ' '.join([f'?{v}' for v in vars])
        bindings = self._query(f"SELECT DISTINCT {vars_str} WHERE {{ GRAPH {graph_uri} {{ {subject_uri} {predicate_uri} {object_uri} }}}}")
        for row in bindings:
            yield tuple([row[v]['value'] for v in vars])

    def get_parents_by_curie(self, curie: CURIE, isa_only: bool = False) -> List[CURIE]:
        return [self.uri_to_curie(obj_uri) for (obj_uri,) in self._triples(curie, RDFS.subClassOf, None, None)]

    def _get_anns(self, curie: CURIE, pred: URIRef):
        uri = self.curie_to_uri(curie)
        bindings = self._query(f"SELECT ?{VAL_VAR} WHERE {{ <{uri}> <{pred}> ?v }}")
        return [row[VAL_VAR]['value'] for row in bindings]

    def get_label_by_curie(self, curie: CURIE):
        labels = self._get_anns(curie, RDFS.label)
        return labels[0]

    def alias_map_by_curie(self, curie: CURIE) -> ALIAS_MAP:
        uri = self.curie_to_uri(curie)
        valstr = "VALUES ?pred {oboInOwl:hasExactSynonym}"
        bindings = self._query(f"SELECT ?pred ?{VAL_VAR} WHERE {{ <{uri}> ?pred ?v . {valstr} }}",
                               {'oboInOwl': 'http://www.geneontology.org/formats/oboInOwl#'})
        m = defaultdict(list)
        for row in bindings:
            #print(f'BINDINGS={row}')
            m[row['pred']['value']].append(row[VAL_VAR]['value'])
        return m


    def get_curies_by_label(self, label: str) -> List[CURIE]:
        return [t.id for t in self.engine.terms()]

    def get_outgoing_relationships_by_curie(self, curie: CURIE, isa_only: bool = False) -> RELATIONSHIP_MAP:
        term = self._term(curie)
        rels = {IS_A: [p.id for p in term.superclasses(distance=1)]}
        for rel_type, parents in term.relationships.items():
            rels[rel_type.id] = [p.id for p in parents]
        return rels

    def create_entity(self, curie: CURIE, label: str = None, relationships: RELATIONSHIP_MAP = None) -> CURIE:
        ont = self.ontology
        t = ont.create_term(curie)
        t.name = label
        for pred, fillers in relationships.items():
            for filler in fillers:
                self.add_relationship(curie, pred, filler)
        return curie

    def add_relationship(self, curie: CURIE, predicate: PRED_CURIE, filler: CURIE):
        t = self._term(curie)
        filler_term = self._create(filler)
        if predicate == IS_A:
            t.superclasses().add(filler_term)
        else:
            predicate_term = self._create_pred(predicate)
            if predicate_term not in t.relationships.keys():
                t.relationships[predicate_term] = []
            t.relationships[predicate_term].add(filler_term)

    def get_definition_by_curie(self, curie: CURIE) -> str:
        """

        :param curie:
        :return:
        """
        return self._term(curie).definition






