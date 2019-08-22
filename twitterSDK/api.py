#!/usr/bin/env python
"""
Author: Waqar Ali
Email: Waqar.ali141@gmail.com
Dated: August 19, 2019

A Wrapper Build Around the Twitter Developers API
"""

import base64

import requests

from .error import TwitterError


class TwitterAPI:
    """
    A python interface into Twitter API

    Currently have two EndPoints.
    1. Search tweets on keyWord
        Usage:
            api = TwitterAPI(consumer_key='YOUR CONSUMER KEY',
                     consumer_secret='YOUR CONSUMER SECRET')
            search_params = {
                'q': 'General Election',
                'result_type': 'recent',
                'count': 2
            }
            api.GetSearch(search_params)

    2. Return Tweets of a given User
        Usage:
           api = TwitterAPI(consumer_key='3GGDJGEAZkbMzBYKk9b4QimJrXX',
                 consumer_secret='hsSMtINA1HxJHyYJD15cYMPpP0cv6xy64bL829PZJ1WIb5b6UI')
            param = {'screen_name': 'Fiona81771350',
                     'count': 2}

            r = api.GetTweets(param)


    """

    # Twitter EndPoints URL's
    base_url = 'https://api.twitter.com/'
    auth_url = '{}oauth2/token'.format(base_url)
    search_url = '{}1.1/search/tweets.json'.format(base_url)
    tweets_url = '{}1.1/statuses/user_timeline.json'.format(base_url)

    def __init__(self,
                 consumer_key=None,
                 consumer_secret=None):
        """
        Instantiate a TwitterAPI Object and authenticate the user with the given Credentials.

        Parameters:
        consumer_key (str):Your Twitter user's consumer_key.
        consumer_secret (str):Your Twitter user's consumer_secret.

        Raises:
        Exception: If Credentials are missing or Can't Authenticate with the given Credentials
        """

        if not all([consumer_key, consumer_secret]):
            raise TwitterError('Missing Authentication Credentials.')

        access_token = TwitterAPI.get_access_token(consumer_key, consumer_secret)

        # Set the Authorization token in the Request session to be used for calling Twitters EndPoints
        self._session = requests.session()
        self._session.headers = {
            'Authorization': 'Bearer {}'.format(access_token)
        }

    @staticmethod
    def get_access_token(consumer_key, consumer_secret):
        """
        Authenticate the Credentials from Twitter and return the Access Token.

        Parameters:
        consumer_key (str):Your Twitter user's consumer_key.
        consumer_secret (str):Your Twitter user's consumer_secret.

        Raises:
        Exception: If Credentials are missing or invalid

        Returns:
        str: Access Token if user is authenticated Successfully.

        """
        if not all([consumer_key, consumer_secret]):
            raise TwitterError('Missing Authentication Credentials.')

        bearer_token = base64.b64encode('{}:{}'.format(consumer_key, consumer_secret).encode('utf8'))
        post_headers = {
            'Authorization': 'Basic {0}'.format(bearer_token.decode('utf8')),
            'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8'
        }

        res = requests.post(url='https://api.twitter.com/oauth2/token',
                            data={'grant_type': 'client_credentials'},
                            headers=post_headers)

        if res.status_code != 200:
            raise TwitterError(res.text)

        bearer_creds = res.json()
        return bearer_creds['access_token']

    def GetSearch(self, query):
        """
        Perform a Request to the Twitter Search Endpoints for the given query

        Parameters:
        query (dict):
            Query Arguments to be used
            query = {
                    'q': 'General Election',
                    'result_type': 'recent',
                    'count': 2
                    }
        Raises:
        Exception: If Can't perform Twitter request successfully

        Returns
        json: Json Response of searched results from the twitter.
        """
        response = self._session.get(self.search_url, params=query)

        if response.status_code != 200:
            raise TwitterError(response.text)

        return response.json()

    def GetTweets(self, query):
        """
        Perform a Request to the Twitter LookUp Endpoints for the given query

        Parameters:
        query (dict):
            Query Arguments to be used
            query = {
                    'screen_name': 'Fiona81771350',
                    'count': 2
                    }
        Raises:
        Exception: If Can't perform Twitter request successfully

        Returns
        json: Json Response of searched results from the twitter.
        """

        response = self._session.get(self.tweets_url, params=query)

        if response.status_code != 200:
            raise TwitterError(response.text)

        return response.json()
