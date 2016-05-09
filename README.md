# DjangoBackend
Django Backend for individual project

## Setup

RabbitMQ server
`rabbitmq-server`

Celery worker(s)
`
celery -A backend worker -l info
`

Web server
`
python manage.py runserver
`

##To Do:
- [ ] Create transactoin graph based on single address (history)
- [ ] Expand diameter to trace coin usage
- [ ] Show path of specific coin until all coinbase (utxo/txo)
- [ ] Custom Gephi Plugin
- [ ] Multi-foci layout
- [ ] AngularJS Webpage to consume API
- [ ] Visualise (VivaGraphJS) subcomponents on web page
- [ ] Visualise (D3js) sub components on web page
- [ ] D3 Dashboard
- [X] Bug rewriting TX 
- [X] Restructure Gephi code into classes
- [ ] Use OpenOrd through Gephi Tookit
- [X] Increase iterations for subcomponets
- [X] Colour PDF correctly 
- [X] Deploy tasks using API requests
- [X] Graph creation task - collate transactions and make graph and list
- [ ] Layout task with status - send graph to gephi program to layout
- [X] Colour resulting graph - colour graphs to match Dan McGinn's colour scheme
- [ ] Custom colouring task - given layout, culour seperate large components
- [X] Subcomponent task
- [X] Write to-do list
- [X] Celery install
