def parse_properties(properties):
    '''
    Parse the input string as a dict of k/v properties
    '''

    result = {}

    lines = properties.split('\n')
    for line in lines:
        if line.startswith('#') or not '=' in line:
            continue
        kv = line.split('=', 1)
        value = kv[1]
        if is_int(value):
            value = int(value)
        elif is_bool(value):
            value = bool(value)
        result.update({kv[0]: value})

    return result


def is_int(s):
    try:
        int(s)
        return True
    except ValueError:
        return False


def is_bool(s):
    return s.lower() == 'true' or s.lower() == 'false'


class FilterModule(object):
    '''
    custom jinja2 filters for working with strings
    '''

    def filters(self):
        return {
            'parse_properties': parse_properties
        }