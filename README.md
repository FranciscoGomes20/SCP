# SCP - Sistema de Chamados Python

<!-- ## Heroku 

No momento, o projeto está rodando em um servidor do Heroku. Você pode acessar e testar através do link:
<p></p>

-->

## Pré-Requisitos

Deve possuir o Python na versão 3.9 instalado na máquina (preferencialmente a versão 3.9.8)

## Instalação

Inicie um ambiente virtual

```python
python -m venv venv
```

Após isso, acesse a pasta do ambiente pelo terminal e ative o arquivo "activate.bat"

```bash
venv\Scripts\activate
```

## Instalando dependências do projeto

Use o gerenciador de pacotes do python para baixar as as bibliotecas necessárias do arquivo requirements.txt

```bash
pip install -r requirements.txt
```

## Executando comandos de migration para banco de dados

Para rodar o projeto, primeiramente devem ser rodados os comandos de migração do banco

```bash
python manage.py makemigrations
```

E também:

```bash
python manage.py migrate
```

## Executando o projeto localmente

Após abrir a pasta raiz do projeto (onde está o arquivo manage.py), com suas devidas dependências instaladas e dentro de um ambiente virtual (de preferência), execute o comando abaixo no terminal.

```bash
python manage.py runserver
```
Isso irá rodar o projeto em um servidor local, caso uma janela do navegador não se inicie sozinha, clique no link gerado no terminal.

## Contribuições

<a href="https://github.com/cristiansuzuki/"></a> [@cristiansuzuki](https://github.com/cristiansuzuki) 


