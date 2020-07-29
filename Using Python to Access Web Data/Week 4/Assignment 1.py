import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

url = "http://py4e-data.dr-chuck.net/comments_836302.html"

html = urllib.request.urlopen(url).read() # Responsavel por ler todo o conteudo do site (o arquivo html) de uma unica vez (em uma unica string).
soup = BeautifulSoup(html, "html.parser") # Responsavel por formar a arvore de elementos HTML

# Tem que encontrar todas as span tags: <span></span>
tags = soup('span') # Encontra todas as tags <span></span> e retorna uma list com elas.

answer = 0
for tag in tags:
    answer += int(tag.contents[0])
print("Sum:", answer)
