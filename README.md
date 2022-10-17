# celeryrmq
This is a simple project that uses celery and rabbitmq to send emails 

## To start the rabbitmq server:
rabbitmq-server

you can view the rabbitmq server in the browser by going to http://localhost:15672    guest is the username and password

## To start it in the backgound (mac):
brew services start rabbitmq

## To stop the server:
brew services stop rabbitmq

## To start the celery 
celery -A celeryrmq worker -l INFO

