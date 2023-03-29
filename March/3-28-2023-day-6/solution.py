import re


def alphanumeric(password):
    return bool(re.match(r"(?i)^[a-z\d]+$", password))
