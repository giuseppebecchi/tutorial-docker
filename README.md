# tutorial-docker
Tutorial di base per docker


## Prequisiti necessari per seguire il tutorial:

1) Installare docker sui computer che utilizzerete durante il tutorial:

https://www.docker.com/community-edition#/download
Verificare che sia installato:
docker -v

2) Installare il pacchetto docker-compose:

https://docs.docker.com/compose/install/
Questo pacchetto è già incluso per gli utenti mac os x nel software docker del punto precedente. Questa installazione si rende necessaria solamente in ambienti linux

3) Registrazione su https://hub.docker.com/

4) Un editor di testo. Si consiglia Pycharm (che utilizzerò io) per la parte su python. Comunque ai fini dell'esercitazione va bene un editor qualsiasi.


## Questi saranno in punti coperti nel tutorial

### 1) differenza tra virtual machine (vagrant) e docker
Prime 20 slide
https://www.slideshare.net/valix85/introduzione-a-docker-maggio-2017-ita?qid=2689113a-d449-4eb8-be13-fc6a21c6f3d6&v=&b=&from_search=4


### 2) concetti base docker (container, services, stack, hub)
https://docs.docker.com/get-started/
https://hub.docker.com/


### 3) realizzazione di un container con software python e sharing attraverso hub.docker.com
https://docs.docker.com/get-started/part2/
https://docs.docker.com/get-started/part3/

File esercitazione: 3_container_python

Task da eseguire:
- analizzare dockerfile
- build -t hellodocker .
- docker run -p 4000:80 hellodocker
- docker tag hellodocker [IL_TUO_USERNAME]/hellodocker:1.0
- docker push [IL_TUO_USERNAME]/hellodocker:1.0
- docker run -p 4010:80 [USERNAME_DI_UN_ALTRO]/hellodocker:1.0

- docker-compose up

- docker swarm init
- docker stack deploy -c docker-compose-ext.yml getstartedlab
- docker stack rm getstartedlab
- docker swarm leave --force



### 4) configurazione di uno stack lamp

File esercitazione: 4_stack_lamp

Task da eseguire:
docker-compose up

docker exec -it 4stacklamp_web_1 bash

Testare volumi per:
- persistenza dei dati
- condivisione dati tra container
- codice sincronizzato per sviluppo

### 5) configurazione di uno stack con applicativo django
https://docs.docker.com/compose/django/
File esercitazione: 5_stack_django

Task da eseguire:
docker-compose run web django-admin.py startproject composeexample .

Editare composeexample/settings.py

DATABASES = {
    'default': {
        'NAME': 'django',
        'ENGINE': 'django.db.backends.mysql',
        'USER': 'root',
        'PASSWORD': 'root',
        'HOST': 'db'
    }
}

docker exec -it 5stackdjangotest_web_1 bash
python manage.py migrate
python manage.py createsuperuser




