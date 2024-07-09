import pika
import json
import random
import time

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.queue_declare(queue='status_queue')

def emit_message():
    status = random.randint(0, 6)
    message = {'status': status}
    channel.basic_publish(
        exchange='',
        routing_key='status_queue',
        body=json.dumps(message),
        properties=pika.BasicProperties(
            delivery_mode=2,  
        ))
    print(f" Message Sent : {message}")

try:
    while True:
        emit_message()
        time.sleep(1)  
except KeyboardInterrupt:
    print('Interrupted')
finally:
    connection.close()
