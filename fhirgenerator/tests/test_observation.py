'''Testing Observation generator'''

import orjson
from dateutil import parser
import datetime
from fhirgenerator.resources.r4.observation import generateObservation
from fhirgenerator.helpers.helpers import default


def testObservationGenerator():
    '''Test function for Observation Generator'''

    with open('fhirgenerator/tests/input/config.json', 'rb') as infile:
        config_dict = orjson.loads(infile.read())

    patient_id = '26774-827647-736278-3737646'

    observation_resource_details = []
    for detail in config_dict['resourceDetails']:
        if detail['fhirResource'] == 'Observation':
            observation_resource_details.append(detail)

    for i, detail in enumerate(observation_resource_details):

        if 'enumSetList' in detail:
            enum_set_list = detail['enumSetList']
            if len(enum_set_list[0].split(':')) > 1:
                value_x_type = 'Ratio'
            elif 'system' in enum_set_list[0]:
                value_x_type = 'CodeableConcept'
            elif 'value' in enum_set_list[0]:
                value_x_type = 'Quantity'
            else:
                value_x_type = 'String'
        elif 'decimalValue' in detail:
            value_x_type = 'Quantity'
        else:
            value_x_type = 'Integer'

        created_resource = generateObservation(detail, patient_id, config_dict['startDate'], config_dict['days'])

        assert created_resource['resourceType'] == 'Observation'
        assert created_resource['status'] == 'final'
        assert created_resource['code']['coding'][0] in detail['codes']
        assert (created_resource['effectiveDateTime'] >= parser.parse(config_dict['startDate'])) and (created_resource['effectiveDateTime'] <= parser.parse(config_dict['startDate']) + datetime.timedelta(days=config_dict['days']))
        assert created_resource['subject']['reference'] == f'Patient/{patient_id}'

        match value_x_type:
            case ['Ratio']:
                assert created_resource['valueRatio']['numerator'] + ':' + created_resource['valueRatio']['denominator'] in detail['enumSetList']
            case ['CodeableConcept']:
                assert created_resource['valueCodeableConcept']['coding'][0] in detail['enumSetList']
            case ['Quantity']:
                if 'enumSetList' in detail:
                    assert created_resource['valueQuantity'] in detail['enumSetList']
                else:
                    assert created_resource['valueQuantity']['value'] <= detail['maxValue'] and created_resource['valueQuantity']['value'] >= detail['minValue']
                    test_system, test_code, test_unit = detail['unit'].split('^')
                    assert created_resource['valueQuantity']['system'] == test_system
                    assert created_resource['valueQuantity']['code'] == test_code
                    assert created_resource['valueQuantity']['unit'] == test_unit
            case ['String']:
                assert created_resource['valueString'] in detail['enumSetList']
            case ['Integer']:
                if 'enumSetList' in detail:
                    assert created_resource['valueInteger'] in detail['enumSetList']
                else:
                    assert created_resource['valueInteger'] <= detail['maxValue'] and created_resource['valueInteger'] >= detail['minValue']

        with open(f'fhirgenerator/tests/output/test_observation_{i}.json', 'wb') as outfile:
            outfile.write(orjson.dumps(created_resource, default=default, option=orjson.OPT_NAIVE_UTC))


# TODO: write more observation tests for all possible value[x] that the package supports
