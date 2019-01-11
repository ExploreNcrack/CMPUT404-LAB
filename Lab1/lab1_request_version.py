import requests

# for testing purposes
# print out the version of requests library

print(requests.__version__)
# 2.18.4 in local
# 2.21.0 in virtual env


# For getting Google homepage
r = requests.get("http://www.google.com")
print(r.status_code)
print(r.text)

# For getting python script on github
r = requests.get("https://github.com/ExploreNcrack")
print(r.status_code)
print(r.text)
