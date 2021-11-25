

import random
import time

import paho.mqtt.client as mqtt

client=mqtt.Client()


while True:
    client.connect('broker.hivemq.com',1883)
    print ('Broker Connected')
    h=random.randint(40,100)
    t=random.randint(20,35)
    k='#,'+str(t)+','+str(h)+'~'
    print(k)
    client.publish('nitw/kits',k)
    time.sleep(1)
