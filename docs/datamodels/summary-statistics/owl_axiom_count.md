# Slot: owl_axiom_count
_Number of OWL axioms in the ontology or subset_


URI: [reporting:owl_axiom_count](https://w3id.org/linkml/reportowl_axiom_count)




## Inheritance

* [count_statistic](count_statistic.md)
    * **owl_axiom_count**





## Applicable Classes

| Name | Description |
| --- | --- |
[UngroupedStatistics](UngroupedStatistics.md) | A summary statistics report object






## Properties

* Range: [xsd:integer](http://www.w3.org/2001/XMLSchema#integer)







## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| filter | Axiom |



### Schema Source


* from schema: https://w3id.org/linkml/summary_statistics




## LinkML Source

<details>
```yaml
name: owl_axiom_count
annotations:
  filter:
    tag: filter
    value: Axiom
description: Number of OWL axioms in the ontology or subset
from_schema: https://w3id.org/linkml/summary_statistics
rank: 1000
is_a: count_statistic
alias: owl_axiom_count
owner: UngroupedStatistics
domain_of:
- UngroupedStatistics
slot_group: owl_statistic_group
range: integer

```
</details>