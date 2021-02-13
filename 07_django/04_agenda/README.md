# Agenda de contatos

Esse projeto contém uma agenda de contatos que permite inserção de pessoas junto com fotos.

## Deploy GCP

É preciso coletar (juntar) os arquivos estáticos antes do deploy:

```python manage.py collectstatic```

Comando para criar chave no linux para se conectar a VM:

```ssh-keygen -f ~/.ssh/chave_gcp -t rsa -b 4096```

O IP deve ser configurado como estático na GCP além do registro da SSH. Conectar ao servidor (VM) com:

```ssh nome_ssh@ip_externo```

Abaixo segue os passos para preparação do ambiente:

* Instalando

```
sudo apt-get update
sudo apt install python3-pip python3.7 python3.7-dev python3.7-venv gcc default-libmysqlclient-dev libssl-dev nginx curl
```

* Atualizando pip e demais

```
python3.7 -m pip install --upgrade pip setuptools wheel --user
export PATH="/home/$USER/.local/bin:$PATH"
python3.7 -m pip install pipenv --user
```

* Criar pasta

```mkdir agenda```

* Entrar na pasta

```cd agenda```

* Criando o ambiente virtual

```
python3.7 -m venv .venv
source .venv/bin/activate
python3.7 -m pip install django gunicorn pillow
exit
```

* Mover arquivos para servidor (SO Linux)

```
# voltar um diretório antes da raiz do projeto
cd ..
sftp nome_ssh@ip_externo
put -R 04_agenda/* agenda
exit
```

Entrar novamente na VM e testar *gunicorn* para ver se consegue rodar na porta 8000:

```
sftp nome_ssh@ip_externo
cd agenda
source .venv/bin/activate
gunicorn --bind 0.0.0.0:8000 agenda.wsgi
```
