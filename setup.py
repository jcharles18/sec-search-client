# coding: utf-8

"""
    SEC Search API

    API for receiving classifications of SEC filings.  Note that this API is in  beta and is subject to change before the release of a stable v1.0.0.  By default, the api will return a maximum of 100 results.   To return more results, pass the `page` parameter.   For example, to return the second page of results, pass `page=2`.  <a href=\"https://www.secsearch.io/profile\" target=\"_blank\">Get an API Key</a>   # noqa: E501

    OpenAPI spec version: 0.1.2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from setuptools import setup, find_packages  # noqa: H301

NAME = "sec-search-client"
VERSION = "1.0.0"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = ["urllib3 >= 1.15", "six >= 1.10", "certifi", "python-dateutil"]

setup(
    name=NAME,
    version=VERSION,
    description="SEC Search API",
    author_email="",
    url="",
    keywords=["Swagger", "SEC Search API"],
    install_requires=REQUIRES,
    packages=find_packages(),
    include_package_data=True,
    long_description="""\
    API for receiving classifications of SEC filings.  Note that this API is in  beta and is subject to change before the release of a stable v1.0.0.  By default, the api will return a maximum of 100 results.   To return more results, pass the &#x60;page&#x60; parameter.   For example, to return the second page of results, pass &#x60;page&#x3D;2&#x60;.  &lt;a href&#x3D;\&quot;https://www.secsearch.io/profile\&quot; target&#x3D;\&quot;_blank\&quot;&gt;Get an API Key&lt;/a&gt;   # noqa: E501
    """
)
