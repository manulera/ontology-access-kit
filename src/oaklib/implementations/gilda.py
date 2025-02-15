"""A text annotator based on Gilda."""

import logging
from dataclasses import dataclass
from typing import Iterator

from oaklib.datamodels.text_annotator import TextAnnotation, TextAnnotationConfiguration
from oaklib.interfaces import TextAnnotatorInterface
from oaklib.interfaces.text_annotator_interface import TEXT, nen_annotation

__all__ = [
    "GildaImplementation",
]


@dataclass
class GildaImplementation(TextAnnotatorInterface):
    """Perform named entity normalization on text strings with Gilda [gyori2021]_.

    .. [gyori2021] Benjamin M Gyori, Charles Tapley Hoyt, Albert Steppi (2021)
        `Gilda: biomedical entity text normalization with machine-learned
        disambiguation as a service <https://doi.org/10.1093/bioadv/vbac034>`_,
        *Bioinformatics Advances*, Volume 2, Issue 1, 2022, vbac034,
    """

    def annotate_text(
        self, text: TEXT, configuration: TextAnnotationConfiguration = None
    ) -> Iterator[TextAnnotation]:
        """
        Implements annotate_text from text_annotator_interface by calling the
        `annotate` endpoint using gilda client.

        :param text: Text to be annotated.
        :param configuration: Text annotation configuration.
        :yield: A generator function that returns annotated results.
        """
        if not configuration:
            raise NotImplementedError("Missing text annotation configuration")
        if not configuration.matches_whole_text:
            raise NotImplementedError("Gilda annotator can't be used to match partial text")

        import gilda

        for match in gilda.ground(text):
            term_id_split = match.term.id.split(":")
            if len(term_id_split) == 1:
                curie = f"{match.term.db}:{match.term.id}"
            elif len(term_id_split) == 2:
                curie = match.term.id
                if str(match.term.db) != str(term_id_split[0]):
                    logging.warning(
                        f"Match term db {match.term.db} does not match prefix of {match.term.id}."
                    )
            else:
                raise ValueError(f"Invalid term id: {match.term.id}")

            yield nen_annotation(
                text=text,
                object_id=curie,
                object_label=match.term.entry_name,
            )
