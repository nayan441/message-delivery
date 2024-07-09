import pika
import json
from datetime import datetime
from pymongo import MongoClient


mongo_client = MongoClient('localhost', 27017)
db = mongo_client['mqtt_data']
collection = db['status_messages']

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()


def callback(ch, method, properties, body):
    message = json.loads(body)
    message['timestamp'] = datetime.now()
    collection.insert_one(message)
    print(f" Message Received : {message}")

channel.basic_consume(queue='nayan-queue', on_message_callback=callback, auto_ack=True)

channel.start_consuming()