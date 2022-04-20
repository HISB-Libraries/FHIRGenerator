# FHIRGenerator

Python Package for FHIR Resource Generation

## Directory Structure

```
├── LICENSE
├── README.md
├── dist (folder for package distribution)
│   ├── fhir-generator-0.0.1.tar.gz
│   └── fhir_generator-0.0.1-py3-none-any.whl
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