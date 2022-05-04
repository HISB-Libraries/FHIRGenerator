'''Testing Patient generator'''

import orjson
from fhirgenerator.resources.r4.patient import generatePatient
from fhirgenerator.helpers.helpers import calculateAge, default


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
    assert isinstance(created_resource['telecom'], list)
    assert created_resource['identifier'][0]['system'] == 'urn:fhirgen:mrn'
    assert created_resource['identifier'][0]['type']['coding'][0] == {'system': 'http://terminology.hl7.org/CodeSystem/v2-0203', 'code': 'MR'}
    assert len(created_resource['identifier'][0]['value']) == 11

    with open('fhirgenerator/tests/output/test_patient.json', 'wb') as outfile:
        outfile.write(orjson.dumps(created_resource, default=default, option=orjson.OPT_NAIVE_UTC))
