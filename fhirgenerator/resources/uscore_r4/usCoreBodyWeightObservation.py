'''File for handling all operations relating to the US Core Body Weight Observation resource'''

from fhirgenerator.resources.r4.observation import generateObservation
from fhir.resources.observation import Observation


def generateUSCoreBodyWeightObservation(detail: dict, patient_id: str, start_date: str, days: str) -> dict:
    '''Generate a US Core Body Weight Observation'''

    detail['codes'] = [{'system': 'http://loinc.org', 'code': '29463-7'}]
    observation_resource = generateObservation(detail, patient_id, start_date, days)
    observation_resource['meta'] = {'profile': ['http://hl7.org/fhir/us/core/StructureDefinition/us-core-body-weight']}
    observation_resource['category'] = [{"coding": [{
        "system": "http://terminology.hl7.org/CodeSystem/observation-category",
        "code": "vital-signs",
        "display": "Vital Signs"
    }]}]

    observation_resource = Observation(**observation_resource).dict()

    return observation_resource
