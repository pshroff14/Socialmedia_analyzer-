import tweepy
import unittest
from Analyzer import *


class TestTwit(unittest.TestCase):

    def testoauth(self):
        auth = OAuthHandler(oauth_consumer_key, oauth_consumer_secret)

        # test getting access token
        auth_url = auth.get_authorization_url()
        print('Please authorize: ' + auth_url)
        verifier = input('PIN: ').strip()
        self.assertTrue(len(verifier) > 0)
        access_token = auth.get_access_token(verifier)
        self.assertTrue(access_token is not None)

    def testaccesstype(self):
        auth = OAuthHandler(oauth_consumer_key, oauth_consumer_secret)
        auth_url = auth.get_authorization_url(access_type='read')
        print('Please open: ' + auth_url)
        answer = input('Did Twitter only request read permissions? (y/n) ')
        self.assertEqual('y', answer.lower())

        # build api object test using oauth
        api = API(auth)
        s = api.update_status('test %i' % random.randint(0, 1000))
        api.destroy_status(s.id)

    def test_add(self):
        self.assertEqual(add_num(5),6)

    # def test_auth(self):
    #     self.assertEqual()

    def test_error(self):
        import pickle
        from tweepy.error import TweepError

        e = TweepError('no reason', {'status': 200})
        e2 = pickle.loads(pickle.dumps(e))

        self.assertEqual(e.reason, e2.reason)
        self.assertEqual(e.response, e2.response)


# This test see's if the list of strings of the GettrendsWoeid is the same as the function itself
    def test_woe(self):
        woeid = 23637105    # Enter WOEID number
        a = trend_location(woeid)
        b = api.GetTrendsWoeid(woeid, exclude=None)
        self.assertListEqual(a, b)






if __name__ == '__main__':
    unittest.main()


