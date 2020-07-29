import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET 

fhand = urllib.request.urlopen("http://py4e-data.dr-chuck.net/comments_836304.xml")

data = ""
for line in fhand:
    data += line.decode().strip()

stuff = ET.fromstring(data)
lst = stuff.findall(".//count")
answer = 0
for element in lst:
    answer += int(element.text)
print("Sum:", answer)
