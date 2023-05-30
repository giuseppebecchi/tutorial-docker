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

4) Un editor di testo. Si consiglia Pycharm (Community o Professional) per la parte su python. Comunque ai fini di questa esercitazione va bene un editor qualsiasi.


## Questi saranno in punti coperti nel tutorial

### 1) differenza tra virtual machine (vagrant) e docker
### 2) concetti base docker (images, container, network, stack, hub)
https://docs.docker.com/get-started/
https://hub.docker.com/

Maggiori approfondimenti:
https://www.slideshare.net/valix85/introduzione-a-docker-maggio-2017-ita?qid=2689113a-d449-4eb8-be13-fc6a21c6f3d6&v=&b=&from_search=4


### 3) realizzazione di un container con software python e sharing attraverso hub.docker.com
https://docs.docker.com/language/python/

File esercitazione: 3_container_python

Task da eseguire:
- analizzare dockerfile
- docker build --tag python-docker .
- docker images ls

#nessuna porta esposta
- docker run  python-docker

- docker run -p 5000:5000 python-docker

- docker run -p 5010:5000 python-docker

- docker run -p 5010:5000 -d python-docker

- docker ps

- docker logs -f [NAME o CONTAINER ID]

- docker stop [NAME o CONTAINER ID]


- docker-compose up

- Ctrl + c per fermarlo

- docker-compose up -d

- docker-compose stop

- docker-compose down

#rinominare
.env.example -> .env

#decommentare linee virtual env nel docker-compose


#verificare lettura della variabile di ambiente
- docker-compose up -d

Importante per personalizzare le password/key e per configurare il comportamento dei containers.


#condivisione immagini su hub docker

- aprire https://hub.docker.com/

- docker tag python-docker [IL_TUO_USERNAME]/python-docker

- docker login

- docker push [IL_TUO_USERNAME]/python-docker

- docker run -p 5020:5000 ciuster/python-docker




##Esercitazione che potete provare a fare:

Vedere com'è documentata l'immagine ufficiale docker di wordpress:

https://hub.docker.com/_/wordpress

Come avviare lo stack seguendo la documentazione (con il docker-compose)




### 4) configurazione di uno stack lamp

File esercitazione: 4_stack_lamp

Task da eseguire:
docker-compose up -d

Verificare:
web:
http://localhost:4000/

adminer:
http://localhost:8080/


Come entrare e ispezionare un container in esecuzione:

docker exec -it ____nome_container___ bash


Testare volumi per:

- persistenza dei dati (db)

- condivisione dati iniziali startup container (db)

- vedere documentazione https://hub.docker.com/_/mysql

- codice sincronizzato per sviluppo (decommentare volume nel container web)


docker-compose down

### 5) configurazione di uno stack con applicativo django (https://www.djangoproject.com/)
https://docs.docker.com/compose/django/
File esercitazione: 5_stack_django

Task da eseguire (se non funziona sudo):

docker-compose run web django-admin startproject composeexample .


Vengono creati:
1) cartella composeexample
2) file manage.py


Editare composeexample/settings.py


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('POSTGRES_NAME'),
        'USER': os.environ.get('POSTGRES_USER'),
        'PASSWORD': os.environ.get('POSTGRES_PASSWORD'),
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

#eseguire un comando dall'esterno sul container con docker exec
docker exec 5_stack_django_web_1 python manage.py help


#eseguire un comando con docker-compose
docker-compose exec web python manage.py help


#eseguire il comando migrate per inizializzare il DB con le tabelle di base di python
docker exec 5_stack_django_web_1 python manage.py migrate


#creare un utente admin
docker exec -it 5_stack_django_web_1 python manage.py createsuperuser


#creare una APPLICATION dal nome "art"
docker exec -it 5_stack_django_web_1 python manage.py startapp art

-> viene creata la cartella art


#aggiungerla in settings.py

    INSTALLED_APPS = [

        ....
        ....,
        'art',

    ]


#creare un modello nel file art/models.py

    class Item(models.Model):
        title = models.CharField(max_length = 150,null=True,blank=True)
        code = models.CharField(max_length = 150,null=True,blank=True)
        description = models.TextField(null=True,blank=True)

        def __str__(self):
            return str(self.title)

#creare il file di migrazione ed effettuare la migrazione per creare le tabelle in DB

docker exec -it 5_stack_django_web_1 python manage.py makemigrations

docker exec -it 5_stack_django_web_1 python manage.py migrate

verificare nell'adminer la creazione della nuova tabella


# configurare l'area amministrativa per questo oggetto nel file art/admin.py

    from .models import Item
    admin.site.register(Item)


verificare nell'area amministrativa la gestione del nuovo tipo di oggetti












