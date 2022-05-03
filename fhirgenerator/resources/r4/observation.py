'''File for handling all operations relating to the Observation resource'''

import uuid
import random
from fhir.resources.observation import Observation

from fhirgenerator.helpers.helpers import makeRandomDate


def generateObservation(resource_detail: dict, patient_id: str, start_date: str, days: int) -> dict:
    '''Generate Observation Resource from resource detail from configuration'''

    observation_id = str(uuid.uuid4())

    observation_code = random.choice(resource_detail['codes'])

    random_date = makeRandomDate(start_date, days)

    if 'enumSetList' in resource_detail:
        enum_set_list = resource_detail['enumSetList']
        if isinstance(enum_set_list[0], dict):
            if 'system' in enum_set_list[0]:
                value_x_type = 'CodeableConcept'
                value_x_value = random.choice(enum_set_list)
            elif 'value' in enum_set_list[0]:
                value_x_type = 'Quantity'
                value_x_value = random.choice(enum_set_list)
        elif len(enum_set_list[0].split(':')) > 1:
            value_x_type = 'Ratio'
            value_x_titer_choice = random.choice(enum_set_list)
            value_x_titer_choice_split = value_x_titer_choice.split(':')
            value_x_value = {
                'numerator': {'value': value_x_titer_choice_split[0]},
                'denominator': {'value': value_x_titer_choice_split[1]}
            }
        elif enum_set_list[0].isnumeric():
            value_x_type = 'Integer'
            value_x_value = random.choice(enum_set_list)
        else:
            value_x_type = 'String'
            value_x_value = random.choice(enum_set_list)
    elif 'minValue' in resource_detail and 'maxValue' in resource_detail:
        min_value = resource_detail['minValue']
        max_value = resource_detail['maxValue']
        if 'decimalValue' in resource_detail:
            decimal_value = resource_detail['decimalValue']
            value_x_type = 'Quantity'
            value_x_value = {
                'value': round(random.uniform(min_value, max_value), decimal_value)
            }
            if decimal_value == 0:
                value_x_value['value'] = float(value_x_value['value'])
            if 'unit' in resource_detail:
                system, code, display = resource_detail['unit'].split('^')
                value_x_value['unit'] = display
                value_x_value['system'] = system
                value_x_value['code'] = code
        else:
            if 'unit' in resource_detail:
                value_x_type = 'Quantity'
                system, code, display = resource_detail['unit'].split('^')
                value_x_value = {
                    'value': round(random.uniform(min_value, max_value)),
                    'unit': display,
                    'system': system,
                    'code': code
                }
            else:
                value_x_type = 'Integer'
                value_x_value = round(random.uniform(min_value, max_value))
    else:
        print("Warning: There was no enumSetList or (minValue and maxValue) in your configuration for this Observation. This Observation will not have a value[x].")
        value_x_type = 'None'
        value_x_value = ''

    observation_data = {
        'id': observation_id,
        'status': 'final',
        'code': {
            'coding': [
                observation_code
            ]
        },
        'subject': {
            'reference': f'Patient/{patient_id}'
        },
        'effectiveDateTime': str(random_date),
        f'value{value_x_type}': value_x_value
    }

    if 'valueNone' in observation_data:
        del observation_data['valueNone']

    observation_resource = Observation(**observation_data).dict()
    return observation_resource
