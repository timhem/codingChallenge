import asyncio
import uuid

from gmqtt import Client as MQTTClient

q = asyncio.Queue()

STOP = asyncio.Event()


def on_connect(client, flags, rc, properties):
    print('Connected to MQTT broker')
    client.subscribe('/events', qos=0)


async def on_message(client, topic, payload, qos, properties):
    # when message is received put it in the queue
    await q.put(payload)


def on_disconnect(client, packet, exc=None):
    print('Disconnected from broker')


def on_subscribe(client, mid, qos, properties):
    print(f'Subscribed to {client.subscriptions[0].topic}')


async def main(broker_ip):
    client = MQTTClient(str(uuid.uuid1()))  # random UID for identification

    # register listener for mqtt events
    client.on_connect = on_connect
    client.on_message = on_message
    client.on_disconnect = on_disconnect
    client.on_subscribe = on_subscribe
    # get the async event loop to attach the read_queue task
    loop = asyncio.get_event_loop()
    loop.create_task(read_queue())

    await client.connect(broker_ip)  # connect to mqtt broker
    await STOP.wait()  # wait for a termination signal
    await client.disconnect()  # disconnect the client


async def read_queue():
    """
    Read a message every 10 seconds and just wait if nothing arrives.
    Increase a counter to count the total number of messages
    Print the message, counter for queue and total number of messages
    :return:
    """
    while True:
        global received
        await asyncio.sleep(10)
        msg = await q.get()
        received += 1
        print(f'The message is {msg}. The Queue still holds {q.qsize()} items and processed {received} Messages')


if __name__ == '__main__':
    received = 0
    broker = 'localhost'
    asyncio.run(main(broker))
