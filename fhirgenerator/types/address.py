'''File for handling all operations relating to the Address datatype'''

from faker import Faker


def generateAddress() -> dict:
    '''Function for generating a FHIR Address'''
    address_data = {
        'line': [generateLineAddress()],
        'city': generateCityAddress(),
        'state': generateStateAddress()
    }
    return address_data


def generateLineAddress():
    '''Function for generating a line in a FHIR Address'''
    fake = Faker()
    return fake.street_address()


def generateCityAddress():
    '''Function for generating a city in a FHIR Address'''
    fake = Faker()
    return fake.city()


def generateStateAddress():
    '''Function for generating a state in a FHIR Address'''
    fake = Faker()
    return fake.state()
