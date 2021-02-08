import pika
message="fraud.jpg was edited:id"
connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='editedImage')

channel.basic_publish(exchange='', routing_key='editedImage', body=message)
print(" [x] Sent "+message)
connection.close()