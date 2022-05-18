'''File for handling all operations relating to the Location resource'''

from faker import Faker
from fhir.resources.location import Location
from fhirgenerator.types.address import generateAddress

from fhirgenerator.types.contactPoint import generateContactPoint


def generateLocation() -> dict:
    '''Generate a Location resource'''

    fake = Faker()

    location_dict = {
        'name': fake.company(),
        'status': 'active',
        'telecom': generateContactPoint(),
        'address': generateAddress(use='work')
    }

    location = Location(**location_dict)

    return dict(location.dict())
