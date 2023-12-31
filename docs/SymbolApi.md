# swagger_client.SymbolApi

All URIs are relative to */v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**all_symbols_symbol_all_get**](SymbolApi.md#all_symbols_symbol_all_get) | **GET** /symbol/all | All Symbols
[**search_symbols_symbol_search_get**](SymbolApi.md#search_symbols_symbol_search_get) | **GET** /symbol/search | Search Symbols

# **all_symbols_symbol_all_get**
> object all_symbols_symbol_all_get()

All Symbols

Returns all symbols :return:

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
api_instance = sec_search_client.SymbolApi(sec_search_client.ApiClient(configuration))

try:
    # All Symbols
    api_response = api_instance.all_symbols_symbol_all_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SymbolApi->all_symbols_symbol_all_get: %s\n" % e)
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

# **search_symbols_symbol_search_get**
> object search_symbols_symbol_search_get(query)

Search Symbols

Search all entites by cik, company_name or symbol :return:

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
api_instance = sec_search_client.SymbolApi(sec_search_client.ApiClient(configuration))
query = NULL  # object | 

try:
    # Search Symbols
    api_response = api_instance.search_symbols_symbol_search_get(query)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SymbolApi->search_symbols_symbol_search_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | [**object**](.md)|  | 

### Return type

**object**

### Authorization

[APIKey](../README.md#APIKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

