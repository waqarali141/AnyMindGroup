#!/usr/bin/env python
"""
Author: Waqar Ali
Email: Waqar.ali141@gmail.com
Dated: August 19, 2019

A Custom Exception to handle errors for twitter API
"""


class TwitterError(Exception):
    def __init__(self, message):
        super().__init__(message)
        self.message = message

