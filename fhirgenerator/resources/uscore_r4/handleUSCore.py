'''File for handling US Core Resource Generation'''

from fhirgenerator.resources.uscore_r4.usCoreBMIObservation import generateUSCoreBMIObservation
from fhirgenerator.resources.uscore_r4.usCoreBodyHeightObservation import generateUSCoreBodyHeightObservation
from fhirgenerator.resources.uscore_r4.usCoreBodyTemperatureObservation import generateUSCoreBodyTemperatureObservation
from fhirgenerator.resources.uscore_r4.usCoreBodyWeightObservation import generateUSCoreBodyWeightObservation
from fhirgenerator.resources.uscore_r4.usCoreCondition import generateUSCoreCondition
from fhirgenerator.resources.uscore_r4.usCoreHeadCircumferenceObservation import generateUSCoreHeadCircumferenceObservation
from fhirgenerator.resources.uscore_r4.usCoreLabResultObservation import generateUSCoreLabResultObservation


def handleUSCore(resource_detail: dict, patient_id: str, start_date: str, days: str) -> dict:
    '''Function to handle US Core resource generation'''

    resource_type = resource_detail['fhirResource']
    match resource_type:
        case ['USCoreCondition']:
            return_resource = generateUSCoreCondition()
        case ['USCoreLaboratoryResultObservation']:
            return_resource = generateUSCoreLabResultObservation()
        case ['USCoreBMIObservation']:
            return_resource = generateUSCoreBMIObservation()
        case ['USCoreHeadCircumferenceObservation']:
            return_resource = generateUSCoreHeadCircumferenceObservation()
        case ['USCoreBodyHeightObservation']:
            return_resource = generateUSCoreBodyHeightObservation()
        case ['USCoreBodyWeightObservation']:
            return_resource = generateUSCoreBodyWeightObservation()
        case ['USCoreBodyTemperatureObservation']:
            return_resource = generateUSCoreBodyTemperatureObservation()

    return return_resource
