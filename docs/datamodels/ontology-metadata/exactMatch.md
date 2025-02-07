# Slot: exactMatch

URI: [skos:exactMatch](http://www.w3.org/2004/02/skos/core#exactMatch)




## Inheritance

* [match](match.md) [ [match_aspect](match_aspect.md)]
    * **exactMatch**





## Applicable Classes

| Name | Description |
| --- | --- |
[HasMappings](HasMappings.md) | 
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

* Range: [Thing](Thing.md)
* Multivalued: True








## Identifier and Mapping Information







### Schema Source


* from schema: http://purl.obolibrary.org/obo/omo/schema




## LinkML Source

<details>
```yaml
name: exactMatch
from_schema: http://purl.obolibrary.org/obo/omo/schema
rank: 1000
is_a: match
slot_uri: skos:exactMatch
multivalued: true
alias: exactMatch
domain_of:
- HasMappings
range: Thing

```
</details>