# DjangoBackend
Django Backend for individual project

## Setup

RabbitMQ server
`rabbitmq-server`

Celery worker(s)
`celery -A backend worker -l info`

Web server
`python manage.py runserver`

##To Do:

- [ ] Deploy tasks using API requests
- [ ] Graph creation task - collate transactions and make graph and list
- [ ] Layout task with status - send graph to gephi program to layout
- [ ] Colour resulting graph - colour graphs to match Dan McGinn's colour scheme
- [ ] Custom colouring task - given layout, culour seperate large components
- [ ] Subcomponent task
- [X] Write to-do list
- [X] Celery install
