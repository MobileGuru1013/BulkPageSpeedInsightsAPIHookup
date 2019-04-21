class PageSpeedResponse():
    def __init__(self, response):
        response.raise_for_status()

        self._response = response
        self._request = response.url
        self.json = response.json()

    @property
    def url(self):
        return self.json.get('id')

    @property
    def title(self):
        return self.json.get('title')

    @property
    def response_code(self):
        return self.json.get('responseCode')

    @property
    def speed(self):
        return self.json.get('ruleGroups').get('SPEED').get('score')

    @property
    def css_response_bytes(self):
        return self.json.get('pageStats').get('cssResponseBytes')

    @property
    def html_response_bytes(self):
        return self.json.get('pageStats').get('htmlResponseBytes')

    @property
    def image_response_bytes(self):
        return self.json.get('pageStats').get('imageResponseBytes')

    @property
    def javascript_response_bytes(self):
        return self.json.get('pageStats').get('javascriptResponseBytes')

    @property
    def number_css_resources(self):
        return self.json.get('pageStats').get('numberCssResources')

    @property
    def number_hosts(self):
        return self.json.get('pageStats').get('numberHosts')

    @property
    def number_js_resources(self):
        return self.json.get('pageStats').get('numberJsResources')

    @property
    def number_resources(self):
        return self.json.get('pageStats').get('numberResources')

    @property
    def number_static_resources(self):
        return self.json.get('pageStats').get('numberStaticResources')

    @property
    def other_response_bytes(self):
        return self.json.get('pageStats').get('otherResponseBytes')

    @property
    def text_response_bytes(self):
        return self.json.get('pageStats').get('textResponseBytes')

    @property
    def total_request_bytes(self):
        return self.json.get('pageStats').get('totalRequestBytes')

    @property
    def total_roundtrips(self):
        return self.json.get('pageStats').get('numTotalRoundTrips')

    @property
    def total_render_blocking_roundtrips(self):
        return self.json.get('pageStats').get('numRenderBlockingRoundTrips')