import sys

if sys.version_info.major == 3 and sys.version_info.minor >= 10:
    import collections.abc as collections
else:
    import collections


def flatten(d, parent_key='', sep='.'):
    '''
    Flatten a nested python dictionary compressing the keys
    '''

    items = []

    for k, v in d.items():
        new_key = parent_key + sep + k if parent_key else k
        if isinstance(v, collections.MutableMapping):
            items.extend(flatten(v, new_key, sep=sep).items())
        else:
            items.append((new_key, v))

    return dict(items)


class FilterModule(object):
    '''
    custom jinja2 filters for working with collections
    '''

    def filters(self):
        return {
            'flatten_collection': flatten
        }
