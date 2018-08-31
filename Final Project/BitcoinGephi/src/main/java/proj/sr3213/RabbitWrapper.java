package proj.sr3213;

import com.rabbitmq.client.*;

import java.io.IOException;
import com.rabbitmq.client.AMQP.BasicProperties;

public class RabbitWrapper {

    private final static String LAYOUT_QUEUE = "ToLayout";

    private Channel channel;
    private Connection connection;
    private QueueingConsumer consumer;
    private BasicProperties props;
    private BasicProperties replyProps;
    private QueueingConsumer.Delivery delivery;

    public RabbitWrapper() throws IOException{
        this("localhost");
    }

    public RabbitWrapper(String host) throws IOException{
        ConnectionFactory factory = new ConnectionFactory();
        factory.setHost("localhost");
        connection = factory.newConnection();
        channel = connection.createChannel();

    }

    public void startConsuming() throws IOException {

        channel.queueDeclare(LAYOUT_QUEUE, false, false, false, null);

        channel.basicQos(1);

        consumer = new QueueingConsumer(channel);
        channel.basicConsume(LAYOUT_QUEUE, false, consumer);

        System.out.println(" [*] Waiting for messages. To exit press CTRL+C");
    }

    public QueueingConsumer.Delivery getDelivery() throws InterruptedException{
        delivery = consumer.nextDelivery();
        return delivery;
    }

    public String getMessage() throws InterruptedException{
        getDelivery();
        getReplyProperties();
        return new String(delivery.getBody());
    }

    public BasicProperties getReplyProperties(){
        props = delivery.getProperties();
        replyProps = new AMQP.BasicProperties
                .Builder()
                .correlationId(props.getCorrelationId())
                .build();
        return replyProps;
    }

    public void basicPublish(String response) throws IOException {
        channel.basicPublish("", props.getReplyTo(), replyProps, response.getBytes());
        channel.basicAck(delivery.getEnvelope().getDeliveryTag(), false);
    }

}
