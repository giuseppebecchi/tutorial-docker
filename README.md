# tutorial-docker
Tutorial di base per docker


## Prequisiti necessari per seguire il tutorial:

1) Installare docker sui computer che utilizzerete durante il tutorial:

https://docs.docker.com/get-docker/
Verificare che sia installato:
docker -v

2) Installare il pacchetto docker-compose:

https://docs.docker.com/compose/install/
Questo pacchetto è già incluso per gli utenti mac os x nel software docker del punto precedente. Questa installazione si rende necessaria solamente in ambienti linux

3) Registrazione su https://hub.docker.com/

4) Un editor di testo. Si consiglia Pycharm Professional per la parte su python. Comunque ai fini di questa esercitazione va bene un editor qualsiasi.


## Questi saranno in punti coperti nel tutorial

### 1) differenza tra virtual machine (vagrant) e docker
Prime 20 slide
https://www.slideshare.net/valix85/introduzione-a-docker-maggio-2017-ita?qid=2689113a-d449-4eb8-be13-fc6a21c6f3d6&v=&b=&from_search=4


### 2) concetti base docker (images, container, network, stack, hub)
https://docs.docker.com/get-started/
https://hub.docker.com/




### 3) realizzazione di un container con software python e sharing attraverso hub.docker.com

https://docs.docker.com/language/python/

File esercitazione: 3_container_python

Task da eseguire:
- analizzare dockerfile
- docker build --t python-docker .
- docker images ls

#nessuna porta esposta
- docker run  python-docker

- docker run -p 5000:5000 python-docker

- docker run -p 5010:5000 python-docker

- docker run -p 5010:5000 -d python-docker

- docker ps

- docker-compose up

- docker-compose up -d

- docker-compose stop
- docker-compose up down

#rinominare
.env.example -> .env

#decommentare linee virtual env nel docker-compose

#verificare lettura della variabile di ambiente
- docker-compose up -d



#condivisione immagini su hub docker

- aprire https://hub.docker.com/

- docker tag python-docker [IL_TUO_USERNAME]/python-docker

- docker login

- docker push [IL_TUO_USERNAME]/python-docker

- docker run -p 5020:5000 ciuster/python-docker









### 4) configurazione di uno stack lamp

File esercitazione: 4_stack_lamp

Task da eseguire:
docker-compose up -d

Verificare:
web
http://localhost:4000/
adminer
http://localhost:8080/



docker exec -it ____nome_container___ bash

Testare volumi per:
- persistenza dei dati (db)
- condivisione dati iniziali startup container (db)
- vedere documentazione https://hub.docker.com/_/mysql

- codice sincronizzato per sviluppo

### 5) configurazione di uno stack con applicativo django
https://docs.docker.com/compose/django/
File esercitazione: 5_stack_django

Task da eseguire (se non funziona sudo):
docker-compose run web django-admin.py startproject composeexample .

Editare composeexample/settings.py

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgres',
        'USER': 'postgres',
        'PASSWORD': 'postgres',
        'HOST': 'db',
        'PORT': 5432,
    }
}



#avviare il server
docker-compose up -d

#verificare che sia funzionante
http://localhost:8000/


#eseguire un comando dall'interno del container
docker exec -it 5_stack_django_web_1 bash
python manage.py help
exit

#eseguire un comando dall'esterno
docker exec 5_stack_django_web_1 python manage.py help
docker exec 5_stack_django_web_1 python manage.py migrate






