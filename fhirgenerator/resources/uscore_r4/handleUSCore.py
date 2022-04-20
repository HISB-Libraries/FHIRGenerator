'''File for handling US Core Resource Generation'''

from fhirgenerator.resources.uscore_r4.usCoreCondition import generateUSCoreCondition
from fhirgenerator.resources.uscore_r4.usCoreLabResultObservation import generateUSCoreLabResultObservation


def handleUSCore(resource_detail: dict, patient_id: str, start_date: str, days: str) -> dict:
    '''Function to handle US Core resource generation'''

    resource_type = resource_detail['fhirResource']
    match resource_type:
        case ['USCoreCondition']:
            return_resource = generateUSCoreCondition()
        case ['USCoreLaboratoryResultObservation']:
            return_resource = generateUSCoreLabResultObservation()

    return return_resource
