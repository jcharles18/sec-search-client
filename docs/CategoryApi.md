# swagger_client.CategoryApi

All URIs are relative to */v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**all_categories_category_all_get**](CategoryApi.md#all_categories_category_all_get) | **GET** /category/all | All Categories
[**get_category_by_id_category_by_id_category_id_get**](CategoryApi.md#get_category_by_id_category_by_id_category_id_get) | **GET** /category/by-id/{category_id} | Get Category By Id
[**latest_categories_category_latest_get**](CategoryApi.md#latest_categories_category_latest_get) | **GET** /category/latest | Latest Categories

# **all_categories_category_all_get**
> object all_categories_category_all_get()

All Categories

Returns all categories :return:

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
api_instance = sec_search_client.CategoryApi(sec_search_client.ApiClient(configuration))

try:
    # All Categories
    api_response = api_instance.all_categories_category_all_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CategoryApi->all_categories_category_all_get: %s\n" % e)
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

# **get_category_by_id_category_by_id_category_id_get**
> object get_category_by_id_category_by_id_category_id_get()

Get Category By Id

Returns latest categories subject to the following constraints: - free account: top 10 - paid account: all results over the last n days paginated by n items per page :return:

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
api_instance = sec_search_client.CategoryApi(sec_search_client.ApiClient(configuration))

try:
    # Get Category By Id
    api_response = api_instance.get_category_by_id_category_by_id_category_id_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CategoryApi->get_category_by_id_category_by_id_category_id_get: %s\n" % e)
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

# **latest_categories_category_latest_get**
> object latest_categories_category_latest_get()

Latest Categories

Returns latest categories subject to the following constraints: - free account: top 10 - paid account: all results over the last 30 days paginated by n items per page :return:

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
api_instance = sec_search_client.CategoryApi(sec_search_client.ApiClient(configuration))

try:
    # Latest Categories
    api_response = api_instance.latest_categories_category_latest_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CategoryApi->latest_categories_category_latest_get: %s\n" % e)
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

