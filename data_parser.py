#!/usr/bin/env python
"""
Author: Waqar Ali
Email: Waqar.ali141@gmail.com
Dated: August 20, 2019

A Data-Pipeline to convert the responses from twitter API to a custom JSON Format
"""

from collections import OrderedDict

from dateutil.parser import *


class Parser:
    """
    A date Parser Class to convert the Twitter Response to the Desired Response.
    """

    def __init__(self):
        pass

    @staticmethod
    def extract_account_info(tweet):
        """
        Parse User Information from Twitter API response

        Parameters:
        tweet (dict): A dictionary containing information about the user

        Returns:
        Ordered Dict: Desired Ordered dictionary for the user information
        """
        account_info = OrderedDict([
            ('fullname', tweet.get('user', {}).get('name')),
            ('href', "/{}".format(tweet.get('user', {}).get('screen_name'))),
            ('id', tweet.get('user', {}).get('id_str')),

        ])
        return account_info

    @staticmethod
    def parse_date(date):
        """
        Parse String formatted to the desired format.

        Parameters:
        date (str): A string formatted date from twitter

        Returns:
        str: A string formatted date of the desired format
        """
        if date:
            date = parse(date)
            try:
                return date.strftime('%-I:%M %p - %e %b %Y')
            except ValueError:
                return date.strftime('%#I:%M %p - %e %b %Y')
        else:
            return ''

    @staticmethod
    def parse_tweets_result(tweets, data_type):
        """
        Convert Twitters API Json response to required json response

        Parameters:
        tweets (json): A json response from the twitter.
        data_type (str): Identifying the data that tweets contain.

        Returns:
        json: A desired json formatted Twitter API response
        """
        if data_type == 'search':
            tweets = tweets.get('statuses', [])

        results = list()
        for tweet in tweets:
            hashtags = ["#{}".format(entity.get('text', '')) for entity in tweet.get('entities', {}).get('hashtags', [])]

            tweet_info = OrderedDict([
                ('account', Parser.extract_account_info(tweet)),
                ('date', Parser.parse_date(tweet.get('created_at'))),
                ('hashtags', hashtags),
                ('likes', tweet.get('favorite_count', 0)),
                ('replies', tweet.get('in_reply_to_status_id_str', 0)),
                ('retweets', tweet.get('retweet_count', 0)),
                ('text', tweet.get('text')),

            ])
            results.append(tweet_info)
        return results



x = Parser()
print (x.parse_date('Sat May 04 15:00:33 +0000 2019'))