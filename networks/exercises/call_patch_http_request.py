import requests
from requests.exceptions import HTTPError
import json
from getpass import getpass

# # utils #############################################################
def pprint(_): return json.dumps(_, indent=4, sort_keys=True)
def iinput(_):
    print('> ' + _, end = ': ')
    return input()
# #####################################################################

try:

    response = requests.patch(
        url='https://api-stage.maersk.com/cargoInsurancePolicies/6861107',
        headers={
            'userId': 'dpm021',
            'content-type': 'application/json',
            'requestDate': '2019-12-04T14:51:13',
            'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJraWQiOiJPYUlROVo4emw1WWFOanFZMVFmZlhYd1Jhb3M9IiwiYWxnIjoiUlMyNTYifQ.eyJhdF9oYXNoIjoidUQ5SzlkQnhucHpJWUZjWkgzNDJ4QSIsInN1YiI6Imluc3VyYW5jZS5jYW5jZWxsYXRpb24iLCJmaXJzdG5hbWUiOiJpbnN1cmFuY2UiLCJjdXN0b21lclN0YXRlIjoiMTExMCIsImF1ZGl0VHJhY2tpbmdJZCI6IjQyNGEyYWI5LTdhYjgtNDZmNC05ZWQwLThiOWVmMDAzNDBhNC0zNzgwNzAxIiwicm9sZXMiOlsiQmFzaWNTb2Z0VXNlciJdLCJpc3MiOiJodHRwczovL2lhbS1jZHQubWFlcnNrLmNvbS9hY20vb2F1dGgyL21hdSIsInRva2VuTmFtZSI6ImlkX3Rva2VuIiwibm9uY2UiOiJ0MG1zbEtiOTdvdk0yeWJ1eU5rUyIsImxhc3RuYW1lIjoiY2FuY2VsbGF0aW9uIiwiYXVkIjoiYmNhMDAxIiwiY19oYXNoIjoidmt3VFhoVTN4a0dsOTdrQk9SbkN1USIsImFjciI6IjAiLCJjYXJyaWVyIjoiTUFFVSIsIm9yZy5mb3JnZXJvY2sub3BlbmlkY29ubmVjdC5vcHMiOiJoTUNjNlJjNzBQVFFPcWJjQUFzSUFOdjVUczAiLCJhenAiOiJiY2EwMDEiLCJhdXRoX3RpbWUiOjE1ODIwMzg2NjAsInJlYWxtIjoiL21hdSIsImV4cCI6MTU4MjA0NTg2MSwidG9rZW5UeXBlIjoiSldUVG9rZW4iLCJpYXQiOjE1ODIwMzg2NjEsImVtYWlsIjoiZGlvZ28ucGVyZWlyYS5tYXJxdWVzQG1hZXJzay5jb20iLCJ1c2VybmFtZSI6Imluc3VyYW5jZS5jYW5jZWxsYXRpb24ifQ.PHKwq2xyEwJxyF-zTh4mB7ZskGzq-onbZp-i68mCuYjc9LwLxJDykp8BY71PEkKQdpd9JWMXy0oTyIT9XfzXpYyTG0obS0OuDB9AACqW7CbniLRRG6JVRCsf6qjBt-Bta92ylAWAPALuCxHZIa72GhA2UiefabpBSMpSMggcaFdOx_uV_JS6dIeYXmp8qbLI4xhO6riym42MEDYqcaBG4sFluH4Fo1nQ9tWEY0b6yh1SNJW5g1hzPU-u8A_Mkijk5aL2eR4La8Pw5GNkhZ3Obb_bylbO0e8jtCiocRhrrt860WwOP6vwZ_-10S4mdi5lcFkqj702Gb_yb3UWl8Kc3g'
        },
        data={
            'carrierCode': 'MAEU',
            'policyStatus': 'Cancelled',
            'priceOwnerCode': '12700306894',
            'cancellationReason': 'ByCustomer',
        },
    )

    print('> sending request...')

    # raise HTTPError for specific status codes
    response.raise_for_status()

except HTTPError as http_err:
    print(f'HTTP err: {http_err}\n')

except Exception as err:
    print(f'Other err: {err}\n')

else:
    print('OK\n')
finally:
    print(f'RESPONSE.HEADERS: {response.headers}\n')
    # print(f'CONTENT: {response.content}\n')
    # print(f'TEXT: {response.text}\n')
    print(f'RESPONSE.TEXT: {pprint(response.json())}\n')


