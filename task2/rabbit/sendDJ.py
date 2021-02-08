import pika
message="celeryTemp/fraud.jpg:id"
connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='rawImage')

channel.basic_publish(exchange='', routing_key='rawImage', body=message)
print(" [x] Sent "+message)
connection.close()