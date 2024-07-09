# Message Delivery through RabbitMQ

# Getting Started

First clone the repository from Github and switch to the new directory:

    $ git clone https://github.com/nayan441/message-delivery.git
    $ cd message-delivery
 
Activate the virtualenv for your project.
    
    $ virtualenv venv
    $ source venv/bin/activate (for Ubuntu)
    $./venv/Script/activate (for Windows)

Install project dependencies:

    $ pip install -r requirements.txt
    
You can now run the fastapi development server:

    $ python app.py

To start Publisher and Consumer for rabbitmq:

    $ python consumer.py

    $ python publisher.py
