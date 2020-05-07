from time import sleep
import pika

params = pika.ConnectionParameters('localhost')
connection = pika.BlockingConnection(params)

channel = connection.channel()
channel.queue_declare(queue='hello')

c = 0
while True:
    sleep(1)
    channel.basic_publish(exchange='',
                      routing_key='hello',
                      body=f'Hello World {c}')
    c += 1
