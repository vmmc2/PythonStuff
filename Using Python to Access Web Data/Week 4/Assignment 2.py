import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup


name = None
url = "http://py4e-data.dr-chuck.net/known_by_Jadon.html"
for i in range(1, 8):
    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html, "html.parser")
    tags = soup('a')
    url = tags[17].get('href', None)
    name = tags[17].contents[0]

print(name)



