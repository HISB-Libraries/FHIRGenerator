# History

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