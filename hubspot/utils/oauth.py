import urllib


def get_auth_url(client_id, redirect_uri, scopes: tuple, optional_scopes=()):
    return 'https://app.hubspot.com/oauth/authorize?' + urllib.parse.urlencode({
        'client_id': client_id,
        'redirect_uri': redirect_uri,
        'scope': ' '.join(scopes),
        'optional_scope': ' '.join(optional_scopes)
    }, quote_via=urllib.parse.quote)
