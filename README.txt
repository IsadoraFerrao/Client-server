BIS
Isadora Ferrão - 151151387
Rodrigo Bisso - 151150178
Sherlon Almeida - 151150179

para rodar client.py:
    para baixar o script do servidor: 
        python3 client.py 8000 script.sh
    
    para baixar o digest do servidor confiavel: 
        python3 client.py 50000 script.sh.sha256

para rodar server.py:
    python3 server.py

para rodar eve.py:
    python3 eve.py

para rodar trusted_server:
    python3 trusted_server.py


------------------------------------------------

Foram desenvolvidos 4 scripts python: cliente, servidor, eve (atacante), e servidor seguro. O cliente se conecta com o atacante, achando que está se conectando com o servidor de onde ele quer baixar um script. O atacante recebe o pedido do cliente e repassa para o servidor. O servidor recebe o pedido do atacante e envia o arquivo, porém, antes de enviar o arquivo de fato, ele envia o SHA-256 do arquivo para outro servidor, considerado seguro. O atacante recebe o script, altera, e repassa para o cliente. O cliente por sua vez pode se conectar ao servidor seguro e pedir o SHA-256 para confrontar com o do arquivo que ele recebeu e assim verificar se houve alteração.
