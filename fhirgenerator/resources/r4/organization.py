'''File for handling all operations relating to the Location resource'''

import uuid
from faker import Faker
from fhir.resources.organization import Organization
from fhirgenerator.types.address import generateAddress
from fhirgenerator.types.contactPoint import generateContactPoint


def generateOrganization() -> dict:
    '''Generate a Location resource'''

    fake = Faker()

    organization_id = str(uuid.uuid4())

    organization_dict = {
        'id': organization_id,
        'name': fake.company(),
        'active': True,
        'telecom': [generateContactPoint()],
        'address': [generateAddress(use='work')]
    }

    organization = Organization(**organization_dict)

    return dict(organization.dict())
