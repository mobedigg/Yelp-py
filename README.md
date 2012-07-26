Yelp-py
=======

Python wrapper for yelp api 2.0

Example:

    from yelp import Yelp

    consumer_key = 'CONSUMER_KEY'
    consumer_secret = 'CONSUMER_SECRET'
    token = 'TOKEN'
    token_secret = 'TOKEN_SECRET'

    ylp = Yelp(consumer_key, consumer_secret, token, token_secret)

    business = ylp.business('yelp-san-francisco')
    print business['name'] #u'Yelp'

    bars = ylp.search(term='bars', location='sf')

Based on [examples][1]


  [1]: https://github.com/Yelp/yelp-api/tree/master/v2/python