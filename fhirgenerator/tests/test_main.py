'''Testing Main function'''

import orjson
from fhirgenerator.main import generateResources
from fhirgenerator.helpers.helpers import default


def testMain():
    '''Testing function for main.py'''

    with open('fhirgenerator/tests/input/config.json', 'rb') as infile:
        config_dict = orjson.loads(infile.read())

    output_collection_bundle = generateResources(config_dict=config_dict, bundle_type='collection')
    output_trans_bundle = generateResources(config_dict=config_dict, bundle_type='transaction')

    with open('fhirgenerator/tests/output/test_main_transaction.json', 'wb') as outfile:
        outfile.write(orjson.dumps(output_trans_bundle, default=default, option=orjson.OPT_NAIVE_UTC))
    with open('fhirgenerator/tests/output/test_main_collection.json', 'wb') as outfile:
        outfile.write(orjson.dumps(output_collection_bundle, default=default, option=orjson.OPT_NAIVE_UTC))

    patient_list_collection = list(filter(lambda entry: entry['resource']['resourceType'] == 'Patient', output_collection_bundle['entry']))
    patient_list_transaction = list(filter(lambda entry: entry['resource']['resourceType'] == 'Patient', output_trans_bundle['entry']))

    assert len(patient_list_collection) == config_dict['numberPatients']
    assert len(patient_list_transaction) == config_dict['numberPatients']
