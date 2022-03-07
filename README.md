<p>
<img src="https://img.shields.io/static/v1?label=STATUS&message=EM%20DESENVOLVIMENTO&color=GREEN"/>
<img src="https://img.shields.io/static/v1?label=licene&message=MIT&color=green" />
</p>

# Desafio programação

## Recursos

- [x] Upload de arquivos formato CNAB
- [x] Processamento de arquivo CNAB
- [x] Processamento assíncrono em segundo plano
- [x] Cadastro no banco de dados (PostgreSQL) de informações
- [x] API REST
- [x] Endpoint de consulta a informações processadas de arquivos CNAB
- [x] Endpoint de consulta a transações
- [x] Autenticação de usuário
- [x] Testes automatizados
- [ ] Lista de operações importadas
- [ ] Atenticação Oauth
- [ ] Melhor cobertura de testes

## Tecnologias utilizadas

- Python 3.9
- Django 4
- Docker

# Dependências

* Docker - [Instalando o Docker](https://docs.docker.com/desktop/)
* Docker compose - [Instalando o Docker Compose](https://docs.docker.com/compose/install/)

<br>
<br>
<hr>

# Iniciando e utilizando o projeto

1. Clonando o repositório

```bash
git clone git@github.com:deividsonorio/desafio-dev.git
```

2. Na pasta clonada do projeto:

```bash
docker-compose up -d
```
3. Serão criados os contâiners necesários para aplicação. 

- desafio-dev_app: Contâiner do aplicativo
- desafio-dev_db: Banco de dados PostgreSQL
- desafio-dev_redis: Contâiner Redis para criação de filas
- desafio-dev_celery: Contâiner Celery para tarefas e workers

4. A aplicação estará disponível em:

* <http://localhost:8000/>

![Imagem da tela inicial da API](./tela-api.png?raw=true "Imagem da tela inicial da API")

<br>

**OBS**: será necessário um usuário e senha para o acesso às URLs de consultas e ao formulário.

Um super usuário é criado automaticamente:

```yml
Usuário: desafio
Senha: dev@pass
```

<br>
<br>
<hr>

# API REST

## Autenticação

A autenticação é feita através de um usuário com permissões.

Na criação do projeto um usuário é criado automaticamente:
```yml
Usuário: desafio
Senha: dev@pass
```

## Página inicial

### Request

`GET /`

    curl -u 'desafio:dev@pass' -i -H 'Accept: application/json' http://localhost:8000/

### Response

    HTTP/1.1 200 OK
    Date: Mon, 07 Mar 2022 18:48:45 GMT
    Server: WSGIServer/0.2 CPython/3.9.9
    Content-Type: application/json
    Vary: Accept, Cookie
    Allow: GET, HEAD, OPTIONS
    X-Frame-Options: DENY
    Content-Length: 189
    X-Content-Type-Options: nosniff
    Referrer-Policy: same-origin
    Cross-Origin-Opener-Policy: same-origin
    
    {"users":"http://localhost:8000/users/","cnab_list":"http://localhost:8000/cnab_list/","transaction_list":"http://localhost:8000/transaction_list/","upload":"http://localhost:8000/upload/"}

## Lista de informações processadas através dos arquivos formato CNAB

### Request

`GET /cnab_list/`

    curl -u 'desafio:dev@pass' -i -H 'Accept: application/json' http://localhost:8000/cnab_list/

### Response

    HTTP/1.1 200 OK
    Date: Mon, 07 Mar 2022 18:49:38 GMT
    Server: WSGIServer/0.2 CPython/3.9.9
    Content-Type: application/json
    Vary: Accept, Cookie
    Allow: GET, POST, HEAD, OPTIONS
    X-Frame-Options: DENY
    Content-Length: 3409
    X-Content-Type-Options: nosniff
    Referrer-Policy: same-origin
    Cross-Origin-Opener-Policy: same-origin
    
    [{"type":"http://localhost:8000/transaction_list/3/","date":"20190301","value":"0000019200","cpf":"84515254073","card":"6777****1313","hour":"172712","shop_owner":"MARCOS PEREIRA","shop_name":"MERCADO DA AVENIDA"},{"type":"http://localhost:8000/transaction_list/3/","date":"20190301","value":"0000019200","cpf":"84515254073","card":"6777****1313","hour":"172712","shop_owner":"MARCOS PEREIRA","shop_name":"MERCADO DA AVENIDA"},{"type":"http://localhost:8000/transaction_list/3/","date":"20190301","value":"0000019200","cpf":"84515254073","card":"6777****1313","hour":"172712","shop_owner":"MARCOS PEREIRA","shop_name":"MERCADO DA AVENIDA"},{"type":"http://localhost:8000/transaction_list/3/","date":"20190301","value":"0000019200","cpf":"84515254073","card":"6777****1313","hour":"172712","shop_owner":"MARCOS PEREIRA","shop_name":"MERCADO DA AVENIDA"},{"type":"http://localhost:8000/transaction_list/3/","date":"20190301","value":"0000019200","cpf":"84515254073","card":"6777****1313","hour":"172712","shop_owner":"MARCOS PEREIRA","shop_name":"MERCADO DA AVENIDA"},{"type":"http://localhost:8000/transaction_list/3/","date":"20190301","value":"0000019200","cpf":"84515254073","card":"6777****1313","hour":"172712","shop_owner":"MARCOS PEREIRA","shop_name":"MERCADO DA AVENIDA"},{"type":"http://localhost:8000/transaction_list/3/","date":"20190301","value":"0000019200","cpf":"84515254073","card":"6777****1313","hour":"172712","shop_owner":"MARCOS PEREIRA","shop_name":"MERCADO DA AVENIDA"},{"type":"http://localhost:8000/transaction_list/3/","date":"20190301","value":"0000019200","cpf":"84515254073","card":"6777****1313","hour":"172712","shop_owner":"MARCOS PEREIRA","shop_name":"MERCADO DA AVENIDA"},{"type":"http://localhost:8000/transaction_list/3/","date":"20190301","value":"0000019200","cpf":"84515254073","card":"6777****1313","hour":"172712","shop_owner":"MARCOS PEREIRA","shop_name":"MERCADO DA AVENIDA"},{"type":"http://localhost:8000/transaction_list/3/","date":"20190301","value":"0000019200","cpf":"84515254073","card":"6777****1313","hour":"172712","shop_owner":"MARCOS PEREIRA","shop_name":"MERCADO DA AVENIDA"},{"type":"http://localhost:8000/transaction_list/3/","date":"20190301","value":"0000019200","cpf":"84515254073","card":"6777****1313","hour":"172712","shop_owner":"MARCOS PEREIRA","shop_name":"MERCADO DA AVENIDA"},{"type":"http://localhost:8000/transaction_list/3/","date":"20190301","value":"0000019200","cpf":"84515254073","card":"6777****1313","hour":"172712","shop_owner":"MARCOS PEREIRA","shop_name":"MERCADO DA AVENIDA"},{"type":"http://localhost:8000/transaction_list/3/","date":"20190301","value":"0000019200","cpf":"84515254073","card":"6777****1313","hour":"172712","shop_owner":"MARCOS PEREIRA","shop_name":"MERCADO DA AVENIDA"},{"type":"http://localhost:8000/transaction_list/3/","date":"20190301","value":"0000019200","cpf":"84515254073","card":"6777****1313","hour":"172712","shop_owner":"MARCOS PEREIRA","shop_name":"MERCADO DA AVENIDA"},{"type":"http://localhost:8000/transaction_list/3/","date":"20190301","value":"0000019200","cpf":"84515254073","card":"6777****1313","hour":"172712","shop_owner":"MARCOS PEREIRA","shop_name":"MERCADO DA AVENIDA"},{"type":"http://localhost:8000/transaction_list/3/","date":"20190301","value":"0000019200","cpf":"84515254073","card":"6777****1313","hour":"172712","shop_owner":"MARCOS PEREIRA","shop_name":"MERCADO DA AVENIDA"}]

## Informação específica

### Request

`GET /cnab_list/<ID>`

    curl -u 'desafio:dev@pass' -i -H 'Accept: application/json' http://localhost:8000/cnab_list/3/

### Response

    HTTP/1.1 200 OK
    Date: Mon, 07 Mar 2022 18:53:19 GMT
    Server: WSGIServer/0.2 CPython/3.9.9
    Content-Type: application/json
    Vary: Accept, Cookie
    Allow: GET, PUT, PATCH, DELETE, HEAD, OPTIONS
    X-Frame-Options: DENY
    Content-Length: 212
    X-Content-Type-Options: nosniff
    Referrer-Policy: same-origin
    Cross-Origin-Opener-Policy: same-origin
    
    {"type":"http://localhost:8000/transaction_list/3/","date":"20190301","value":"0000019200","cpf":"84515254073","card":"6777****1313","hour":"172712","shop_owner":"MARCOS PEREIRA","shop_name":"MERCADO DA AVENIDA"}

## Lista de tipos de transações

### Request

`GET /transaction_list/`

    curl -u 'desafio:dev@pass' -i -H 'Accept: application/json' http://localhost:8000/transaction_list/

### Response

    HTTP/1.1 200 OK
    Date: Mon, 07 Mar 2022 18:55:08 GMT
    Server: WSGIServer/0.2 CPython/3.9.9
    Content-Type: application/json
    Vary: Accept, Cookie
    Allow: GET, POST, HEAD, OPTIONS
    X-Frame-Options: DENY
    Content-Length: 620
    X-Content-Type-Options: nosniff
    Referrer-Policy: same-origin
    Cross-Origin-Opener-Policy: same-origin
    
    [{"type":1,"description":"Débito","nature":"Entrada","sign":"+"},{"type":2,"description":"Boleto","nature":"Saída","sign":"-"},{"type":3,"description":"Financiamento","nature":"Saída","sign":"-"},{"type":4,"description":"Crédito","nature":"Entrada","sign":"+"},{"type":5,"description":"Recebimento Empréstimo","nature":"Entrada","sign":"+"},{"type":6,"description":"Vendas","nature":"Entrada","sign":"+"},{"type":7,"description":"Recebimento TED","nature":"Entrada","sign":"+"},{"type":8,"description":"Recebimento DOC","nature":"Entrada","sign":"+"},{"type":9,"description":"Aluguel","nature":"Saída","sign":"-"}]


## Tipo específico de transação

### Request

`GET /transaction_list/<ID>/`

    curl -u 'desafio:dev@pass' -i -H 'Accept: application/json' http://localhost:8000/transaction_list/5/

### Response

    HTTP/1.1 200 OK
    Date: Mon, 07 Mar 2022 18:56:43 GMT
    Server: WSGIServer/0.2 CPython/3.9.9
    Content-Type: application/json
    Vary: Accept, Cookie
    Allow: GET, PUT, PATCH, DELETE, HEAD, OPTIONS
    X-Frame-Options: DENY
    Content-Length: 80
    X-Content-Type-Options: nosniff
    Referrer-Policy: same-origin
    Cross-Origin-Opener-Policy: same-origin
    
    {"type":5,"description":"Recebimento Empréstimo","nature":"Entrada","sign":"+"}

## Upload de arquivo

### Request

`POST /upload/`

### Response
    
OBS: _arquiv_cnab_ é o nome do campo com o arquivo que a API espera receber

    curl -u 'desafio:dev@pass' -i -X POST -H "Content-Type: multipart/form-data" -F "arquivo_cnab=@CNAB.txt" http://localhost:8000/upload/

    HTTP/1.1 100 Continue
    
    HTTP/1.1 200 OK
    Date: Mon, 07 Mar 2022 19:02:06 GMT
    Server: WSGIServer/0.2 CPython/3.9.9
    Content-Type: application/json
    Vary: Accept, Cookie
    Allow: GET, POST, HEAD, OPTIONS
    X-Frame-Options: DENY
    Content-Length: 46
    X-Content-Type-Options: nosniff
    Referrer-Policy: same-origin
    Cross-Origin-Opener-Policy: same-origin
    
    "Arquivo enviado para processamento. CNAB.txt"

<br>
<br>
<hr>

# Teste automatizados

Os testes podem ser realizados através de:

```shell
docker exec desafio-dev_app_1 ./manage.py test cnab
```