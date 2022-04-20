'''Helper functions file'''

from datetime import date, datetime
from dateutil import parser
import decimal


def calculateAge(birthDate: datetime, start: str = str(date.today())) -> int:
    '''Calculate Age from birth date'''
    today = parser.parse(start)
    age = today.year - birthDate.year - ((today.month, today.day) < (birthDate.month, birthDate.day))
    return age


def default(obj):
    '''Callable function for JSON serialization of Decimal types'''
    if isinstance(obj, decimal.Decimal):
        return float(str(obj))
    raise TypeError
