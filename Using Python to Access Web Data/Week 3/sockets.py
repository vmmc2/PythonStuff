# Python, como a boa linguagem que eh, apresenta suporte simples para trabalharmos com sockets.

import socket  # necessario dar import nessa lib para trabalharmos com os sockets.

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Nessa linha, a gente faz a criacao do nosso socket (que vai servir para estabelecermos a comunicacao entre a nossa maquina e um servidor, por exemplo)
mysock.connect(("data.pr4e.org", 80)) # Nessa linha, a gente ta fazendo de fato a conexao entre a nossa maquina e um servidor. Para isso, a gente deve fornecer o host e uma porta.
