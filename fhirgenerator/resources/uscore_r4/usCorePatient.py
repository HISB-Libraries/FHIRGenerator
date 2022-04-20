'''File for handling all operations relating to the US Core Patient resource'''

from fhirgenerator.resources.r4.patient import generatePatient


def generateUSCorePatient(config: dict) -> dict:
    '''Generate Patient Resource'''
    patient_resource = generatePatient(config)
    patient_resource['meta']['profile'] = ['http://hl7.org/fhir/us/core/StructureDefinition/us-core-patient']
    return patient_resource
