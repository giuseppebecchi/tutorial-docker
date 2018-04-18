# tutorial-docker
Tutorial di base per docker

Docker tutorial


Prequisiti necessari per seguire il tutorial:
1) Installare docker sui computer che utilizzerete durante il tutorial:
https://www.docker.com/community-edition#/download
Verificare che sia installato:
docker -v

2) Installare il pacchetto docker-compose:
https://docs.docker.com/compose/install/
Questo pacchetto è già incluso per gli utenti mac os x nel software docker. Questa installazione si rende necessaria solamente in ambienti linux


Questi saranno in punti coperti nel tutorial

1) differenza tra virtual machine (vagrant) e docker
2) concetti base docker (container, services, stack, hub)
tps://www.slideshare.net/valix85/introduzione-a-docker-maggio-2017-ita?qid=2689113a-d449-4eb8-be13-fc6a21c6f3d6&v=&b=&from_search=4
https://docs.docker.com/get-started/
https://hub.docker.com/

3) realizzazione di un container con software python e sharing attraverso hub.docker.com
https://docs.docker.com/get-started/part2/

File esercitazione: 3_container_python

Task da eseguire:
- dockerfile
- run
- build
- tagging
- upload/sharing

4) configurazione di uno stack lamp

File esercitazione: 4_stack_lamp

Task da eseguire:
docker-compose up

docker exec -it 4stacklamp_web_1 bash

Testare volumi per:
- persistenza dei dati
- condivisione dati tra container
- codice sincronizzato per sviluppo

5) configurazione di uno stack con applicativo django
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




