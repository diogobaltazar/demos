from requests.exceptions import HTTPError
import requests
import json

# utils #############################################################
def pprint(_): return json.dumps(_, indent=4, sort_keys=True)
#####################################################################


try:

    params = {'q': 'requests+language:python'}
    response = requests.get(
        'https://api.github.com/search/repositories',
        params,
    )

    # raise HTTPError for specific status codes
    response.raise_for_status()

except HTTPError as http_err:
    print(f'HTTP err: {http_err}')

except Exception as err:
    print(f'Other err: {err}')

else:
    print('OK')
    # print(f'HEADERS: {response.headers}\n')
    print(f'CONTENT: {response.content}\n')
    # print(f'TEXT: {response.text}\n')
    print(f'TEXT: {pprint(response.json())}\n')
    print(f'TEXT: {response.raw}\n')
