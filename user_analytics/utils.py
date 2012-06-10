
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

    result['ANALYTICS_IS_SECURE'] = request.is_secure()

    return result
