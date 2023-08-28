"""
    This program sends a message to a queue on the RabbitMQ server.

    Author: Pasquale Salomone
    Date: August 28, 2023

"""

# add imports at the beginning of the file
import pika
message =['Hello World!','Hello Pasquale!','Dr.Case rocks!']
# create a blocking connection to the RabbitMQ server
conn = pika.BlockingConnection(pika.ConnectionParameters("LOCALHOST"))
# use the connection to create a communication channel
ch = conn.channel()
# use the channel to declare a queue
ch.queue_declare(queue="hello")
# use the channel to publish a message to the queue
ch.basic_publish(exchange="", routing_key="hello", body=message[0])
ch.basic_publish(exchange="", routing_key="hello", body=message[1])
ch.basic_publish(exchange="", routing_key="hello", body=message[2])
# print a message to the console for the user
print(f" [x] Sent {message[0]}")
print(f" [x] Sent {message[1]}")
print(f" [x] Sent {message[2]}")
# close the connection to the server
conn.close()
