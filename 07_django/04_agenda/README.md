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

* Entrar novamente na VM e testar *gunicorn* para ver se consegue rodar na porta 8000:

```
sftp nome_ssh@ip_externo
cd agenda
source .venv/bin/activate
gunicorn --bind 0.0.0.0:8000 agenda.wsgi
```

* Redirecionar o domínio (nome do site) usando cloudflare (*não executado, apenas listado*)

* Abaixo tutorial da Digital Ocean (Nginx e Gunicorn)

```
ssh nome_ssh@ip_externo

## FONTE:
## https://www.digitalocean.com/community/tutorials/how-to-set-up-django-with-postgres-nginx-and-gunicorn-on-ubuntu-18-04

# Criando o arquivo (socket)
sudo nano /etc/systemd/system/gunicorn.socket
##################################################

# COLAR (SEM EDIÇÃO)
[Unit]
Description=gunicorn socket

[Socket]
ListenStream=/run/gunicorn.sock

[Install]
WantedBy=sockets.target
##################################################
# Para salvar a escrita acima : Ctrl O + Enter + Ctrl X

# Criando outro arquivo (criando um serviço)
sudo nano /etc/systemd/system/gunicorn.service
##################################################

# Editar, depois Colar (nome de usuário e conferir local venv)
[Unit]
Description=gunicorn daemon
Requires=gunicorn.socket
After=network.target

[Service]
User=carlos
Group=www-data
WorkingDirectory=/home/carlos
ExecStart=/home/carlos/agenda/.venv/bin/gunicorn \
          --access-logfile - \
          --workers 3 \
          --bind unix:/run/gunicorn.sock \
          agenda.wsgi:application

[Install]
WantedBy=multi-user.target  
##################################################

# Ativando
sudo systemctl start gunicorn.socket
sudo systemctl enable gunicorn.socket
##################################################

# Checando
sudo systemctl status gunicorn.socket

# ABAIXO ESTÁ DANDO PAU COM A SEGUINTE MENSAGEM (deploy não foi finalizado)
sudo systemctl status gunicorn
<!--
● gunicorn.service - gunicorn daemon
   Loaded: loaded (/etc/systemd/system/gunicorn.service; disabled; vendor preset: enabled)
   Active: failed (Result: exit-code) since Sat 2021-02-13 15:53:27 UTC; 23min ago
 Main PID: 12528 (code=exited, status=3)

Feb 13 15:53:27 app-django gunicorn[12528]:   File "<frozen importlib._bootstrap>", line 965, in _fin
Feb 13 15:53:27 app-django gunicorn[12528]: ModuleNotFoundError: No module named 'agenda.wsgi'
Feb 13 15:53:27 app-django gunicorn[12528]: [2021-02-13 15:53:27 +0000] [12558] [INFO] Worker exiting
Feb 13 15:53:27 app-django gunicorn[12528]: [2021-02-13 15:53:27 +0000] [12528] [INFO] Shutting down:
Feb 13 15:53:27 app-django gunicorn[12528]: [2021-02-13 15:53:27 +0000] [12528] [INFO] Reason: Worker
Feb 13 15:53:27 app-django systemd[1]: gunicorn.service: Main process exited, code=exited, status=3/N
Feb 13 15:53:27 app-django systemd[1]: gunicorn.service: Failed with result 'exit-code'.
Feb 13 15:53:27 app-django systemd[1]: gunicorn.service: Start request repeated too quickly.
Feb 13 15:53:27 app-django systemd[1]: gunicorn.service: Failed with result 'exit-code'.
Feb 13 15:53:27 app-django systemd[1]: Failed to start gunicorn daemon.
 -->

curl --unix-socket /run/gunicorn.sock localhost
sudo systemctl status gunicorn
##################################################

sudo nano /etc/nginx/sites-enabled/sitedjango
# Colar o aqui abaixo após execução do comando acima
##################################################

# Configurando o nginx server block (mais simples possível)
server {
    listen 80;
    server_name ip_servidor;

    location = /favicon.ico { access_log off; log_not_found off; }

    location /static/ {
        root /home/carlos/agenda;
    }

    location /media {
        alias /home/carlos/agenda/media/;
    }

    location / {
        include proxy_params;
        proxy_pass http://unix:/run/gunicorn.sock;
    }
}

##################################################

sudo rm /etc/nginx/sites-enabled/default
sudo systemctl restart nginx
sudo systemctl restart gunicorn

sudo vim agenda/agenda/settings.py
# add ip ALLOWED_HOSTS e outras modificações não citadas (como tirar do modo DEBUG)
##################################################
```

*ATENÇÃO*: a partir daqui não foram descritos os passos para deploy já que não foi possível avançar com o erro citada anteriormente em um dos passos. Será apenas adicionado os arquivos com comandos.

* Configurando HTTPS e Segurança

Arquivos para esse etapa são encontrados no diretório `nginx_deploy`.

* Migrar para o BD MySQL (MariaDB)

Arquivos se encontra em `deploy/mysql.txt`.

* Conectar git no servidor e configurar local settings

* Customização da área Admin
