
#HTTP_KEYS in this array are pickable
HTTP_KEYS_TO_PRESERVE = [
    'HTTP_X_FORWARDED_FOR',
    'HTTP_CLIENT_IP',
    'HTTP_X_FORWARDED',
    'HTTP_X_CLUSTER_CLIENT_IP',
    'HTTP_FORWARDED_FOR',
    'HTTP_FORWARDED',

    'HTTP_REFERER',
    'REQUEST_METHOD',
    'QUERY_STRING',
    'HTTP_HOST',
    'PATH_INFO',
    'HTTP_USER_AGENT',
    'HTTP_ACCEPT_LANGUAGE',
    'REMOTE_ADDR',
    'REMOTE_HOST',
    'REMOTE_USER',
    ]

def massage_request(request):
    '''
    Grabs whatever it needs from the request object and makes sure it is
    serializable (pickable) so that it can be processed later
    '''

    request_meta = request.META

    result = {}

    for key in HTTP_KEYS_TO_PRESERVE:
        if request_meta.has_key(key):
            result[key] = request_meta[key]

    print request.raw_post_data

    result['ANALYTICS_IS_SECURE'] = request.is_secure()


class TwoWayDic(dict):
    '''
    Very basic TwoWayDic. Only valid during construction

    Usage:

    x = TwoWayDic({'A' : 2, 'B' : 3, 'C': 4})
    print x.A
    > 2
    print x.reverse[3]
    > 'B'
    print x['C']
    > 4
    '''
    reverse = None

    def __getattr__(self, name):
        '''Allows calling TwoWayDic.key'''
        if name in self:
            return self[name]
        raise AttributeError

    def __init__(self, data):
        self.reverse = dict(reversed(item) for item in data.items())
        super(TwoWayDic, self).__init__(data)