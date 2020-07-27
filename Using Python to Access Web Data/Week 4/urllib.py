# In Python, we have a library called "urllib" that makes easy for us to work with sockets and to retrieve web-pages (web-data) from the internet.

# Since HTTP is so common, we have this library that does all the socket work for us and makes the web pages look like a file.

import urllib.request, urllib.parse, urllib.error

fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
for line in fhand:
  print(line.decode().strip())
