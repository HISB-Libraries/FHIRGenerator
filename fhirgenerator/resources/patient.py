'''File for handling all operations relating to the Patient resource'''

import uuid
import random
import datetime
from dateutil import parser
from fhir.resources.patient import Patient

from fhirgenerator.types.humanName import generateName
from fhirgenerator.types.address import generateAddress
from fhirgenerator.types.identifier import generateMRNIdentifier

gender_map = {
    'M': 'male',
    'F': 'female',
    'O': 'other',
    'U': 'unknown'
}


def generateBirthDateFromAge(age: int, startDate: str) -> str:
    '''Generate a random birthday that matches the given age'''
    start = parser.parse(startDate)
    random_number_of_days = random.randrange(365)
    birthdate = datetime.date(start.year - age - 1, start.month, start.day) + datetime.timedelta(days=random_number_of_days)
    return str(birthdate)


def generatePatient(configuration: dict) -> dict:
    '''Generate Patient Resource'''

    patient_id = str(uuid.uuid4())
    patient_data = {
        'id': patient_id,
        'identifier': [generateMRNIdentifier()],
        'name': [generateName(gender=configuration['gender'])],
        'address': [generateAddress()],
        'gender': gender_map[configuration['gender'].upper()],
        'birthDate': generateBirthDateFromAge(configuration['age'], configuration['startDate'])
    }
    patient_resource = Patient(**patient_data).dict()
    return patient_resource
