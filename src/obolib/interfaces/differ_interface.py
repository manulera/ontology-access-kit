from abc import ABC
from typing import Dict, List, Iterable

from obolib.interfaces.basic_ontology_interface import BasicOntologyInterface
from obolib.resource import OntologyResource
from obolib.types import CURIE


class DifferInterface(BasicOntologyInterface, ABC):
    """
    Generates descriptions of differences

    """

    def diff(self, left_ontology_id: CURIE, right_ontology_id: CURIE) -> str:
        """
        Diffs two ontologies - both must be ontologies wrapped by the current implementation

        :param left_ontology_id:
        :param right_ontology_id:
        :return: TBD KGCL?
        """
