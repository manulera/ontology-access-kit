# Slot: creator

URI: [dcterms:creator](http://purl.org/dc/terms/creator)




## Inheritance

* [provenance_property](provenance_property.md)
    * **creator**





## Applicable Classes

| Name | Description |
| --- | --- |
[HasProvenance](HasProvenance.md) | 
[Ontology](Ontology.md) | An OWL ontology
[Term](Term.md) | A NamedThing that includes classes, properties, but not ontologies
[Class](Class.md) | 
[Property](Property.md) | 
[AnnotationProperty](AnnotationProperty.md) | A property used in non-logical axioms
[ObjectProperty](ObjectProperty.md) | A property that connects two objects in logical axioms
[TransitiveProperty](TransitiveProperty.md) | An ObjectProperty with the property of transitivity
[NamedIndividual](NamedIndividual.md) | An instance that has a IRI
[HomoSapiens](HomoSapiens.md) | An individual human being
[Subset](Subset.md) | A collection of terms grouped for some purpose






## Properties

* Range: [HomoSapiens](HomoSapiens.md)
* Multivalued: True








## Identifier and Mapping Information







### Schema Source


* from schema: http://purl.obolibrary.org/obo/omo/schema




## LinkML Source

<details>
```yaml
name: creator
from_schema: http://purl.obolibrary.org/obo/omo/schema
close_mappings:
- prov:wasAttributedTo
rank: 1000
is_a: provenance_property
slot_uri: dcterms:creator
multivalued: true
alias: creator
domain_of:
- HasProvenance
- Ontology
range: HomoSapiens
structured_pattern:
  syntax: '{orcid_regex}'
  interpolated: true
  partial_match: false

```
</details>