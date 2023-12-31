# coding: utf-8

"""
    SEC Search API

    API for receiving classifications of SEC filings.  Note that this API is in  beta and is subject to change before the release of a stable v1.0.0.  By default, the api will return a maximum of 100 results.   To return more results, pass the `page` parameter.   For example, to return the second page of results, pass `page=2`.  <a href=\"https://www.secsearch.io/profile\" target=\"_blank\">Get an API Key</a>   # noqa: E501

    OpenAPI spec version: 0.1.2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import sec_search_client
from sec_search_client.models.validation_error import ValidationError  # noqa: E501
from sec_search_client.rest import ApiException


class TestValidationError(unittest.TestCase):
    """ValidationError unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testValidationError(self):
        """Test ValidationError"""
        # FIXME: construct object with mandatory attributes with example values
        # model = sec_search_client.models.validation_error.ValidationError()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()