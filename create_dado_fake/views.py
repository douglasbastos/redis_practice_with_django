# coding: utf-8
import string
from random import choice
from model_mommy import generators


def generator_range_string_lowercase(type_string='letters', min=6, max=12):
    max_length = choice(range(min, max+1))
    if type_string == 'lowercase':
        return str(''.join(choice(string.ascii_lowercase) for i in range(max_length)))
    elif type_string == 'uppercase':
        return str(''.join(choice(string.ascii_uppercase) for i in range(max_length)))
    else:
        return str(''.join(choice(string.ascii_letters) for i in range(max_length)))
