'''File for handling all operations relating to the Condition resource'''

import uuid
import random
import datetime
from dateutil import parser
from fhir.resources.condition import Condition


def generateCondition(resource_detail: dict, patient_id: str, start_date: str, days: int) -> dict:
    '''Generate Condition Resource from resource detail from configuration'''

    condition_id = str(uuid.uuid4())

    condition_code = random.choice(resource_detail['codes'])

    start_date = parser.parse(start_date)
    random_number_of_days = random.randrange(days)
    random_date = start_date + datetime.timedelta(days=random_number_of_days)

    condition_data = {
        'id': condition_id,
        'code': {
            'coding': [
                condition_code
            ]
        },
        'subject': {
            'reference': f'Patient/{patient_id}'
        },
        'onsetDateTime': str(random_date)
    }

    condition_resource = Condition(**condition_data)
    return dict(condition_resource.dict())
