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
r = requests.get("https://raw.githubusercontent.com/ExploreNcrack/CMPUT404-LAB/master/Lab1/lab1.py")
print(r.status_code)
print(r.text)
