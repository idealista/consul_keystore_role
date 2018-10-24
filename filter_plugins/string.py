def parse_properties(properties):
    '''
    Parse the input string as a dict of k/v properties
    '''

    result = {}

    lines = properties.split('\n')
    for line in lines:
        if line.startswith('#'):
            continue
        kv = line.split('=', 1)
        result.update({kv[0]: kv[1]})

    return result


class FilterModule(object):
    '''
    custom jinja2 filters for working with strings
    '''

    def filters(self):
        return {
            'parse_properties': parse_properties
        }