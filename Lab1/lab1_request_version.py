

# for testing purposes
# print out the version of requests library

import requests

print(requests.__version__)

# 2.18.4 in local

# 2.21.0 in virtual env

r = requests.get("http://www.google.com")
print(r.status_code)
print(r.text)

r = requests.get("https://github.com/ExploreNcrack")

