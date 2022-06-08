'''File for handling all operations relating to the US Core Location resource'''

from fhirgenerator.resources.r4.location import generateLocation
from fhir.resources.location import Location

def generateUSCoreLocation(config: dict) -> dict:
    '''Generate US Core Location Resource'''

    location_resource = generateLocation()
    location_resource['meta'] = {'profile': ['http://hl7.org/fhir/us/core/StructureDefinition/us-core-location']}

    location_resource = Location(**location_resource).dict()

    return location_resource
