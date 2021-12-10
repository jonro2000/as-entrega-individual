import sys
import requests
from requests.exceptions import HTTPError

url = sys.argv[1]
try:
    response = requests.get(url)

    # If the response was successful, no Exception will be raised
    response.raise_for_status()
except HTTPError as http_err:
    print(f'HTTP error occurred: {http_err}')  # Python 3.6
except Exception as err:
    print(f'Other error occurred: {err}')  # Python 3.6
else:
    print('Success!')
    print(response.text)
    print(response.headers)
    f = open('/home/vagrant/shared_folder/data/content.html', 'w')
    f.write(response.text)
    f.close()
    f = open('/home/vagrant/shared_folder/data/headers.txt', 'w')
    f.write(str(response.headers))
    f.close()
