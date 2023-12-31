# swagger_client.ClassificationApi

All URIs are relative to */v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**all_classifications_classification_all_get**](ClassificationApi.md#all_classifications_classification_all_get) | **GET** /classification/all | All Classifications
[**classification_search_classification_search_get**](ClassificationApi.md#classification_search_classification_search_get) | **GET** /classification/search | Classification Search
[**get_classification_by_id_classification_by_name_classification_machine_name_get**](ClassificationApi.md#get_classification_by_id_classification_by_name_classification_machine_name_get) | **GET** /classification/by-name/{classification_machine_name} | Get Classification By Id
[**latest_classifications_classification_latest_get**](ClassificationApi.md#latest_classifications_classification_latest_get) | **GET** /classification/latest | Latest Classifications

# **all_classifications_classification_all_get**
> object all_classifications_classification_all_get()

All Classifications

Returns all classifications :return:

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
api_instance = sec_search_client.ClassificationApi(sec_search_client.ApiClient(configuration))

try:
    # All Classifications
    api_response = api_instance.all_classifications_classification_all_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClassificationApi->all_classifications_classification_all_get: %s\n" % e)
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

# **classification_search_classification_search_get**
> object classification_search_classification_search_get(classification_machine_name=classification_machine_name, start_date=start_date, end_date=end_date, confidence=confidence, symbol=symbol, cik=cik, form_type=form_type, page=page, per_page=per_page)

Classification Search

Returns latest classifications subject to the following constraints: - free account: top 10 - paid account: all results over the last n days paginated by n items per page (max of 100 items per page) :return:

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
api_instance = sec_search_client.ClassificationApi(sec_search_client.ApiClient(configuration))
classification_machine_name = NULL  # object |  (optional)
start_date = 2023 - 12 - 01  # object |  (optional) (default to 2023-12-01)
end_date = 2023 - 12 - 31  # object |  (optional) (default to 2023-12-31)
confidence = 90  # object |  (optional) (default to 90)
symbol = NULL  # object |  (optional)
cik = NULL  # object |  (optional)
form_type = NULL  # object |  (optional)
page = 1  # object |  (optional) (default to 1)
per_page = 100  # object |  (optional) (default to 100)

try:
    # Classification Search
    api_response = api_instance.classification_search_classification_search_get(
        classification_machine_name=classification_machine_name, start_date=start_date, end_date=end_date,
        confidence=confidence, symbol=symbol, cik=cik, form_type=form_type, page=page, per_page=per_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClassificationApi->classification_search_classification_search_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **classification_machine_name** | [**object**](.md)|  | [optional] 
 **start_date** | [**object**](.md)|  | [optional] [default to 2023-12-01]
 **end_date** | [**object**](.md)|  | [optional] [default to 2023-12-31]
 **confidence** | [**object**](.md)|  | [optional] [default to 90]
 **symbol** | [**object**](.md)|  | [optional] 
 **cik** | [**object**](.md)|  | [optional] 
 **form_type** | [**object**](.md)|  | [optional] 
 **page** | [**object**](.md)|  | [optional] [default to 1]
 **per_page** | [**object**](.md)|  | [optional] [default to 100]

### Return type

**object**

### Authorization

[APIKey](../README.md#APIKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_classification_by_id_classification_by_name_classification_machine_name_get**
> object get_classification_by_id_classification_by_name_classification_machine_name_get(classification_machine_name, days=days, page=page, per_page=per_page)

Get Classification By Id

Returns latest classifications subject to the following constraints: - free account: top 10 - paid account: all results over the last n days paginated by n items per page :return:

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
api_instance = sec_search_client.ClassificationApi(sec_search_client.ApiClient(configuration))
classification_machine_name = NULL  # object | 
days = 30  # object |  (optional) (default to 30)
page = 1  # object |  (optional) (default to 1)
per_page = 100  # object |  (optional) (default to 100)

try:
    # Get Classification By Id
    api_response = api_instance.get_classification_by_id_classification_by_name_classification_machine_name_get(
        classification_machine_name, days=days, page=page, per_page=per_page)
    pprint(api_response)
except ApiException as e:
    print(
        "Exception when calling ClassificationApi->get_classification_by_id_classification_by_name_classification_machine_name_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **classification_machine_name** | [**object**](.md)|  | 
 **days** | [**object**](.md)|  | [optional] [default to 30]
 **page** | [**object**](.md)|  | [optional] [default to 1]
 **per_page** | [**object**](.md)|  | [optional] [default to 100]

### Return type

**object**

### Authorization

[APIKey](../README.md#APIKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **latest_classifications_classification_latest_get**
> object latest_classifications_classification_latest_get()

Latest Classifications

Returns latest classifications subject to the following constraints: - free account: top 10 - paid account: all results over the last 30 days paginated by n items per page :return:

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
api_instance = sec_search_client.ClassificationApi(sec_search_client.ApiClient(configuration))

try:
    # Latest Classifications
    api_response = api_instance.latest_classifications_classification_latest_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClassificationApi->latest_classifications_classification_latest_get: %s\n" % e)
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

