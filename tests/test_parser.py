#!/usr/bin/env python
"""
Author: Waqar Ali
Email: Waqar.ali141@gmail.com
Dated: August 21, 2019
"""
import json
import unittest

from ddt import ddt, data, unpack

from data_parser import Parser


@ddt
class ParserTest(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(ParserTest, self).__init__(*args, **kwargs)
        self.parser = Parser()

    @data(('Sat May 04 15:00:33 +0000 2019', '3:00 PM -  4 May 2019'), ('', ''))
    @unpack
    def test_parse_date(self, input_date, formatted_date):
        self.assertEqual(self.parser.parse_date(input_date), formatted_date)

    def test_tweet_result(self):
        with open('testdata/search.json', encoding='utf-8') as f:
            tweet_data = json.load(f)
        with open('testdata/user_tweet.json', encoding='utf-8') as f:
            user_data = json.load(f)

        tweet_outcome = self.parser.parse_tweets_result(tweet_data, 'search')
        user_outcome = self.parser.parse_tweets_result(user_data, 'user')

        self.assertEqual(tweet_outcome[0]['account']['fullname'], 'Twitter Dev')
        self.assertEqual(tweet_outcome[1]['likes'], 27)

        self.assertEqual(user_outcome[0]['retweets'], 284)
        self.assertEqual(user_outcome[1]['hashtags'], [])
