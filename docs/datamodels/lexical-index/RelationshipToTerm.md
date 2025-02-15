# Class: RelationshipToTerm
_A relationship of an ontology element to a lexical term_




URI: [li:RelationshipToTerm](https://w3id.org/linkml/lexical_index/RelationshipToTerm)


```{mermaid}
 classDiagram
    class RelationshipToTerm
      RelationshipToTerm : element
      RelationshipToTerm : element_term
      RelationshipToTerm : pipeline
      RelationshipToTerm : predicate
      RelationshipToTerm : source
      RelationshipToTerm : synonymized
      
```



<!-- no inheritance hierarchy -->


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [predicate](predicate.md) | 0..1 <br/> [xsd:anyURI](http://www.w3.org/2001/XMLSchema#anyURI) |  | direct |
| [element](element.md) | 0..1 <br/> [xsd:anyURI](http://www.w3.org/2001/XMLSchema#anyURI) |  | direct |
| [element_term](element_term.md) | 0..1 <br/> NONE | the original term used in the element | direct |
| [source](source.md) | 0..1 <br/> [xsd:anyURI](http://www.w3.org/2001/XMLSchema#anyURI) |  | direct |
| [pipeline](pipeline.md) | 0..* <br/> [LexicalTransformationPipeline](LexicalTransformationPipeline.md) |  | direct |
| [synonymized](synonymized.md) | 0..1 <br/> [xsd:boolean](http://www.w3.org/2001/XMLSchema#boolean) |  | direct |



## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [LexicalGrouping](LexicalGrouping.md) | [relationships](relationships.md) | range | [RelationshipToTerm](RelationshipToTerm.md) |






## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/linkml/lexical_index





## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | li:RelationshipToTerm |
| native | li:RelationshipToTerm |


## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: RelationshipToTerm
description: A relationship of an ontology element to a lexical term
from_schema: https://w3id.org/linkml/lexical_index
rank: 1000
attributes:
  predicate:
    name: predicate
    from_schema: https://w3id.org/linkml/lexical_index
    rank: 1000
    range: uriorcurie
  element:
    name: element
    from_schema: https://w3id.org/linkml/lexical_index
    rank: 1000
    range: uriorcurie
  element_term:
    name: element_term
    description: the original term used in the element
    from_schema: https://w3id.org/linkml/lexical_index
    rank: 1000
  source:
    name: source
    from_schema: https://w3id.org/linkml/lexical_index
    rank: 1000
    range: uriorcurie
  pipeline:
    name: pipeline
    from_schema: https://w3id.org/linkml/lexical_index
    rank: 1000
    multivalued: true
    range: LexicalTransformationPipeline
  synonymized:
    name: synonymized
    from_schema: https://w3id.org/linkml/lexical_index
    rank: 1000
    range: boolean

```
</details>

### Induced

<details>
```yaml
name: RelationshipToTerm
description: A relationship of an ontology element to a lexical term
from_schema: https://w3id.org/linkml/lexical_index
rank: 1000
attributes:
  predicate:
    name: predicate
    from_schema: https://w3id.org/linkml/lexical_index
    rank: 1000
    alias: predicate
    owner: RelationshipToTerm
    domain_of:
    - RelationshipToTerm
    range: uriorcurie
  element:
    name: element
    from_schema: https://w3id.org/linkml/lexical_index
    rank: 1000
    alias: element
    owner: RelationshipToTerm
    domain_of:
    - RelationshipToTerm
    range: uriorcurie
  element_term:
    name: element_term
    description: the original term used in the element
    from_schema: https://w3id.org/linkml/lexical_index
    rank: 1000
    alias: element_term
    owner: RelationshipToTerm
    domain_of:
    - RelationshipToTerm
    range: string
  source:
    name: source
    from_schema: https://w3id.org/linkml/lexical_index
    rank: 1000
    alias: source
    owner: RelationshipToTerm
    domain_of:
    - RelationshipToTerm
    range: uriorcurie
  pipeline:
    name: pipeline
    from_schema: https://w3id.org/linkml/lexical_index
    rank: 1000
    multivalued: true
    alias: pipeline
    owner: RelationshipToTerm
    domain_of:
    - RelationshipToTerm
    range: LexicalTransformationPipeline
  synonymized:
    name: synonymized
    from_schema: https://w3id.org/linkml/lexical_index
    rank: 1000
    alias: synonymized
    owner: RelationshipToTerm
    domain_of:
    - RelationshipToTerm
    range: boolean

```
</details>