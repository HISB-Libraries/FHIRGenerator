'''Testing Location generator'''

import orjson
from fhirgenerator.resources.r4.organization import generateOrganization
from fhirgenerator.helpers.helpers import default
from fhir.resources.address import Address
from fhir.resources.contactpoint import ContactPoint


def testOrganizationGenerator():
    '''Test function for Location Generator'''

    with open('fhirgenerator/tests/input/config.json', 'rb') as infile:
        config_dict = orjson.loads(infile.read())

    organization_resource_details = []
    for detail in config_dict['resourceDetails']:
        if detail['fhirResource'] == 'USCoreOrganization':
            organization_resource_details.append(detail)

    for i, detail in enumerate(organization_resource_details):

        created_resource = generateOrganization()

        assert created_resource['resourceType'] == 'Organization'

        assert isinstance(Address(**created_resource['address'][0]), Address)
        assert isinstance(ContactPoint(**created_resource['telecom'][0]), ContactPoint)

        with open(f'fhirgenerator/tests/output/test_organization_{i}.json', 'wb') as outfile:
            outfile.write(orjson.dumps(created_resource, default=default, option=orjson.OPT_NAIVE_UTC))
