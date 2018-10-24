def filter_list(list, cond=None):
    '''
    Filter the input list by condition
    '''

    return filter(cond, list)


class FilterModule(object):
    '''
    custom jinja2 filters for working with lists
    '''

    def filters(self):
        return {
            'filter': filter_list
        }