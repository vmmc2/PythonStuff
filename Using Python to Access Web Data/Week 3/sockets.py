# Python, como a boa linguagem que eh, apresenta suporte simples para trabalharmos com sockets.

import socket  # necessario dar import nessa lib para trabalharmos com os sockets.

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Nessa linha, a gente faz a criacao do nosso socket (que vai servir para estabelecermos a comunicacao entre a nossa maquina e um servidor, por exemplo)
mysock.connect(("data.pr4e.org", 80)) # Nessa linha, a gente ta fazendo de fato a conexao entre a nossa maquina e um servidor. Para isso, a gente deve fornecer o host e uma porta.

cmd = "GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n".encode() # Isso aqui eh basicamente o comando que vamos enviar para o servidor. No caso, estamos enviando um comando do tipo GET para solicitar dados/documento.
mysock.send(cmd) # Enviando o nosso comando para o servidor.

while True:
  data = mysock.recv(512) # Comando para recebr os dados provenientes do servidor ao qual nos conectamos. Nesse caso, podemos receber apenas 512 caracteres por vez.
  if len(data) < 1:
    break # Isso quer dizer que nao estamos mais recebendo dados do servidor.
  print(data.decode())
mysock.close() # Acabamos de pegar os dados que queriamos, fechamos o socket, interrompendo a conexao com o servidor.
