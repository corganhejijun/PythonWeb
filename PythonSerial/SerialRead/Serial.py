import serial
import serial.tools.list_ports
from django.conf import settings
from multiprocessing import Queue
import threading

def getList():
    ports = ['COM%s' % (i + 1) for i in range(256)]
    port_list = []
    for port in ports:
        try:
            s = serial.Serial(port)
            s.close()
            port_list.append(port)
        except (OSError, serial.SerialException):
            pass
    for com in settings.COM:
        if (com['name'] not in port_list):
            port_list.append(com['name'])
    print(port_list)
    return port_list

def getComData(name, baudrate):
    com = openCom(name, baudrate)
    if (com['queue'].empty()):
        return ''
    result = ''
    maxCount = 100
    while True:
        maxCount -= 1
        result += com['queue'].get_nowait()
        if (maxCount <= 0 or com['queue'].empty()):
            break;
    return result

def readCom(com, queue):
    while True:
        data = com.read()
        if (len(data) > 0):
            queue.put(data)

def openCom(name, baudrate):
    for com in settings.COM:
        if (name == com['name']):
            return com
    print('open ' + name + ' success')
    com = serial.Serial(port=name, baudrate=baudrate)
    q = Queue()
    th = threading.Thread(target=readCom, args=(com, q))
    item = {
        'name': name,
        'com': com,
        'thread': th,
        'queue': q
    }
    settings.COM.append(item)
    th.start()
    return item

def closeCom(name):
    for com in settings.COM:
        if (name == com['name']):
            print('close ' + name + ' success')
            com['com'].close()
            com['thread'].join()
            settings.COM.remove(com)
            return;
