#Shreyan Sequeira, 02.03.2024
#MQTT data logger for dog collar project
#The functions regarding connecting to owntracks were created using the assistance of Dr. Stamou's videos and presentation on Aula
#However, I feel as though I have made enough changes to the source code that I feel I can gain credit for it
import paho.mqtt.client as mqtt
from datetime import datetime
import time

#this will hold incoming messages
messages = []
'''Callback function that connects the broker
 Upon connection, subscribes to the topic. In this case, as owntracks publishes location data, 
 this what will be obtained from the messages.'''
#08/03/2024: added a connection to the collar/logs topic
def connection(client, userdata, flags, rc):
    if rc == 0:
        client.connected_flag = True
        print("Connected OK Returned code=", rc)
        client.subscribe("owntracks/SS/#")
        client.subscribe("collar/logs")
    else:
        print("Connection Unsuccessful, Error message:", rc)
#08/03/2024: data from the collar/logs topic is now saved to an array
def on_message(client, userdata, msg):
    topic = msg.topic
    try:
        messages.append(msg.payload.decode("utf8"))
    except Exception as e:
        print(f"Cannot decode data on topic {topic}: {e}")
    userdata['logs'].append(msg.payload.decode())

def on_disconnect(client, userdata, rc):
    print("Disconnected with result code "+str(rc))

client = mqtt.Client(userdata={'logs': []})
client.on_connect = connection
client.on_message = on_message
client.on_disconnect = on_disconnect

client.username_pw_set("SS", "mqttBROKER")
client.connect("broker.hivemq.com", 1883)

#this ensures the code loops forever which is vital for recieving continuous realtime information
client.loop_start()
client.loop_forever()

