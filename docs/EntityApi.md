# swagger_client.EntityApi

All URIs are relative to */v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**company_names_entitycompanies_all_get**](EntityApi.md#company_names_entitycompanies_all_get) | **GET** /entitycompanies/all | Company Names
[**get_filings_by_cik_entity_cik_cik_get**](EntityApi.md#get_filings_by_cik_entity_cik_cik_get) | **GET** /entity/cik/{cik} | Get Filings By Cik
[**search_entities_entity_search_get**](EntityApi.md#search_entities_entity_search_get) | **GET** /entity/search/ | Search Entities

# **company_names_entitycompanies_all_get**
> object company_names_entitycompanies_all_get()

Company Names

Returns all company names :return:

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
api_instance = sec_search_client.EntityApi(sec_search_client.ApiClient(configuration))

try:
    # Company Names
    api_response = api_instance.company_names_entitycompanies_all_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EntityApi->company_names_entitycompanies_all_get: %s\n" % e)
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

# **get_filings_by_cik_entity_cik_cik_get**
> object get_filings_by_cik_entity_cik_cik_get()

Get Filings By Cik

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
api_instance = sec_search_client.EntityApi(sec_search_client.ApiClient(configuration))

try:
    # Get Filings By Cik
    api_response = api_instance.get_filings_by_cik_entity_cik_cik_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EntityApi->get_filings_by_cik_entity_cik_cik_get: %s\n" % e)
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

# **search_entities_entity_search_get**
> object search_entities_entity_search_get(query)

Search Entities

Search all company_name or symbol :return:

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
api_instance = sec_search_client.EntityApi(sec_search_client.ApiClient(configuration))
query = NULL  # object | 

try:
    # Search Entities
    api_response = api_instance.search_entities_entity_search_get(query)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EntityApi->search_entities_entity_search_get: %s\n" % e)
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

