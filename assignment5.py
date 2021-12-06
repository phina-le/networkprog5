import requests
import json

#get API
response = requests.get("https://api.covidtracking.com/v1/us/daily.json").json()

#initialize dict
d = {"country":"United States"} #I couldn't find any "country" or "United States" in the API
index = 1

#reformat date strings
def reformat(s):
    s = str(s)
    newS = s[4:6] + "-" + s[6:8] + "-" + s[:4]
    return newS

#fill dict
for i in range(4, -1, -1):
    d["day" + str(index)]= [reformat(response[i]['date']), (response[i]['positive'])]
    index = index + 1
print(d)