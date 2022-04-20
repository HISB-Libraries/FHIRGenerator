# FHIRGenerator

Python Package for FHIR Resource Generation

## Directory Structure

```
├── LICENSE
├── README.md
├── fhirgenerator (high-level package folder)
│   ├── __init__.py
│   ├── docs (place for documentation of the package)
│   │   └── __init__.py
│   ├── helpers (helper functions)
│   │   ├── __init__.py
│   │   └── helpers.py
│   ├── main.py (main entrypoint for the package with generateResources function)
│   ├── resources (resource-level generation functions)
│   │   ├── __init__.py
│   │   ├── bundle.py
│   │   ├── condition.py
│   │   ├── observation.py
│   │   └── patient.py
│   ├── tests (tests for testing resource-level functions as well as generateResources)
│   │   ├── __init__.py
│   │   ├── input
│   │   │   └── config.json
│   │   ├── output
│   │   │   ├── test_bundle_collection.json
│   │   │   ├── test_bundle_transaction.json
│   │   │   ├── test_condition_0.json
│   │   │   ├── test_main_collection.json
│   │   │   ├── test_main_transaction.json
│   │   │   ├── test_observation_0.json
│   │   │   ├── test_observation_1.json
│   │   │   └── test_patient.json
│   │   ├── test_bundle.py
│   │   ├── test_condition.py
│   │   ├── test_main.py
│   │   ├── test_observation.py
│   │   └── test_patient.py
│   └── types (type-level generators for generating specific FHIR data types)
│       ├── __init__.py
│       ├── address.py
│       ├── configurationDictionary.py
│       ├── humanName.py
│       └── identifier.py
├── pylama.ini (config file for pylama linting)
├── pyproject.toml (package file)
├── requirements.txt (requirements file for package development)
└── setup.py (package setup file)
```

## US Core Support

Support currently exists for generating the following US Core STU4 Profiles:

* US Core Patient
    * add this to the configuration file to indicate you want a US Core Patient: `"usCorePatient": true`
* US Core Condition
    * currently labels it as a `problem-list-item` for the `category` with a `clinicalStatus` of `active`
    * to be US Core compliant, you must provide codes in the `resourceDetails` that are from the US Core Condition Code ValueSet (https://www.hl7.org/fhir/us/core/ValueSet-us-core-condition-code.html). Currently, the generator cannot choose a random code from this expansive list, so you must enter options in the configuration
* US Core Lab Result Observation
    * to be US Core compliant, you must provide codes in the `resourceDetails` that are from LOINC. Currently, the generator cannot choose a random code from all LOINC codes, so you must enter code options in the configuration