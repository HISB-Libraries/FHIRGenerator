# FHIRGenerator

Python Package for FHIR Resource Generation

## How to Use this Generator

### Installation

This package requires Python 3.10 or higher. Installation can be done with `pip`:

```
pip install fhirgenerator
```

### Usage

The main form of usage is through the generateResources function:

```
from fhirgenerator import generateResources

output_bundle = generateResources(configuration_dictionary)
```

This function takes in a configuration dictionary. This is most easily stored in a JSON file, but can be declared within the Python file as well. An example configuration file can be found in the package repo at `fhirgenerator/docs/example_config.json`. The below section will also go through what elements in the configuration represent.

### Configuration for generateResources()

#### Meta/Patient Level Configuration

| Key               | Required? | Data Type | Description                                                                                                                                                                                                                                   | Example        |
|-------------------|-----------|-----------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------
| `numberPatients`  | Yes       | integer   | The number of patients you wish to generate                                                                                                                                                                                                   | 10             |
| `ageMin`          | Yes       | integer   | The minimum age of the patients you wish to generate                                                                                                                                                                                          | 0              |
| `ageMax`          | Yes       | integer   | The maximum age of the patients you wish to generate                                                                                                                                                                                          | 89             |
| `genderMFOU`      | Yes       | list      | A list of 4 values: the first represents the percentage of patients generated that have a `Patient.gender` of `male`,  the second for a `gender` of `female`, the third for a `gender` of `other`, and the fourth for a `gender` of `unknown` | [47, 47, 1, 5] |
| `startDate`       | Yes       | string    | The beginning date of the range that the non-Patient resources will be generated in                                                                                                                                                           | "01-01-2022"   |
| `days`            | Yes       | integer   | The total length of time that the non-Patient resources will be generated for                                                                                                                                                                 | 365            |
| `usCorePatient`   | No        | boolean   | If included and is `true`, the Patient resource generated will be a US Core Patient (defaults to a base FHIR Patient)                                                                                                                         | true           |
| `bundleType`      | No        | string    | If included and is `transaction`, the output for `generateResources()` will be of type `transaction` (defaults to a Bundle of type `collection`)                                                                                              | "transaction"  |
| `resourceDetails` | Yes       | list      | See the below section on what data elements an object in the `resourceDetails` list could contain                                                                                                                                             |                |


#### Resource Detail Object in `resourceDetails` Configuration

| Key                     | Resources Affected     | Required?                             | Data Type    | Description                                                                                                                                                                                                                                                                                                                                                                                             | Example                                                                 |
|:-----------------------:|:----------------------:|:-------------------------------------:|:------------:|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------|
| `fhirResource`          | All                    | Yes                                   | string       | This describes what you would like to generate. Currently supports: <ul><li>Condition</li><li>Observation</li><li>US Core Condition</li><li>US Core Lab Result Observation</li>                                                                                                                                                                                                                         | "Observation"                                                           |
| `codes`                 | All                    | Yes                                   | list of dict | This describes what possible codes you would like to populate the resources `code` element. For currently supported resource types, this is required (but may not be in the future when  considering profiles that have a fixed `code`). The dictionaries in this object will have two keys: `system` and `code` (the same format that a FHIR Coding datatype would have, with display being optional). | [{<br />    "system": "http://loinc.org",<br />    "code": "12345-6}]   |
| `enumSetList`           | Observation            | No if `minValue` and `maxValue` exist | list         | Gives a list of possible `Observation.value[x]` choices that resources could have. Currently supported types include: CodeableConcept, Quantity, strings                                                                                                                                                                                                                                                | ["1:8", "1:16", "1:32", 1:64"]                                          |
| `minValue`              | Observation            | No if `enumSetList` exists            | integer      | The minimum value for `Observation.value[x]`                                                                                                                                                                                                                                                                                                                                                            | 1                                                                       |
| `maxValue`              | Observation            | No if `enumSetList` exists            | integer      | The minimum value for `Observation.value[x]`                                                                                                                                                                                                                                                                                                                                                            | 7                                                                       |
| `decimalValue`          | Observation            | No                                    | integer      | If exists, will determine how many decimal places the `Observation.value[x]` will contain (will be represented as `valueQuantity`)                                                                                                                                                                                                                                                                      | 1                                                                       |
| `minOccurancesPerCycle` | Condition, Observation | Yes                                   | integer      | The minimum number of times this resource will appear in one cycle                                                                                                                                                                                                                                                                                                                                      | 2                                                                       |
| `maxOccurancesPerCycle` | Condition, Observation | Yes                                   | integer      | The maximum number of times this resource will appear in one cycle                                                                                                                                                                                                                                                                                                                                      | 3                                                                       |
| `cycleLengthInDays`     | Condition, Observation | Yes                                   | integer      | This value divided by the `days` value will give you the total number of cycles. The total number of resources could therefore be within `[minOccurancesPerCycle * (cycleLengthInDays/days), maxOccurancesPerCycle * (cycleLengthInDays/days)]` (inclusive)                                                                                                                                             | 365                                                                     |


## US Core Support

Support currently exists for generating the following US Core STU4 Profiles:

* US Core Patient
* US Core Condition
    * currently labels it as a `problem-list-item` for the `category` with a `clinicalStatus` of `active`
    * to be US Core compliant, you must provide codes in the `resourceDetails` that are from the US Core Condition Code ValueSet (https://www.hl7.org/fhir/us/core/ValueSet-us-core-condition-code.html). Currently, the generator cannot choose a random code from this expansive list, so you must enter options in the configuration
* US Core Lab Result Observation
    * to be US Core compliant, you must provide codes in the `resourceDetails` that are from LOINC. Currently, the generator cannot choose a random code from all LOINC codes, so you must enter code options in the configuration