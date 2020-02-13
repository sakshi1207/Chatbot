from django.shortcuts import *
from django.views.decorators.csrf import *
import pandas
import random

def chatbot(request):
    return render(request,"chatbot.html")

def messageReply(request):
    print("in Message reply")
    msg=request.GET['msg']
    df = pandas.read_json('mychatdata')
    print(df)

    df1 = df["response"][df["request"] == msg]
    response =df1
    print(df1)

    l = len(response)
    if len == 0:
        return HttpResponse('sorry didn understand u')
    else:
        response = list(response)
        ran = int(random.uniform(0, len(response)))
    return HttpResponse(response[ran])
