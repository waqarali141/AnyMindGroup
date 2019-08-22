#!/usr/bin/env python
"""
Author: Waqar Ali
Email: Waqar.ali141@gmail.com
Dated: August 21, 2019
"""

import unittest
from unittest.mock import patch

from ddt import ddt, data, unpack

from twitterSDK import TwitterError
from twitterwrapper import search_tweets, user_tweets


@ddt
class ParserTest(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(ParserTest, self).__init__(*args, **kwargs)

    @data(('test', 205, 422), ('test', 10, 200), ('test', -1, 422))
    @unpack
    def test_search_tweet_limit_parameter(self, hashtag, limit, response_code):
        self.assertEqual(search_tweets(hashtag, limit)[1], response_code)

    @data(('waqar', 205, 422), ('Albino', 10, 200), ('Tester1', -1, 422))
    @unpack
    def test_user_tweet_limit_parameter(self, username, limit, response_code):
        self.assertEqual(search_tweets(username, limit)[1], response_code)

    @patch('twitterwrapper.TwitterAPI')
    def test_search_tweet_api_credentials(self, api):
        api.side_effect = TwitterError('Missing Authentication Credentials.')
        response, response_code = search_tweets('test', 2)
        self.assertEqual(response_code, 401)
        self.assertEqual(response['Message'], 'Missing Authentication Credentials.')

    @patch('twitterwrapper.TwitterAPI')
    def test_user_tweet_api_credentials(self, api):
        api.side_effect = TwitterError('Missing Authentication Credentials.')
        response, response_code = user_tweets('DummyUser', 5)
        self.assertEqual(response_code, 401)
        self.assertEqual(response['Message'], 'Missing Authentication Credentials.')

    @patch('twitterwrapper.TwitterAPI.GetSearch')
    @patch('twitterwrapper.Parser.parse_tweets_result', )
    def test_search_tweet_response(self, response, parser):
        response.return_value = []
        parser.return_value = []
        response, response_code = search_tweets('Dummy', 1)
        self.assertEqual(response, [])
        self.assertEqual(response_code, 200)

    @patch('twitterwrapper.TwitterAPI.GetTweets')
    @patch('twitterwrapper.Parser.parse_tweets_result', )
    def test_user_tweet_response(self, response, parser):
        response.return_value = []
        parser.return_value = []
        response, response_code = user_tweets('Dummy', 1)
        self.assertEqual(response, [])
        self.assertEqual(response_code, 200)

    @patch('twitterwrapper.TwitterAPI.GetSearch')
    def test_search_tweet_bad_request(self, response):
        response.side_effect = TwitterError('Bad Parameters')
        response, response_code = search_tweets('Dummy', 1)
        self.assertEqual(response['Message'], 'Bad Parameters')
        self.assertEqual(response_code, 400)

    @patch('twitterwrapper.TwitterAPI.GetTweets')
    def test_user_tweet_bad_request(self, response):
        response.side_effect = TwitterError('Bad Parameters')
        response, response_code = user_tweets('DummyUser', 1)
        self.assertEqual(response['Message'], 'Bad Parameters')
        self.assertEqual(response_code, 400)
