'''File for handling all operations relating to the Observation resource'''

import uuid
import random
import datetime
from dateutil import parser
from fhir.resources.observation import Observation


def generateObservation(resource_detail: dict, patient_id: str, start_date: str, days: int) -> dict:
    '''Generate Observation Resource from resource detail from configuration'''

    observation_id = str(uuid.uuid4())

    observation_code = random.choice(resource_detail['codes'])

    start_date = parser.parse(start_date)
    random_number_of_days = random.randrange(days)
    random_date = start_date + datetime.timedelta(days=random_number_of_days)

    if 'enumSetList' in resource_detail:
        enum_set_split = resource_detail['enumSetList'].split(',')
        enum_set_split = [enum.strip(' ') for enum in enum_set_split]
        if len(enum_set_split[0].split(':')) > 1:
            value_x_type = 'Ratio'
            value_x_titer_choice = random.choice(enum_set_split)
            value_x_titer_choice_split = value_x_titer_choice.split(':')
            value_x_value = {
                'numerator': {'value': value_x_titer_choice_split[0]},
                'denominator': {'value': value_x_titer_choice_split[1]}
            }
        else:
            value_x_type = 'String'
            value_x_value = random.choice(enum_set_split)
    else:
        min_value = resource_detail['minValue']
        max_value = resource_detail['maxValue']
        decimal_value = resource_detail['decimalValue']
        value_x_type = 'Quantity'
        value_x_value = {
            'value': round(random.uniform(min_value, max_value), decimal_value)
        }

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

    observation_resource = Observation(**observation_data).dict()
    return observation_resource
