"""
    This program sends a message to a queue on the RabbitMQ server.

    Author: Pasquale Salomone
    Date: August 28, 2023

"""

# add imports at the beginning of the file
import pika, sys

def send_message(host: str, queue_name: str, message: str):
    """
    Sends a message to a queue on the RabbitMQ server.

    Author: Pasquale Salomone
    Date: August 28, 2023

    Parameters:
        host (str): The hostname or IP address of the RabbitMQ server.
        queue_name (str): The name of the queue to which the message will be sent.
        message (str): The message to be sent to the queue.

    Raises:
        AMQPConnectionError: If a connection to the RabbitMQ server cannot be established.

    """
   

    try:
        # create a blocking connection to the RabbitMQ server
        conn = pika.BlockingConnection(pika.ConnectionParameters(host))
        # use the connection to create a communication channel
        ch = conn.channel()
        # use the channel to declare a queue
        ch.queue_declare(queue=queue_name)
        # use the channel to publish a message to the queue
        ch.basic_publish(exchange="", routing_key=queue_name, body=message)
        # print a message to the console for the user
        print(f" [x] Sent {message}")
    except pika.exceptions.AMQPConnectionError as e:
        print(f"Error: Connection to RabbitMQ server failed: {e}")
        sys.exit(1)
    finally:
        # close the connection to the server
        conn.close()

# Standard Python idiom to indicate main program entry point
# This allows us to import this module and use its functions
# without executing the code below.
# If this is the program being run, then execute the code below
if __name__ == "__main__":
    send_message("localhost","hello","Hello World!")