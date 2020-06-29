import paho.mqtt.client as mqtt
import inspect
import random
import time
import numpy as np
from datetime import datetime

host = "localhost"
nclienteA = "Cliente 1"
topico = "casa/habitacion/luz"
i=1

def on_message_maestro(client, userdata, message):
    print("Mensaje Enviado " ,str(message.payload.decode("utf-8")))
    print("Mensaje Topico=",message.topic)
    print("Mensaje qos=",message.qos)
    print("Mensaje retain flag = ",message.retain)
    
def on_publish(client, userdata, mid):
    print("Esto es una prueba desde Cliente 1")
    print("mid: "+str(mid))
    print("cliente: "+str(cliente))

def on_disconnect(client, userdata, rc):
    if rc == 0:
        print("Error en la conexión")
        cliente.loop_stop()

#1. Crear un cliente maestro (A) y esclavo(B) 
cliente = mqtt.Client(client_id=nclienteA, clean_session=True)
#2. Asociar callbacks
cliente.on_message = on_message_maestro
cliente.on_publish = on_publish
cliente.on_disconnect = on_disconnect

#3. Conectar el cliente al broker
cliente.connect(host)
cliente.subscribe(topico,qos=1)
#4 iniciar loop
cliente.loop_start()

start_time = datetime.now()
while i==1:
    num = np.random.random()
    cliente.publish(topic=topico, payload=(num), qos=1, retain=True)
    time.sleep(5)
    timedelta=datetime.now()-start_time
    if timedelta.seconds>=30:
        break

#cliente.publish(topic=topico, payload = "Esto es una prueba2 desde Cliente 1", qos=1, retain=True)

#cliente.loop_stop()
#cliente.disconnect()