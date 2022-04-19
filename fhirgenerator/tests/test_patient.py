'''Testing Patient generator'''

from ..resources.patient import generatePatient
from ..helpers.helpers import calculateAge


def testPatientGenerator():
    '''Test function for Patient Generator'''
    patient_config = {
        "age": 66,
        "gender": 'F',
        "startDate": '01-01-2022'
    }
    created_resource = generatePatient(patient_config)

    assert created_resource['resourceType'] == 'Patient'
    assert created_resource['gender'] == 'female'
    assert calculateAge(created_resource['birthDate'], start=patient_config['startDate']) == patient_config['age']
    assert isinstance(created_resource['name'], list)
    assert isinstance(created_resource['address'], list)
