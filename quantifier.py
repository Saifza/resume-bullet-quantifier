import re

def has_numbers(text):
    return bool(re.search(r'\d', text))