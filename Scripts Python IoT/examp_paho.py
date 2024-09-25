#Instalar previamente...
#PAHO  pip install paho-mqtt

import time
import random
import paho.mqtt.client as mqtt

#1) Definición de variables 
server = "test.mosquitto.org"
port = 1883
keepAliveTime = 60
topicPublish = "sub/MarcoEsp32" #topico para publicar o enviar datos
topicSubscribe = "pub/MarcoEsp32" #topico para subscribirse o recibir datos

# 1) Función para Conectarse a Broker MQTT
def on_connect(client, userdata, flags, reason_code, properties):
    print(f"\r\nEstado de Conexión  a Broker MQTT: {reason_code}")
    client.subscribe(topicSubscribe) # Subscribirse a un Tópic

# 2) Función Callback para recepcinar mensajes MQTT una vez subscrito
def on_message(client, userdata, msg):
    #Imprimir el tópico de donde se recepciona mensaje y el mensaje (payload)
    print(msg.topic + " " + str(msg.payload))

# 3) PROGRAMA PRINCIPAL
mqttc = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
mqttc.on_connect = on_connect
mqttc.on_message = on_message
mqttc.connect(server, port, keepAliveTime)   #Función para conectarse a un Broker MQTT
mqttc.loop_start()  #Función de tipo Bucle para mantener la coexión MQTT
print("OKI")
while True:
    numero_decimal_aleatorio = random.uniform(0, 1)
    payload = int(numero_decimal_aleatorio*10)
    print(payload)
    mqttc.publish(topicPublish, payload )
    time.sleep(3)
    