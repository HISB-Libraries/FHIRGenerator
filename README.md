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


#### Resource Detail Object in `resourceDetails` Configuration for Observation

| Key                      | Required                              | Data Type    | Description                                                                                                                                                                                                                                                                                                                                                                                             | Example                                                                |
|:------------------------:|:-------------------------------------:|:------------:|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| `fhirResource`           | Yes                                   | string       | This describes what you would like to generate. Currently supports:                                                                                                                                                                                                                                                                                                                                     | "Observation"                                                          |
| `codes`                  | Yes                                   | list of dict | This describes what possible codes you would like to populate the resources `code` element. For currently supported resource types, this is required (but may not be in the future when  considering profiles that have a fixed `code`). The dictionaries in this object will have two keys: `system` and `code` (the same format that a FHIR Coding datatype would have, with display being optional). | [{<br />    "system": "http://loinc.org",<br />    "code": "12345-6"}] |
| `enumSetList`            | No if `minValue` and `maxValue` exist | list         | Gives a list of possible `Observation.value[x]` choices that resources could have. Currently supported types include: CodeableConcept, Quantity, Integer, Decimal, Ratio, Strings                                                                                                                                                                                                                       | ["1:8", "1:16", "1:32", 1:64"]                                         |
| `minValue`               | No if `enumSetList` exists            | integer      | The minimum value for `Observation.value[x]`                                                                                                                                                                                                                                                                                                                                                            | 1                                                                      |
| `maxValue`               | No if `enumSetList` exists            | integer      | The maximum value for `Observation.value[x]`                                                                                                                                                                                                                                                                                                                                                            | 7                                                                      |
| `decimalValue`           | No                                    | integer      | If exists, will determine how many decimal places the `Observation.value[x]` will contain (will be represented as `valueQuantity`)                                                                                                                                                                                                                                                                      | 1                                                                      |
| `dateType`               | No                                    | string       | If exists, will determine the `valueDateTime`'s format (currently only supports dateTime).                                                                                                                                                                                                                                                                                                              | "dateTime"                                                             |
| `dateRange`              | No                                    | list         | If exists, will determine the `valueDateTime`'s date range. Its a list with two elements, the first element indicating how far behind the `effectiveDateTime` the range will start, and the second element indicating how far behind the `effectiveDateTime` the range will end.                                                                                                                        | [-100, 0]                                                              |
| `unit`                   | No                                    | string       | If exists, will determine the `valueQuantity`'s unit, system, and code. Must be in the form of `system^code^unit`.                                                                                                                                                                                                                                                                                      | "UCUM^[in_i]^Inch"                                                     |
| `minOccurrencesPerCycle` | Yes                                   | integer      | The minimum number of times this resource will appear in one cycle                                                                                                                                                                                                                                                                                                                                      | 2                                                                      |
| `maxOccurrencesPerCycle` | Yes                                   | integer      | The maximum number of times this resource will appear in one cycle                                                                                                                                                                                                                                                                                                                                      | 3                                                                      |
| `cycleLengthInDays`      | Yes                                   | integer      | This value divided by the `days` value will give you the total number of cycles. The total number of resources could therefore be within `[minOccurrencesPerCycle * (cycleLengthInDays/days), maxOccurrencesPerCycle * (cycleLengthInDays/days)]` (inclusive)                                                                                                                                           | 365                                                                    |

How value[x] can take form in this configuration detail:

* valueCodeableConcept
    * Detail needs to have an `enumSetList` that is a list of CodeableConcepts (**NOTE: This is a list of CodeableConcepts, not Codings**)
* valueDateTime
    * Detail needs to have a `dateRange` with an optional `dateType`
* valueQuantity
    * Detail would need to have an `enumSetList` that is a list of Quantitys or a `minValue`, `maxValue`, and `unit`, with an optional `decimalValue`
* valueRatio
    * Detail would need to have an `enumSetList` that is a list of strings that contain "numerator:denominator"
* valueInteger
    * Detail would need to have a `minValue`, 'maxValue`, and NO `decimalValue`

#### Resource Detail Object in `resourceDetails` Configuration for Condition

| Key                      | Required                              | Data Type    | Description                                                                                                                                                                                                                                                                                                                                                                                             | Example                                                                        |
|:------------------------:|:-------------------------------------:|:------------:|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| `fhirResource`           | Yes                                   | string       | This describes what you would like to generate.                                                                                                                                                                                                                                                                                                                                                         | "Condition"                                                                    |
| `codes`                  | Yes                                   | list of dict | This describes what possible codes you would like to populate the resources `code` element. For currently supported resource types, this is required (but may not be in the future when  considering profiles that have a fixed `code`). The dictionaries in this object will have two keys: `system` and `code` (the same format that a FHIR Coding datatype would have, with display being optional). | [{<br />    "system": "http://snomed.info/sct",<br />    "code": "736686006"}] |
| `minOccurrencesPerCycle` | Yes                                   | integer      | The minimum number of times this resource will appear in one cycle                                                                                                                                                                                                                                                                                                                                      | 2                                                                              |
| `maxOccurrencesPerCycle` | Yes                                   | integer      | The maximum number of times this resource will appear in one cycle                                                                                                                                                                                                                                                                                                                                      | 3                                                                              |
| `cycleLengthInDays`      | Yes                                   | integer      | This value divided by the `days` value will give you the total number of cycles. The total number of resources could therefore be within `[minOccurrencesPerCycle * (cycleLengthInDays/days), maxOccurrencesPerCycle * (cycleLengthInDays/days)]` (inclusive)                                                                                                                                           | 365                                                                            |

#### Resource Detail Object in `resourceDetails` Configuration for MedicationStatement

| Key                      | Required                                       | Data Type    | Description                                                                                                                                                                                                                                                                     | Example                                                                                                                                          |
|:------------------------:|:----------------------------------------------:|:------------:|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------------------------------:|
| `fhirResource`           | Yes                                            | string       | This describes what you would like to generate.                                                                                                                                                                                                                                 | "MedicationStatement"                                                                                                                            |
| `codes`                  | Yes                                            | list of dict | This describes what possible codes you would like to populate the resources `medicationCodeableConcept` element. The dictionaries in this object will have two keys: `system` and `code` (the same format that a FHIR Coding datatype would have, with display being optional). | [{<br />    "system": "http://www.nlm.nih.gov/research/umls/rxnorm",<br />    "code": "7984"}]                                                   |
| `enumSetList`            | No if `minValue`, `maxValue`, and `unit` exist | list         | Gives a list of possible `MedicationStatement.dosage[0].doseAndRate[0].doseQuantity` choices that resources could have. Currently supported types include: CodeableConcept, Quantity, Integer, Decimal, Ratio, Strings                                                          | ["1 http://terminology.hl7.org/CodeSystem/v3-orderableDrugForm^TAB^TAB", "2 http://terminology.hl7.org/CodeSystem/v3-orderableDrugForm^TAB^TAB"] |
| `minValue`               | No if `enumSetList` exists                     | integer      | The minimum value for `MedicationStatement.dosage[0].doseAndRate[0].doseQuantity`                                                                                                                                                                                               | 1                                                                                                                                                |
| `maxValue`               | No if `enumSetList` exists                     | integer      | The maximum value for `MedicationStatement.dosage[0].doseAndRate[0].doseQuantity`                                                                                                                                                                                               | 7                                                                                                                                                |
| `decimalValue`           | No                                             | integer      | If exists, will determine how many decimal places the `MedicationStatement.dosage[0].doseAndRate[0].doseQuantity`                                                                                                                                                               | 1                                                                                                                                                |
| `unit`                   | No if `enumSetList` exists                     | string       | If exists, will determine the `doseQuantity`'s unit, system, and code. Must be in the form of `system^code^unit`.                                                                                                                                                               | "http://terminology.hl7.org/CodeSystem/v3-orderableDrugForm^TAB^TAB"                                                                             |
| `minOccurrencesPerCycle` | Yes                                            | integer      | The minimum number of times this resource will appear in one cycle                                                                                                                                                                                                              | 2                                                                                                                                                |
| `maxOccurrencesPerCycle` | Yes                                            | integer      | The maximum number of times this resource will appear in one cycle                                                                                                                                                                                                              | 3                                                                                                                                                |
| `cycleLengthInDays`      | Yes                                            | integer      | This value divided by the `days` value will give you the total number of cycles. The total number of resources could therefore be within `[minOccurrencesPerCycle * (cycleLengthInDays/days), maxOccurrencesPerCycle * (cycleLengthInDays/days)]` (inclusive)                   | 365                                                                                                                                              |

#### Resource Detail Object in `resourceDetails` Configuration for Encounter

| Key                      | Required                              | Data Type    | Description                                                                                                                                                                                                                                                                                                                                                                                             | Example                                                                                                 |
|:------------------------:|:-------------------------------------:|:------------:|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------:|
| `fhirResource`           | Yes                                   | string       | This describes what you would like to generate.                                                                                                                                                                                                                                                                                                                                                         | "Encounter"                                                                                             |
| `codes`                  | Yes                                   | list of dict | This describes what possible codes you would like to populate the resources `type` element. For currently supported resource types, this is required (but may not be in the future when considering profiles that have a fixed `code`). The dictionaries in this object will have two keys: `system` and `code` (the same format that a FHIR Coding datatype would have, with display being optional).  | [{<br />    "system": "http://terminology.hl7.org/CodeSystem/encounter-type",<br />    "code": "ADMS"}] |
| `class`                  | No                                    | dict         | This describes what class you would like the Encounter to have. If not included, the Encounters will contain classes randomly chosen from the allowed ValueSet.                                                                                                                                                                                                                                         | {<br />    "system": "http://terminology.hl7.org/CodeSystem/v3-ActCode",<br />    "code": "AMB"}        |
| `minOccurrencesPerCycle` | Yes                                   | integer      | The minimum number of times this resource will appear in one cycle                                                                                                                                                                                                                                                                                                                                      | 2                                                                                                       |
| `maxOccurrencesPerCycle` | Yes                                   | integer      | The maximum number of times this resource will appear in one cycle                                                                                                                                                                                                                                                                                                                                      | 3                                                                                                       |
| `cycleLengthInDays`      | Yes                                   | integer      | This value divided by the `days` value will give you the total number of cycles. The total number of resources could therefore be within `[minOccurrencesPerCycle * (cycleLengthInDays/days), maxOccurrencesPerCycle * (cycleLengthInDays/days)]` (inclusive)                                                                                                                                           | 365                                                                                                     |

#### Resource Detail Object in `resourceDetails` Configuration for Procedure

| Key                      | Required                              | Data Type    | Description                                                                                                                                                                                                                                                                                                                                                                                             | Example                                                                                                 |
|:------------------------:|:-------------------------------------:|:------------:|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------:|
| `fhirResource`           | Yes                                   | string       | This describes what you would like to generate.                                                                                                                                                                                                                                                                                                                                                         | "Procedure"                                                                                             |
| `codes`                  | Yes                                   | list of dict | This describes what possible codes you would like to populate the resources `code` element. For currently supported resource types, this is required (but may not be in the future when considering profiles that have a fixed `code`). The dictionaries in this object will have two keys: `system` and `code` (the same format that a FHIR Coding datatype would have, with display being optional).  | [{<br />    "system": "http://snomed.info/sct",<br />    "code": "115006"}]                             |
| `minOccurrencesPerCycle` | Yes                                   | integer      | The minimum number of times this resource will appear in one cycle                                                                                                                                                                                                                                                                                                                                      | 2                                                                                                       |
| `maxOccurrencesPerCycle` | Yes                                   | integer      | The maximum number of times this resource will appear in one cycle                                                                                                                                                                                                                                                                                                                                      | 3                                                                                                       |
| `cycleLengthInDays`      | Yes                                   | integer      | This value divided by the `days` value will give you the total number of cycles. The total number of resources could therefore be within `[minOccurrencesPerCycle * (cycleLengthInDays/days), maxOccurrencesPerCycle * (cycleLengthInDays/days)]` (inclusive)                                                                                                                                           | 365                                                                                                     |

## US Core Support

Support currently exists for generating the following US Core STU4 Profiles:

* US Core Patient
* US Core Condition
    * currently labels it as a `problem-list-item` for the `category` with a `clinicalStatus` of `active`
    * to be US Core compliant, you must provide codes in the `resourceDetails` that are from the US Core Condition Code ValueSet (https://www.hl7.org/fhir/us/core/ValueSet-us-core-condition-code.html). Currently, the generator cannot choose a random code from this expansive list, so you must enter options in the configuration
* US Core Lab Result Observation
    * to be US Core compliant, you must provide codes in the `resourceDetails` that are from LOINC. Currently, the generator cannot choose a random code from all LOINC codes, so you must enter code options in the configuration
* US Core Vital Signs
    * US Core BMI
    * US Core Head Circumference
    * US Core Body Height
* US Core Location

## Extending the FHIR Generator Package

### Command Line Tooling

The package supports a command line function for generating a template file for easier time extending this package. Similar to Angular's `ng new component {name}`, the command line tool uses the following format:

```fhirgenerator new profile {resource_type} {profile_name}```

Where:

* `resource_type` is going to be which resource you would be building a generator for (examples include observation and condition)
* `profile_name` is the name of the profile for which you are building a generator for

# History

## 0.1.3

* Fixed valueDateTime generation in components

## 0.1.2

* Added support for Observation.valueDateTime generation
* Added support for Location generation
* Added support for US Core Location generation
* Added SSN identifier and marital status to Patients

## 0.1.1

* Added support for Observation.component generation (TODO: write information in README about how to use it)
* Fixed testing suite to actually test different value[x] cases
* Fixed CodeableConcept generation to work

## 0.1.0

* First minor release
* Added chance for patient to have a maiden name (40% chance) or a usual name (60% chance)
* Added chance for patient to have an old address (25% chance)
* Updated Address.py to use fhir.resources typed Address
* Created ContactPoint generator to generate ContactPoint data types
    * Patients will all have phone numbers and 90% of them will have emails
* Added command line functionality for generating a template file for extending the package. See above section "Extending the FHIR Generator Package" for usage instructions

## 0.0.10

* Removed superfluous print statement in helpers.helpers.default
* Fixed state name generation to use 2 letter codes versus full name
* Fixed US Core generation to be valid

## 0.0.9

* Add US Core Race and Ethnicity to US Core Patients

## 0.0.8

* If decimal is .0, its stored as an integer in the data
* Add zip codes and phone numbers to Patients

## 0.0.7

* Added US Core Body Weight, US Core Body Temperature, US Core Heart Rate
* Added support for not generating `Observation.value[x]` to avoid errors in any wrappers

## 0.0.6

* Improve README to have better documentation for each resource type in resource details
* Fix spelling error of occurrence

## 0.0.5

Improvements

* Updated README
* Added this History page
* Added Procedure, MedicationStatement, Encounter
* Added US Core BMI, Head Circumference (other vital signs in progress)
* Added associated tests for new profiles
* Added support for `unit` in configuration to specify a unit for a `valueQuantity` (must be in form `system^code^display`)
* Added support for not including a `decimalValue` in configuration to create a `valueInteger` (unless theres a unit, then it will create a `valueQuantity`)
* Expanded testing scripts to be more comprehensive

## 0.0.4

* Changed `enumSetList` in configuration to be a list and to include:
    * a list of titers (as strings) for a valueRatio
    * a list of decimals for a valueQuantity
    * a list of Codings for a valueCodeableConcept
    * a list of strings (that are not titers) for a valueString (this is the default behavior if the `enumSetList` does not meet one of the above criteria)
* Improved testing scripts to be more comprehensive

## 0.0.3

* First working release of package