import pika
import json

params = pika.URLParameters(
    "amqps://bbcubjzu:cINzy3QgaUwo2dfgPIFbBgPn_JtKIj-9@mustang.rmq.cloudamqp.com/bbcubjzu")

connection = pika.BlockingConnection(params)

channel = connection.channel()


def publish_product(data):
    data = json.dumps(data)
    channel.basic_publish(
        exchange="", routing_key="flask", body=data)
