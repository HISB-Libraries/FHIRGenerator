'''File for handling all operations relating to the Observation resource'''

import uuid
import random
from fhir.resources.observation import Observation, ObservationComponent
from fhir.resources.quantity import Quantity

from fhirgenerator.helpers.helpers import makeRandomDate


def generateObservation(resource_detail: dict, patient_id: str, start_date: str, days: int) -> dict:
    '''Generate Observation Resource from resource detail from configuration'''

    observation_id = str(uuid.uuid4())

    observation_code = random.choice(resource_detail['codes'])

    random_date = makeRandomDate(start_date, days)

    value_x_type, value_x_value = handleValueTypes(resource_detail)

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

    if 'profile' in resource_detail:
        observation_data['meta'] = {}
        observation_data['meta']['profile'] = resource_detail['profile']

    if 'components' in resource_detail:
        observation_data['component'] = []
        for component_details in resource_detail['components']:
            observation_data['component'].append(generateObservationComponent(component_details))

    observation_resource = Observation(**observation_data).dict()
    return observation_resource


def generateObservationComponent(component_detail):
    '''Generate a component for an Observation'''
    component_code = random.choice(component_detail['codes'])

    value_x_type, value_x_value = handleValueTypes(component_detail)

    component_data = {
        'code': {
            'coding': [
                component_code
            ]
        },
        f'value{value_x_type}': value_x_value
    }

    component = ObservationComponent(**component_data).dict()
    return component


def handleValueTypes(detail, decimal_value=None):
    '''Determine value[x] type for resource generation'''
    if 'enumSetList' in detail:
        enum_set_list = detail['enumSetList']

        if 'value' in enum_set_list[0]:
            value_x_type = 'Quantity'
            value_x_value = random.choice(enum_set_list)
        elif 'coding' in enum_set_list[0]:
            value_x_type = 'CodeableConcept'
            value_x_value = random.choice(enum_set_list)
        elif enum_set_list[0].isnumeric():
            value_x_type = 'Integer'
            value_x_value = random.choice(enum_set_list)
        elif len(enum_set_list[0].split(':')) > 1:
            value_x_type = 'Ratio'
            value_x_titer_choice = random.choice(enum_set_list)
            value_x_titer_choice_split = value_x_titer_choice.split(':')
            value_x_value = {
                'numerator': {'value': value_x_titer_choice_split[0]},
                'denominator': {'value': value_x_titer_choice_split[1]}
            }

        else:
            value_x_type = 'String'
            value_x_value = random.choice(enum_set_list)
    elif 'minValue' in detail and 'maxValue' in detail:
        # Quantity or Integer Value
        min_value = detail['minValue']
        max_value = detail['maxValue']
        if 'decimalValue' in detail:
            decimal_value = detail['decimalValue']

        if 'unit' in detail:
            value_x_type, value_x_value = createValueQuantity(min_value, max_value, detail['unit'], decimal_value)
        else:
            if decimal_value is not None:
                value_x_type, value_x_value = createValueQuantity(min_value, max_value, None, decimal_value)
            else:
                value_x_type, value_x_value = createValueInteger(min_value, max_value)
    else:
        print("Warning: There was no enumSetList or (minValue and maxValue) in your configuration for this Observation. This Observation will not have a value[x].")
        value_x_type = 'None'
        value_x_value = ''

    return value_x_type, value_x_value


def createValueInteger(min_value, max_value):
    '''Generate a valueInteger'''
    type_string = "Integer"
    value = int(round(random.uniform(min_value, max_value)))
    return type_string, value


def createValueQuantity(min_value, max_value, unit_coding=None, decimal=None):
    '''Generate a valueQuantity'''
    type_string = "Quantity"

    value = random.uniform(min_value, max_value)
    if decimal is not None:
        value = round(value, decimal)
    else:
        value = int(value)

    if unit_coding is not None:
        system, code, display = unit_coding.split('^')
        quantity_data = {
            'value': value,
            'unit': display,
            'system': system,
            'code': code
        }
    else:
        quantity_data = {
            'value': value
        }

    quantity = Quantity(**quantity_data).dict()
    return type_string, quantity
