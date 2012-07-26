import json
import oauth2
import urllib
import urllib2


__all__ = ['Yelp']

class Yelp():

    def __init__(self, consumer_key, consumer_secret, token, token_secret):
        self.host = 'api.yelp.com/v2/'
        self.consumer_key = consumer_key
        self.consumer_secret = consumer_secret
        self.token = token
        self.token_secret = token_secret

    def _request(self, path, url_params=None):
        """Returns response for API request."""
        # Unsigned URL
        encoded_params = ''
        if url_params:
            encoded_params = urllib.urlencode(url_params)
        url = 'http://{host}{path}?{params}'.format(host=self.host, path=path, params=encoded_params)

        # Sign the URL
        consumer = oauth2.Consumer(self.consumer_key, self.consumer_secret)
        oauth_request = oauth2.Request('GET', url, {})
        oauth_request.update({'oauth_nonce': oauth2.generate_nonce(),
                            'oauth_timestamp': oauth2.generate_timestamp(),
                            'oauth_token': self.token,
                            'oauth_consumer_key': self.consumer_key})

        token = oauth2.Token(self.token, self.token_secret)
        oauth_request.sign_request(oauth2.SignatureMethod_HMAC_SHA1(), consumer, token)
        signed_url = oauth_request.to_url()

      # Connect
        try:
            conn = urllib2.urlopen(signed_url, None)
            try:
                response = json.loads(conn.read())
            finally:
                conn.close()
        except urllib2.HTTPError, error:
            response = json.loads(error.read())

        return response

    def business(self, bid, cc=None, lang=None):
        url_params = {}
        if cc:
            url_params['cc'] = cc
        if lang:
            url_params['lang'] = lang

        path = 'business/{bid}'.format(bid=bid)

        business = self._request(path, url_params)

        return business

    def search(self, term=None, location=None, bounds=None, point=None, current_location=None, offset=None, limit=None, cc=None, lang=None, cll=None, radius=None, category=None, deals=None, sort=None):

        assert location or bounds or point, 'location, bounds, or point required'
        
        path = 'search'
        url_params = {}
        
        if term:
            url_params['term'] = term
        if location:
            url_params['location'] = location
        if bounds:
            url_params['bounds'] = bounds
        if point:
            url_params['ll'] = point
        if offset:
            url_params['offset'] = offset
        if limit:
            url_params['limit'] = limit
        if cc:
            url_params['cc'] = cc
        if lang:
            url_params['lang'] = lang
        if current_location:
            url_params['cll'] = current_location
        if radius:
            url_params['radius_filter'] = radius
        if category:
            url_params['category_filter'] = category
        if deals:
            url_params['deals_filter'] = deals
        if sort:
            url_params['sort'] = sort        
        
        result = self._request(path, url_params)

        return result