from __future__ import print_function
import time
import cloudmersive_image_api_client
from cloudmersive_image_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Apikey
configuration = cloudmersive_image_api_client.Configuration()
configuration.api_key['Apikey'] = '7cb7be78-35a6-4a37-98b0-d93098d9ddbb'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Apikey'] = 'Bearer'

# create an instance of the API class
api_instance = cloudmersive_image_api_client.RecognizeApi(cloudmersive_image_api_client.ApiClient(configuration))
image_file = 'hamburguer.jpg' 
# file | Image file to perform the operation on.  Common file formats such as PNG, JPEG are supported.

try:
    # Describe an image in natural language
    api_response = api_instance.recognize_describe(image_file)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RecognizeApi->recognize_describe: %s\n" % e)