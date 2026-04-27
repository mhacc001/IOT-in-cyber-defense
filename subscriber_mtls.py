import ssl
import paho.mqtt.client as mqtt

try:
    MQTT_CLIENT_ARGS = {"callback_api_version": mqtt.CallbackAPIVersion.VERSION1}
except AttributeError:
    MQTT_CLIENT_ARGS = {}

BROKER = "localhost"
PORT = 8883
TOPIC = "hydroficient/sensors/water"

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("[SUCCESS] Connected to broker")
        client.subscribe(TOPIC)
    else:
        print(f"[ERROR] Connection failed with code {rc}")

def on_message(client, userdata, msg):
    print(f"Received on {msg.topic}: {msg.payload.decode()}")

client = mqtt.Client(client_id="device-002", **MQTT_CLIENT_ARGS)
client.on_connect = on_connect
client.on_message = on_message

client.tls_set(
    ca_certs="certs/ca.pem",
    certfile="certs/device-002.pem",
    keyfile="certs/device-002-key.pem",
    cert_reqs=ssl.CERT_REQUIRED,
    tls_version=ssl.PROTOCOL_TLS_CLIENT
)
client.tls_insecure_set(True)

client.connect(BROKER, PORT, keepalive=60)
client.loop_forever()
