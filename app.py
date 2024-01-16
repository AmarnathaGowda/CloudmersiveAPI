from __future__ import print_function
from cloudmersive_nlp_api_client.rest import ApiException
import cloudmersive_nlp_api_client
from pprint import pprint
import time
import os
from dotenv import load_dotenv
load_dotenv()

print(os.getenv('API_key'))

import cloudmersive_validate_api_client
from cloudmersive_validate_api_client.rest import ApiException

# create an instance of the API class
api_instance = cloudmersive_validate_api_client.DomainApi()
domain = 'cloudmersive.com' # str | Domain name to check, for example \"cloudmersive.com\".  The input is a string so be sure to enclose it in double-quotes.

# Configure API key authorization: Apikey

api_instance.api_client.configuration.api_key = {}
api_instance.api_client.configuration.api_key['Apikey'] = os.getenv('API_key')

try:
    # Validate a domain name
    api_response = api_instance.domain_check(domain)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DomainApi->domain_check: %s\n" % e)


# #configuration the API key for autorization
# configuration = cloudmersive_nlp_api_client.Configuration()
# configuration.api_key['ApiKey'] = os.getenv('API_key')

configuration = cloudmersive_nlp_api_client.ExtractEntitiesApi()

# # os.getenv('API_KEY')

# Creating an instance of the analyticsAPI class for sentiment analysis
# api_instance = cloudmersive_nlp_api_client.AnalyticsApi(
#     cloudmersive_nlp_api_client.ApiClient(configuration))

configuration.api_client.configuration.api_key = {}
configuration.api_client.configuration.api_key['Apikey'] = os.getenv('API_key')

value = 'Cloudmersive is a leader in Highly Scalable Cloud APIs.' # str | Input string

# Creating a sentiment analysis request object
# input = cloudmersive_nlp_api_client.SentimentAnalysisRequest(
#     'ITs the tutorials of clalling the API')

try:
    # Making a request to the API to perform sentiement analysinf on the sentiment
    api_response = configuration.extract_entities_post(value)
    pprint(api_response)
except ApiException as e:
    print('Exception when calling AnalysticsApi -> analytics_sentment:%s\n'% e)

