# DjangoBackend
Django Backend for individual project

## Setup

RabbitMQ server
```
rabbitmq-server
```

Celery worker(s)
```
celery -A backend worker -l info
```

Web server
```
python manage.py runserver
```

Gephi worker
```
mvn exec:java
```

## Ubuntu Requirements

```
apt-get install libfreetype6-dev

```

## Basic Tmux usage for SSH

Ctrl + B then D to detach

`tmux attach` to reatach

## Cloud IPs

Gephi Worker Server: 146.169.46.179
Backend and Celery:  146.169.46.187

##To Do:
- [X] Create transactoin graph based on single address (history)
- [X] Expand diameter to trace coin usage
- [X] Show path of specific coin until all coinbase (utxo/txo)
- [X] Custom Gephi Plugin
- [X] Initial Multi-foci layout
- [ ] AngularJS Webpage to consume API
- [ ] Visualise (VivaGraphJS) subcomponents on web page
- [ ] Visualise (D3js) sub components on web page
- [ ] D3 Dashboard
- [X] Bug rewriting TX 
- [X] Restructure Gephi code into classes
- [X] Use OpenOrd
- [X] Increase iterations for subcomponets
- [X] Colour PDF correctly 
- [X] Deploy tasks using API requests
- [X] Graph creation task - collate transactions and make graph and list
- [ ] Layout task with status - send graph to gephi program to layout
- [X] Colour resulting graph - colour graphs to match Dan McGinn's colour scheme
- [ ] Custom colouring task - given layout, colour seperate large components
- [X] Subcomponent task
- [X] Write to-do list
- [X] Celery install
