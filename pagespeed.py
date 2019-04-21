import requests
from responses import PageSpeedResponse


class PageSpeed(object):
    def __init__(self, api_key=None):
        self.api_key = api_key
        self.endpoint = 'https://www.googleapis.com/pagespeedonline/v4/runPagespeed'

    def fetch(self, url, **kwargs):
        kwargs.setdefault('filter_third_party_resources', False)
        kwargs.setdefault('screenshot', False)
        kwargs.setdefault('strategy', 'desktop')

        params = kwargs.copy()
        params.update({'url': url})

        response = requests.get(self.endpoint, params=params)

        if kwargs.get('strategy') == 'desktop':
            return PageSpeedResponse(response)
        elif kwargs.get('strategy') == 'mobile':
            return PageSpeedResponse(response)
        else:
            raise ValueError('Invalid Strategy: {0}'.format(kwargs.get('strategy')))