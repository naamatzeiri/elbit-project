# Kafka Publisher and Consumer

## Prerequisites

- Download docker and docker-compose
- Python installed
- `confluent_kafka` library installed (`pip install confluent_kafka`)

## Setting Up Kafka

- Write a 'docker-compose' file consisting of a kafka image and a zookeeper image and deploy it.

## Writing the Kafka Python files

- Write a publisher.py file: Sends 10 messages to the kafka, which is recieved and stored by the kafka broker in the "ABC" topic.
- Write a consumer.py file: Read the messages from the "ABC" topic in the kafka broker and prints them.

## Running the Program

- Enter cmd (or vscode terminal) and writh the following command:
    - python producer.py
    - python consumer.py