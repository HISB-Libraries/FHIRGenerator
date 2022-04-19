'''Main entrypoint for package'''

from random import randint
from fhirgenerator.resources import patient


def generateResources(config_dict: dict) -> dict:
    '''Main function for generating resources'''

    print(f'Using the following configuration for running this script... {config_dict}')

    final_bundle_entries = []

    # Getting total numbers of each gender
    gender_totals = round(config_dict['genderMFOU'] * .01 * config_dict['numberPatients'])
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

    for i in range(0, config_dict['numberPatients']):
        patient_age = randint(config_dict['ageMin'], config_dict['ageMax'])
        patient_config = {
            "age": patient_age,
            "gender": gender_totals_list[i],
            "startDate": config_dict['startDate']
        }
        patient_resource = patient.generatePatient(patient_config)
        final_bundle_entries.extend([patient_resource])

    return final_bundle_entries
