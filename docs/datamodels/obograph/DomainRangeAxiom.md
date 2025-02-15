# Class: DomainRangeAxiom



URI: [og:DomainRangeAxiom](https://github.com/geneontology/obographs/DomainRangeAxiom)


```{mermaid}
 classDiagram
    class DomainRangeAxiom
      Axiom <|-- DomainRangeAxiom
      
      DomainRangeAxiom : allValuesFromEdges
      DomainRangeAxiom : domainClassIds
      DomainRangeAxiom : meta
      DomainRangeAxiom : predicateId
      DomainRangeAxiom : rangeClassIds
      
```




## Inheritance
* [Axiom](Axiom.md)
    * **DomainRangeAxiom**



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [predicateId](predicateId.md) | 0..1 <br/> [xsd:string](http://www.w3.org/2001/XMLSchema#string) |  | direct |
| [domainClassIds](domainClassIds.md) | 0..* <br/> [xsd:string](http://www.w3.org/2001/XMLSchema#string) |  | direct |
| [rangeClassIds](rangeClassIds.md) | 0..* <br/> [xsd:string](http://www.w3.org/2001/XMLSchema#string) |  | direct |
| [allValuesFromEdges](allValuesFromEdges.md) | 0..* <br/> [Edge](Edge.md) | A list of edges that represent subclasses of universal restrictions | direct |
| [meta](meta.md) | 0..1 <br/> [Meta](Meta.md) |  | [Axiom](Axiom.md) |



## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Graph](Graph.md) | [domainRangeAxioms](domainRangeAxioms.md) | range | [DomainRangeAxiom](DomainRangeAxiom.md) |






## Identifier and Mapping Information







### Schema Source


* from schema: https://github.com/geneontology/obographs





## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | og:DomainRangeAxiom |
| native | og:DomainRangeAxiom |


## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: DomainRangeAxiom
from_schema: https://github.com/geneontology/obographs
rank: 1000
is_a: Axiom
slots:
- predicateId
- domainClassIds
- rangeClassIds
- allValuesFromEdges

```
</details>

### Induced

<details>
```yaml
name: DomainRangeAxiom
from_schema: https://github.com/geneontology/obographs
rank: 1000
is_a: Axiom
attributes:
  predicateId:
    name: predicateId
    from_schema: https://github.com/geneontology/obographs
    rank: 1000
    alias: predicateId
    owner: DomainRangeAxiom
    domain_of:
    - DomainRangeAxiom
    - PropertyChainAxiom
    range: string
  domainClassIds:
    name: domainClassIds
    from_schema: https://github.com/geneontology/obographs
    rank: 1000
    multivalued: true
    alias: domainClassIds
    owner: DomainRangeAxiom
    domain_of:
    - DomainRangeAxiom
    range: string
  rangeClassIds:
    name: rangeClassIds
    from_schema: https://github.com/geneontology/obographs
    rank: 1000
    multivalued: true
    alias: rangeClassIds
    owner: DomainRangeAxiom
    domain_of:
    - DomainRangeAxiom
    range: string
  allValuesFromEdges:
    name: allValuesFromEdges
    description: A list of edges that represent subclasses of universal restrictions
    from_schema: https://github.com/geneontology/obographs
    rank: 1000
    multivalued: true
    alias: allValuesFromEdges
    owner: DomainRangeAxiom
    domain_of:
    - Graph
    - DomainRangeAxiom
    range: Edge
  meta:
    name: meta
    from_schema: https://github.com/geneontology/obographs
    rank: 1000
    alias: meta
    owner: DomainRangeAxiom
    domain_of:
    - GraphDocument
    - Graph
    - Node
    - PropertyValue
    - Axiom
    range: Meta

```
</details>