# swagger_client.FilingApi

All URIs are relative to */v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_filing_text_filing_path_sequence_text_get**](FilingApi.md#get_filing_text_filing_path_sequence_text_get) | **GET** /filing/{path}/{sequence}/text | Get Filing Text
[**get_filings_by_symbol_filing_symbol_symbol_get**](FilingApi.md#get_filings_by_symbol_filing_symbol_symbol_get) | **GET** /filing/symbol/{symbol} | Get Filings By Symbol

# **get_filing_text_filing_path_sequence_text_get**
> object get_filing_text_filing_path_sequence_text_get(path, sequence)

Get Filing Text

Returns the text of a filing given its path and sequence number :return: text of filing

### Example

```python
from __future__ import print_function
import time
import sec_search_client
from sec_search_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKey
configuration = sec_search_client.Configuration()
configuration.api_key['X-API-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-API-Key'] = 'Bearer'

# create an instance of the API class
api_instance = sec_search_client.FilingApi(sec_search_client.ApiClient(configuration))
path = NULL  # object | 
sequence = NULL  # object | 

try:
    # Get Filing Text
    api_response = api_instance.get_filing_text_filing_path_sequence_text_get(path, sequence)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FilingApi->get_filing_text_filing_path_sequence_text_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | [**object**](.md)|  | 
 **sequence** | [**object**](.md)|  | 

### Return type

**object**

### Authorization

[APIKey](../README.md#APIKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_filings_by_symbol_filing_symbol_symbol_get**
> object get_filings_by_symbol_filing_symbol_symbol_get()

Get Filings By Symbol

Returns latest filings subject to the following constraints: - free account: returns 'must pay' message - paid account: all results over the last n days paginated by n items per page :return:

### Example

```python
from __future__ import print_function
import time
import sec_search_client
from sec_search_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKey
configuration = sec_search_client.Configuration()
configuration.api_key['X-API-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-API-Key'] = 'Bearer'

# create an instance of the API class
api_instance = sec_search_client.FilingApi(sec_search_client.ApiClient(configuration))

try:
    # Get Filings By Symbol
    api_response = api_instance.get_filings_by_symbol_filing_symbol_symbol_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FilingApi->get_filings_by_symbol_filing_symbol_symbol_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**object**

### Authorization

[APIKey](../README.md#APIKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

