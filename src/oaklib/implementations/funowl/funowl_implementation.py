import logging
from dataclasses import dataclass
from typing import Any, Iterable, List, Mapping, Optional

import rdflib
from funowl import (
    IRI,
    AnnotationAssertion,
    Axiom,
    Declaration,
    ObjectSomeValuesFrom,
    OntologyDocument,
    SubClassOf,
)
from funowl.converters.functional_converter import to_python
from funowl.writers.FunctionalWriter import FunctionalWriter
from kgcl_schema.datamodel import kgcl

from oaklib.datamodels.vocabulary import (
    DEPRECATED_PREDICATE,
    HAS_DEFINITION_CURIE,
    HAS_EXACT_SYNONYM,
    IS_A,
    LABEL_PREDICATE,
)
from oaklib.interfaces import SearchInterface
from oaklib.interfaces.owl_interface import OwlInterface, ReasonerConfiguration
from oaklib.interfaces.patcher_interface import PatcherInterface
from oaklib.types import CURIE, PRED_CURIE


@dataclass
class FunOwlImplementation(OwlInterface, PatcherInterface, SearchInterface):
    """
    An experimental partial implementation of :ref:`OwlInterface`

    Wraps FunOWL

    `<https://github.com/hsolbrig/funowl>`_

    """

    ontology_document: OntologyDocument = None

    def __post_init__(self):
        if self.ontology_document is None:
            resource = self.resource
            if resource is None or resource.local_path is None:
                doc = OntologyDocument()
            else:
                logging.info(f"Loading {resource.local_path} into FunOwl")
                doc = to_python(str(resource.local_path))
            self.ontology_document = doc
        if self.functional_writer is None:
            self.functional_writer = FunctionalWriter()
            for prefix in doc.prefixDeclarations.as_prefixes():
                self.functional_writer.bind(prefix.prefixName, prefix.fullIRI)

    @property
    def _ontology(self):
        return self.ontology_document.ontology

    def entity_iri_to_curie(self, entity: IRI) -> CURIE:
        uri = entity.to_rdf(self.functional_writer.g)
        return self.uri_to_curie(str(uri), use_uri_fallback=True)

    def curie_to_entity_iri(self, curie: CURIE) -> IRI:
        return IRI(self.curie_to_uri(curie))

    def _single_valued_assignment(self, curie: CURIE, property: CURIE) -> Optional[str]:
        labels = [a.value for a in self.annotation_assertion_axioms(curie, property=property)]
        if labels:
            if len(labels) > 1:
                logging.warning(f"Multiple labels for {curie} = {labels}")
            val = labels[0]
            rdf_v = val.to_rdf(self.functional_writer.g)
            if isinstance(rdf_v, rdflib.Literal):
                return rdf_v.value
            else:
                raise ValueError(f"Label must be literal, not {val}")

    def definition(self, curie: CURIE) -> Optional[str]:
        return self._single_valued_assignment(curie, HAS_DEFINITION_CURIE)

    def label(self, curie: CURIE) -> str:
        labels = [
            a.value for a in self.annotation_assertion_axioms(curie, property=LABEL_PREDICATE)
        ]
        if labels:
            if len(labels) > 1:
                logging.warning(f"Multiple labels for {curie} = {labels}")
            label = labels[0]
            rdf_v = label.to_rdf(self.functional_writer.g)
            if isinstance(rdf_v, rdflib.Literal):
                return rdf_v.value
            else:
                raise ValueError(f"Label must be literal, not {label}")

    def entities(self, filter_obsoletes=True, owl_type=None) -> Iterable[CURIE]:
        for ax in self._ontology.axioms:
            if isinstance(ax, Declaration):
                uri = ax.v.full_uri(self.functional_writer.g)
                try:
                    yv = self.uri_to_curie(str(uri))
                except ValueError:
                    logging.warning(
                        "could not compress URI %s with functional writer context %s",
                        uri,
                        list(self.functional_writer.g.namespaces()),
                    )
                    continue
                else:
                    yield yv

    def axioms(self, reasoner: Optional[ReasonerConfiguration] = None) -> Iterable[Axiom]:
        ont = self._ontology
        for axiom in ont.axioms:
            yield axiom

    def set_axioms(self, axioms: List[Axiom]) -> None:
        self._ontology.axioms = axioms

    def dump(self, path: str = None, syntax: str = None, **kwargs):
        if syntax is None or syntax == "ofn":
            out = self.ontology_document.to_functional(self.functional_writer)
        elif syntax == "ttl" or syntax == "turtle":
            g = rdflib.Graph()
            self.ontology_document.to_rdf(g)
            out = g.serialize(format="ttl")
        else:
            out = str(self.ontology_document)
        if path is None:
            print(out)
        elif isinstance(path, str):
            with open(path, "w", encoding="UTF-8") as file:
                file.write(str(out))
        else:
            path.write(str(out))

    # ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    # Implements: PatcherInterface
    # ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

    def _set_annotation_predicate_value(self, subject: CURIE, property: CURIE, value: Any):
        for axiom in self.annotation_assertion_axioms(subject, property):
            self._ontology.axioms.remove(axiom)
        self._ontology.axioms.append(
            AnnotationAssertion(
                subject=self.curie_to_entity_iri(subject),
                property=self.curie_to_entity_iri(property),
                value=value,
            )
        )

    def apply_patch(
        self,
        patch: kgcl.Change,
        activity: kgcl.Activity = None,
        metadata: Mapping[PRED_CURIE, Any] = None,
        configuration: kgcl.Configuration = None,
    ) -> Optional[kgcl.Change]:
        if isinstance(patch, kgcl.NodeChange):
            about = patch.about_node
            if isinstance(patch, kgcl.NodeRename):
                self._set_annotation_predicate_value(about, LABEL_PREDICATE, patch.new_value)
            elif isinstance(patch, kgcl.NodeTextDefinitionChange):
                self._set_annotation_predicate_value(about, HAS_DEFINITION_CURIE, patch.new_value)
            elif isinstance(patch, kgcl.NewSynonym):
                self._ontology.axioms.append(
                    AnnotationAssertion(
                        subject=about,
                        property=self.curie_to_entity_iri(HAS_EXACT_SYNONYM),
                        value=patch.new_value,
                    )
                )
            elif isinstance(patch, kgcl.NodeObsoletion):
                self._set_annotation_predicate_value(about, DEPRECATED_PREDICATE, value=True)
            elif isinstance(patch, kgcl.NodeDeletion):
                raise NotImplementedError("Deletions not supported yet")
            elif isinstance(patch, kgcl.NodeCreation):
                self._set_annotation_predicate_value(about, LABEL_PREDICATE, patch.name)
            elif isinstance(patch, kgcl.NameBecomesSynonym):
                label = self.label(about)
                self.apply_patch(
                    kgcl.NodeRename(id=f"{patch.id}-1", about_node=about, new_value=patch.new_value)
                )
                self.apply_patch(
                    kgcl.NewSynonym(id=f"{patch.id}-2", about_node=about, new_value=label)
                )
            else:
                raise NotImplementedError(f"Cannot handle patches of type {type(patch)}")
        elif isinstance(patch, kgcl.EdgeChange):
            about = patch.about_edge
            subject = self.curie_to_uri(patch.subject)
            object = self.curie_to_uri(patch.object)
            if isinstance(patch, kgcl.EdgeCreation):
                if patch.predicate == IS_A or patch.predicate == "is_a":
                    self._ontology.axioms.append(SubClassOf(subject, object))
                else:
                    predicate = self.curie_to_entity_iri(patch.predicate)
                    self._ontology.axioms.append(
                        SubClassOf(subject, ObjectSomeValuesFrom(predicate, object))
                    )
            else:
                raise NotImplementedError(f"Cannot handle patches of type {type(patch)}")
        else:
            raise NotImplementedError(f"Cannot handle patches of type {type(patch)}")
        return patch
