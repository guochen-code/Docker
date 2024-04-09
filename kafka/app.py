from flask import Flask, Response
import time
import json  # Add import for the json module
from kafka import KafkaConsumer

app = Flask(__name__)

def kafka_event_stream():
    consumer = KafkaConsumer('sample', bootstrap_servers='localhost:9092,localhost:9093,localhost:9094', 
                             value_deserializer=lambda m: json.loads(m.decode('utf-8')))
    for message in consumer:
        yield f"data: {json.dumps(message.value)}\n\n"  # Serialize message value to JSON

@app.route('/stream')
def stream():
    return Response(kafka_event_stream(), mimetype="text/event-stream")