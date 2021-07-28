import re


def is_ok():
    print(bool(re.match('^[1234]+$', '')))
    print(bool(re.match('none', 'none')))

a = is_ok()