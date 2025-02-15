# Slot: mapping_count
_Number of mappings (including xrefs) in the ontology or subset_


URI: [reporting:mapping_count](https://w3id.org/linkml/reportmapping_count)




## Inheritance

* [count_statistic](count_statistic.md)
    * **mapping_count**





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
| filter | Mapping |



### Schema Source


* from schema: https://w3id.org/linkml/summary_statistics




## LinkML Source

<details>
```yaml
name: mapping_count
annotations:
  filter:
    tag: filter
    value: Mapping
description: Number of mappings (including xrefs) in the ontology or subset
from_schema: https://w3id.org/linkml/summary_statistics
rank: 1000
is_a: count_statistic
alias: mapping_count
owner: UngroupedStatistics
domain_of:
- UngroupedStatistics
slot_group: metadata_statistic_group
range: integer

```
</details>