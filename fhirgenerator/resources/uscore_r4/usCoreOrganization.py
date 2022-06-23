'''File for handling all operations relating to the US Core Location resource'''

from fhirgenerator.resources.r4.organization import generateOrganization
from fhir.resources.organization import Organization

def generateUSCoreOrganization() -> dict:
    '''Generate US Core Organization Resource'''

    organization_resource = generateOrganization()
    organization_resource['meta'] = {'profile': ['http://hl7.org/fhir/us/core/StructureDefinition/us-core-organization']}

    organization_resource = Organization(**organization_resource).dict()

    return organization_resource
