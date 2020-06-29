import paho.mqtt.client as mqtt
import inspect

host = "localhost"
nclienteB = "Cliente 2"
topico = "casa/#"

def on_message_esclavo(client, userdata, message):
    print("Mensaje Recibido " ,str(message.payload.decode("utf-8")))
    print("Mensaje Topico=",message.topic)
    print("Mensaje qos=",message.qos)
    print("Mensaje retain flag = ",message.retain)
    if message.payload.decode("utf-8") == " ":
        print("Hubo un error")

def on_disconnect(client, userdata, rc):
    if rc == 1:
        print("Error en la conexión")
        cliente.loop_stop()
    
cliente = mqtt.Client(client_id=nclienteB, clean_session=True)

cliente.on_message = on_message_esclavo
cliente.on_disconnect = on_disconnect

cliente.connect(host)
cliente.subscribe(topico,qos=1)

cliente.loop_start()

#cliente.loop_stop()
#cliente.disconnect()