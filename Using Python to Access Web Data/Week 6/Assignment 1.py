import urllib.request, urllib.parse, urllib.error
import json

url = "http://py4e-data.dr-chuck.net/comments_836305.json"

data = urllib.request.urlopen(url).read().decode()

dic = json.loads(data)
answer = 0
for element in dic["comments"]:
    answer += int(element["count"])
print("Answer:", answer)
