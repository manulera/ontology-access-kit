# Slot: rdf_triple_count
_Number of RDF triples in the ontology or subset_


URI: [reporting:rdf_triple_count](https://w3id.org/linkml/reportrdf_triple_count)




## Inheritance

* [count_statistic](count_statistic.md)
    * **rdf_triple_count**





## Applicable Classes

| Name | Description |
| --- | --- |
[UngroupedStatistics](UngroupedStatistics.md) | A summary statistics report object






## Properties

* Range: [xsd:integer](http://www.w3.org/2001/XMLSchema#integer)







## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/linkml/summary_statistics




## LinkML Source

<details>
```yaml
name: rdf_triple_count
description: Number of RDF triples in the ontology or subset
from_schema: https://w3id.org/linkml/summary_statistics
rank: 1000
is_a: count_statistic
alias: rdf_triple_count
owner: UngroupedStatistics
domain_of:
- UngroupedStatistics
slot_group: owl_statistic_group
range: integer

```
</details>