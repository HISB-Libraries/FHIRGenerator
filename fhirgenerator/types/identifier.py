'''File for handling all operations relating to the Identifer datatype'''

from faker import Faker


def generateMRNIdentifier() -> dict:
    '''Generate a Patient.identifier for a MRN'''
    fake = Faker()
    identifier_dict = {
        'system': 'urn:fhirgen:mrn',
        'type': {'coding': [
            {
                'system': 'http://terminology.hl7.org/CodeSystem/v2-0203',
                'code': 'MR'
            }
        ]},
        'value': fake.ssn()
    }
    return identifier_dict
