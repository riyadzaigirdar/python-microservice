import pika
import json
from main import Product, db
params = pika.URLParameters(
    "amqps://bbcubjzu:cINzy3QgaUwo2dfgPIFbBgPn_JtKIj-9@mustang.rmq.cloudamqp.com/bbcubjzu")

connection = pika.BlockingConnection(params)

channel = connection.channel()

channel.queue_declare("flask")


def callback(ch, method, properties, body):
    print("received in flask")
    data = json.loads(body)
    print(data)
    obj = Product(id=data["id"], title=data["title"], image=data["image"])
    db.session.add(obj)
    db.session.commit()
    print("done")


channel.basic_consume(
    queue="flask", on_message_callback=callback, auto_ack=True)

print("started consuming")

channel.start_consuming()

channel.close()
