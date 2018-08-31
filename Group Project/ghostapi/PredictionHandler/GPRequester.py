import pika
import uuid
import json

# TODO: Refactor this class

class GPRequester(object):
    def __init__(self, username, password, host, queue_name):
        self.username = username
        self.password = password
        self.host = host
        self.queue_name = queue_name
        # Setup connection to server
        credentials = pika.PlainCredentials(username, password)
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(
            host=host, credentials=credentials,
            heartbeat_interval=0))
        self.channel = self.connection.channel()

        # Sets up queue (creates it if needed) connection
        # Create anonymous exclusive callback queue
        result = self.channel.queue_declare(exclusive=True)         
        self.callback_queue = result.method.queue
        
        # Start listening for callback queue messages (results)
        self.channel.basic_consume(self.on_response, no_ack=True,   
                                   queue=self.callback_queue)

    # In response to receiving prediction results
    def on_response(self, ch, method, props, body):                 
        if self.corr_id == props.correlation_id:
            self.response = body
    
    # Request generation of gp model and predictions
    def generate(self, request, await_response=True):               
        if(not await_response):
            self.channel.basic_publish(exchange='', routing_key=self.queue_name, body=json.dumps(request))
            return None

        self.response = None
        self.corr_id = str(uuid.uuid4())
        self.channel.basic_publish(exchange='',
                                   routing_key=self.queue_name,
                                   properties=pika.BasicProperties(
                                         reply_to = self.callback_queue,
                                         correlation_id = self.corr_id),
                                   body=json.dumps(request))
        while self.response is None:
            self.connection.process_data_events()
        return json.loads(self.response)
