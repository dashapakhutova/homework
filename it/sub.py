import paho.mqtt.client as mqtt_client
import random
import time
import serial as sr

UNIQUE_ID = 999
port = "COM4"
ser = sr.Serial(port, 9600)
min_ = 0
max_ = 0
stack = []
stack_len = 3



### функция включения светодиода по автоматическому порогу
def mode_porog(data, topic):
    global min_
    global max_
    if("/porog-min" in topic):
        min_ = data
    elif("/porog-max" in topic):
        max_ = data
    else:
        mean = (min_+max_)/2.
        if (data>=mean):
            ser.write("1".encode())
        else:
            ser.write("0".encode())
        #print("mean = ", mean, "; data = ", data, sep="")
        
### функция включения светодиода при падении значений датчика
def mode_fall(data):
    global stack
    global stack_len
    stack.append(data)
    if len(stack) > stack_len:
        stack.pop(0)
    if(len(stack)>1):
        dw_cnt = 0
        up_cnt = 0
        for i in range(1, len(stack)):
            if (stack[i] < stack[i-1]):
                dw_cnt += 1
        for i in range(1, len(stack)):
            if (stack[i] >= stack[i-1]):
                up_cnt += 1
        if(dw_cnt == len(stack)-1):
            ser.write("1".encode())
        elif(up_cnt == len(stack)-1):
            ser.write("0".encode())

### тестовая функция для записи на ардуино
def write(data):       
    print(f"recieved command {data}")
    if (data == "1"):
        ser.write("1".encode())
        time.sleep(2)
    if (data =="0"):
        ser.write("0".encode())
        time.sleep(2)

def on_message(client, data, message):
    data = float(message.payload.decode("utf-8"))
    topic = message.topic
    if ("/fall" in topic):
        mode_fall(data)
    elif any(i in topic for i in ["/porog-min", "/porog-max", "/porog-value"]):
        mode_porog(data, topic)
    elif any(i in topic for i in ["/instant", "/average", "/stream"]):
        print(f"Topic: {topic}")
        print(f"Message: {data}")
        print()
    '''
    print(f"Topic: {topic}")
    print(f"Message: {data}")
    print()
    '''
    return data
    


broker = "broker.emqx.io"
client = mqtt_client.Client(f"lab_{random.randint(10000, 99999)}")
client.on_message = on_message

try:
    client.connect(broker)
except Exception:
    print("Failed to connect")
    ser.close()
    exit()    

client.loop_start()
print("Connected")    

client.subscribe(f'lab/{UNIQUE_ID}/photo/instant') #задание 1
client.subscribe(f'lab/{UNIQUE_ID}/photo/average') #задание 2
client.subscribe(f'lab/{UNIQUE_ID}/photo/stream') #задание 3
client.subscribe(f'lab/{UNIQUE_ID}/photo/fall') #задание 4

#задание 5
client.subscribe(f'lab/{UNIQUE_ID}/photo/porog-max')
client.subscribe(f'lab/{UNIQUE_ID}/photo/porog-min')
client.subscribe(f'lab/{UNIQUE_ID}/photo/porog-value')

time.sleep(600)
client.disconnect()
client.loop_stop()
print("Stop communication")
