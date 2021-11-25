import paho.mqtt.client as mqtt
import pandas as pd

client=mqtt.Client()
client.connect('broker.hivemq.com',1883)
print ('Broker Connected')

client.subscribe('nitw/kits')
label=0
data=[]
count=0
def on_message(client,userdata,msg):
  global label,count
  k=msg.payload.decode('utf-8')
  k=k.split(',')
  temp=float(k[1])
  hum=float(k[-1][:-1])
  if (temp<25 and temp>=20):
    label=1
  elif (temp<30 and temp>=25):
    label=2
  elif (temp<35 and temp>=30):
    label=3
  else:
    label=0
  #print(temp,hum,label)
  dummy=[]
  dummy.append(temp)
  dummy.append(hum)
  dummy.append(label)
  data.append(dummy)
  count+=1
  print(count)
  if count==200:
    df=pd.DataFrame(data)
    df.to_csv('iot.csv')

client.on_message=on_message
client.loop_forever()
