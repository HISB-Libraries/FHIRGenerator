'''Testing Location generator'''

from genericpath import exists
import orjson
from fhirgenerator.resources.uscore_r4.usCoreOrganization import generateUSCoreOrganization
from fhirgenerator.helpers.helpers import default
from fhir.resources.address import Address
from fhir.resources.contactpoint import ContactPoint


def testUSCoreOrganizationGenerator():
    '''Test function for Location Generator'''

    with open('fhirgenerator/tests/input/config.json', 'rb') as infile:
        config_dict = orjson.loads(infile.read())

    organization_resource_details = []
    for detail in config_dict['resourceDetails']:
        if detail['fhirResource'] == 'Organization':
            organization_resource_details.append(detail)

    for i, detail in enumerate(organization_resource_details):

        created_resource = generateUSCoreOrganization()

        assert created_resource['resourceType'] == 'Organization'
        assert created_resource['meta']['profile'][0] == 'http://hl7.org/fhir/us/core/StructureDefinition/us-core-organization'
        assert 'active' in created_resource.keys()

        assert isinstance(Address(**created_resource['address'][0]), Address)
        assert isinstance(ContactPoint(**created_resource['telecom'][0]), ContactPoint)

        with open(f'fhirgenerator/tests/output/test_usCoreOrganization_{i}.json', 'wb') as outfile:
            outfile.write(orjson.dumps(created_resource, default=default, option=orjson.OPT_NAIVE_UTC))
