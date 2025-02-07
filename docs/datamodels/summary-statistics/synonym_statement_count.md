# Slot: synonym_statement_count
_Number of synonym statements (assertions) in the ontology or subset_


URI: [reporting:synonym_statement_count](https://w3id.org/linkml/reportsynonym_statement_count)




## Inheritance

* [count_statistic](count_statistic.md)
    * **synonym_statement_count**





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
| filter | Synonym |



### Schema Source


* from schema: https://w3id.org/linkml/summary_statistics




## LinkML Source

<details>
```yaml
name: synonym_statement_count
annotations:
  filter:
    tag: filter
    value: Synonym
description: Number of synonym statements (assertions) in the ontology or subset
from_schema: https://w3id.org/linkml/summary_statistics
rank: 1000
is_a: count_statistic
alias: synonym_statement_count
owner: UngroupedStatistics
domain_of:
- UngroupedStatistics
slot_group: metadata_statistic_group
range: integer

```
</details>