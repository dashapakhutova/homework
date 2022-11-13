from operator import ne
import serial.tools.list_ports
import serial as sr
import paho.mqtt.client as mqtt_client
import time, random
import numpy as np

port="COM13"
broker = "broker.emqx.io"
my_id = 999
duration = 20
queue = []
avg_value = 0
need_input = True
max_val = 0
min_val = 0
client = mqtt_client.Client(f'lab_{random.randint(10000, 999999)}')
client.connect(broker)
arduino = sr.Serial(port=port, baudrate=9600)



def map(value, in_min, in_max, out_min, out_max):
    return (value - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

def help_note():
    print(
"""List of commands:
0 - Exit
1 - Send current value
2 - Send mean value
3 - Stream (20 seconds)
4 - Check if values fall (20 seconds)
5 - Stream min, max and current values (20 seconds)
6 - Print list of commands"""
    )



help_note()
while True:
    if need_input:
        command = int(input("Input: "))
    if (command == 6):
        help_note()
        continue
    elif (command == 0):
        arduino.close()
        client.disconnect()
        break
    
    arduino.write(np.array([1], dtype='uint8').tobytes())
    time.sleep(0.01)
    while arduino.inWaiting() < 2:
        pass

    response = arduino.read(2)  # Прочитали
    response = [int(byte_) for byte_ in response]   # массив байт в массив int8
    response = (response[0] << 8 & 0xFF00) + (response[1] & 0xFF)   # Взяли число
    response = map(response, 0, 1024, 0, 100)   # Смена диапазона
    queue.append(response)  # Фиксируем новое значение
    avg_value += response
    if len(queue) >= 100:
        avg_value -= queue.pop(0)

    #1 отправить одно значение
    if command == 1:
        client.publish(f'lab/{my_id}/photo/instant', response) 
    #2 отправить среднее значение
    elif command == 2:
        client.publish(f'lab/{my_id}/photo/average', avg_value/len(queue)) 
    #3 потоковая передача
    elif command == 3:
        if need_input:
            timer_start = time.time()
            need_input = False
        if time.time() - timer_start >= duration:
            need_input = True
        client.publish(f'lab/{my_id}/photo/stream', response)
    #4 нахождение убывающих и возрастающих участков рядов измерений
    elif command == 4:
        if need_input:
            timer_start = time.time()
            need_input = False
        if time.time() - timer_start >= duration:
            need_input = True
        client.publish(f'lab/{my_id}/photo/fall', response)
    #5 включение/выключение по порогу освещенности
    elif command == 5:
        if need_input:
            timer_start = time.time()
            need_input = False
        if time.time() - timer_start >= duration:
            need_input = True
        client.publish(f'lab/{my_id}/photo/porog-max', max(queue))
        client.publish(f'lab/{my_id}/photo/porog-min', min(queue))
        client.publish(f'lab/{my_id}/photo/porog-value', response)
