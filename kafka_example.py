from flask import Flask, request
from kafka import KafkaProducer, KafkaConsumer

app = Flask(__name__)

topic_name = 'FirstTopic1'
bootstrap_servers = 'localhost:9092'

#Root page
@app.route("/produce")
def produce_kafka_message():
    value = request.args.get('value') 
    if value is None:
        return "Please provide 'value' query parameter"

    producer = KafkaProducer(bootstrap_servers=bootstrap_servers)
    producer.send(topic_name, key=b'foo', value=bytes(value, 'utf-8'))
    return "sent"

    
#Consume kafka message
@app.route("/consume")
def consume_kafka_message():
    try:
        consumer = KafkaConsumer(topic_name, group_id='group_id1', bootstrap_servers=bootstrap_servers, auto_offset_reset='earliest')
        # Poll for new messages
        message_batch = consumer.poll(timeout_ms=1000) # Poll with a 1-second timeout

        for tp, messages in message_batch.items():
            for message in messages:
                return "Received message: {}".format(message.value.decode('utf-8'))
        return "No message received"
    except:
        return "Error in consuming message"
    finally:
        # Close the consumer
        consumer.close()

    