#!/usr/bin/env python
"""
Author: Waqar Ali
Email: Waqar.ali141@gmail.com
Dated: August 20, 2019

Flask API EndPoints Bound with Swagger.yml file
"""

from data_parser import Parser
from twitterSDK import TwitterError, TwitterAPI


# Add your credentials from twitter developer account to make API calls to Twitter API
CONSUMER_KEY = "Your's App Consumer Key"
CONSUMER_SECRET = "Your's App Consumer Secret"


def search_tweets(hashtag, limit=30):
    """
    Get tweets by a hashtag. Get the list of tweets with the given hashtag.
    Optional parameters:
        limit: integer, specifies the number of tweets to retrieve, the default should be 30
    """

    # Return if Limit is Not in the range of 0 to 200
    if limit > 200 or limit < 0:
        return {"Message": "Please Provide a valid limit between 0-200"}, 422

    # Initiate the TwitterAPI instance with the given Credentials
    try:
        api = TwitterAPI(consumer_key=CONSUMER_KEY,
                         consumer_secret=CONSUMER_SECRET)
    except TwitterError as e:
        # Return with 401 if can't authenticate the user with given credentials
        return {"Message": e.message}, 401

    # Query Param for twitter API
    query = {
        'q': '#{}'.format(hashtag),
        'count': limit
    }
    try:
        x = api.GetSearch(query)
    except TwitterError as e:
        return {"Message": e.message}, 400

    return Parser.parse_tweets_result(x, 'search'), 200


def user_tweets(username, limit=30):
    """
    Get user tweets. Get the list of tweets that the user has on his feed in JSON format.
    Optional parameters:
        limit: integer, specifies the number of tweets to retrieve, the default should be 30

    """

    # Return if Limit is Not in the range of 0 to 200
    if limit > 200 or limit < 0:
        return {"Message": "Please Provide a valid limit between 0-200"}, 422

    # Initiate the TwitterAPI instance with the given Credentials
    try:
        api = TwitterAPI(consumer_key=CONSUMER_KEY,
                         consumer_secret=CONSUMER_SECRET)
    except TwitterError as e:
        # Return with 401 if can't authenticate the user with given credentials
        return {"Message": e.message}, 401

    # Query Param for twitter API
    query = {
        'screen_name': username,
        'count': limit
    }
    try:
        x = api.GetTweets(query)
    except TwitterError as e:
        return {"Message": e.message}, 400

    return Parser.parse_tweets_result(x, 'user'), 200
