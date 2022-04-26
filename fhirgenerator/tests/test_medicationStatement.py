'''Testing MedicationStatement generator'''

import orjson
from dateutil import parser
import datetime
from fhirgenerator.resources.r4.medicationStatement import generateMedicationStatement
from fhirgenerator.helpers.helpers import default


def testProcedureGenerator():
    '''Test function for Procedure Generator'''

    with open('fhirgenerator/tests/input/config.json', 'rb') as infile:
        config_dict = orjson.loads(infile.read())

    patient_id = '26774-827647-736278-3737646'

    ms_resource_details = []
    for detail in config_dict['resourceDetails']:
        if detail['fhirResource'] == 'MedicationStatement':
            ms_resource_details.append(detail)

    for i, detail in enumerate(ms_resource_details):
        created_resource = generateMedicationStatement(detail, patient_id, config_dict['startDate'], config_dict['days'])

        assert created_resource['resourceType'] == 'MedicationStatement'
        assert created_resource['status'] == 'completed'
        assert created_resource['medicationCodeableConcept']['coding'][0] in detail['codes']
        assert (created_resource['effectiveDateTime'] >= parser.parse(config_dict['startDate'])) and (created_resource['effectiveDateTime'] <= parser.parse(config_dict['startDate']) + datetime.timedelta(days=config_dict['days']))
        assert created_resource['subject']['reference'] == f'Patient/{patient_id}'
        # TODO: add assertions for MedicationStatement.dosage[0].doseAndRate[0].doseQuantity

        with open(f'fhirgenerator/tests/output/test_medicationStatement_{i}.json', 'wb') as outfile:
            outfile.write(orjson.dumps(created_resource, default=default, option=orjson.OPT_NAIVE_UTC))
