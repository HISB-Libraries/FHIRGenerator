'''Main entrypoint for package'''

from random import randint
from fhirgenerator.resources.patient import generatePatient
from fhirgenerator.resources.observation import generateObservation
from fhirgenerator.resources.condition import generateCondition
from fhirgenerator.resources.bundle import generateBundle


def generateResources(config_dict: dict, bundle_type: str = 'collection') -> dict:
    '''Main function for generating resources'''

    final_bundle_entries = []

    # Getting total numbers of each gender
    gender_totals = [round(value * config_dict['numberPatients'] * .01) for value in config_dict['genderMFOU']]
    if sum(gender_totals) > config_dict['numberPatients']:
        gender_totals[0] -= (sum(gender_totals) - config_dict['numberPatients'])
    elif sum(gender_totals) < config_dict['numberPatients']:
        gender_totals[2] += (config_dict['numberPatients'] - sum(gender_totals))

    gender_totals_list = []
    for i in range(0, gender_totals[0]):
        gender_totals_list.append('M')
    for i in range(0, gender_totals[1]):
        gender_totals_list.append('F')
    for i in range(0, gender_totals[2]):
        gender_totals_list.append('O')
    for i in range(0, gender_totals[3]):
        gender_totals_list.append('U')

    for j in range(0, config_dict['numberPatients']):

        patient_age = randint(config_dict['ageMin'], config_dict['ageMax'])
        patient_config = {
            "age": patient_age,
            "gender": gender_totals_list[j],
            "startDate": config_dict['startDate']
        }
        patient_resource = generatePatient(patient_config)
        final_bundle_entries.append(patient_resource)

        for resource_detail in config_dict['resourceDetails']:
            num_of_cycles = round(resource_detail['cycleLengthInDays'] / config_dict['days'])
            num_of_resources = randint(resource_detail['minOccurancesPerCycle'], resource_detail['maxOccurancesPerCycle']) * num_of_cycles
            bundle_entry_list = []
            resource_type = resource_detail['fhirResource']
            if resource_type == 'Observation':
                for k in range(0, num_of_resources):
                    bundle_entry_list.append(generateObservation(resource_detail, patient_resource['id'], config_dict['startDate'], config_dict['days']))
            if resource_type == 'Condition':
                for k in range(0, num_of_resources):
                    bundle_entry_list.append(generateCondition(resource_detail, patient_resource['id'], config_dict['startDate'], config_dict['days']))
            final_bundle_entries.extend(bundle_entry_list)

        print(f'Patient number {j+1} generated')

    final_bundle = generateBundle(final_bundle_entries, type=bundle_type)

    return final_bundle
