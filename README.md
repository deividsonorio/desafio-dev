<p>
<img src="https://img.shields.io/static/v1?label=STATUS&message=EM%20DESENVOLVIMENTO&color=GREEN"/>
<img src="https://img.shields.io/static/v1?label=licene&message=MIT&color=green" />
</p>

# Desafio programação

Este projeto foi somenmte iniciado. Foi deenvolvida uma primeira ideia devido ao tempo escasso que tive nos dias de prova.

Foi somente montada uma base. As ideias seguintes seriam implementadas caso houvesse possibilidade:

* Upload de arquivo e tratamento em "chunks" para evitar problema com tempo de processamento
* Criação de task em segundo plano com Celery, para procesamento
* Criação de endpoint para processamento de arquivo, com aproveitamento da task assíncrona
* Inserção em massa ao invés de linha a linha
* Cobertura de testes

## Recursos

- [x] Upload de arquivos formato CNAB
- [x] Processamento de arquivo CNAB
- [x] Cadastro no banco de dados (PostgreSQL) de informações

# Dependências

* Docker - [Instalando o Docker](https://docs.docker.com/desktop/)
* Docker compose - [Instalando o Docker Compose](https://docs.docker.com/compose/install/)

# Iniciando e utilizando o projeto

1. Clonando o repositório

```bash
git clone git@github.com:deividsonorio/desafio-dev.git
```

2. Na pasta clonada do projeto:

```bash
docker-compose up -d
```
3. Serão criados os contâiners necesários para aplicação. Ela estará disponível no endereço:

<http://localhost:8000/cnab/>