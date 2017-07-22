from django.shortcuts import render
from django.http import HttpResponse
import json

import Serial

# Create your views here.
def index(request):
    return render(request, "SerialRead/index.html");

def getJson(request):
    data = {'data': '', 'success': True, 'msg': ''}
    if ('p' in request.GET):
        param = request.GET['p']
        if (param == 'list'):
            list = Serial.getList()
            if (len(list) <= 0):
                data['success'] = False
                data['msg'] = 'can\'t find serial port'
            else:
                data['data'] = list
        if ('c' in request.GET):
            comName = param.encode('utf-8')
            Serial.closeCom(comName)
        if ('b' in request.GET):
            comName = param.encode('utf-8')
            baud = request.GET['b']
            serialData = Serial.getComData(comName, baud)
            if (len(serialData) <= 0):
                data['success'] = False
            else:
                print serialData
                data['data'] = serialData
    return HttpResponse(json.dumps(data))
