import urllib.request, urllib.parse, urllib.error
import json

url = "http://py4e-data.dr-chuck.net/json?"

location = "University of Southern California"

url = url + urllib.parse.urlencode({'key':'42','address': location})

data = urllib.request.urlopen(url).read().decode()


dic = json.loads(data)
answer = dic['results'][0]['place_id']
print(answer)
