import pika

params = pika.URLParameters(
    "amqps://bbcubjzu:cINzy3QgaUwo2dfgPIFbBgPn_JtKIj-9@mustang.rmq.cloudamqp.com/bbcubjzu")

connection = pika.BlockingConnection(params)

channel = connection.channel()

channel.queue_declare("django")


def callback(ch, method, properties, body):
    print("received in django")
    print("body", body)


channel.basic_consume(
    queue="django", on_message_callback=callback, auto_ack=True)

print("started consuming")

channel.start_consuming()

channel.close()
