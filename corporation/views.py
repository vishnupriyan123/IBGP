from django.shortcuts import render
from django.http import HttpResponse
from corporation.models import Corporation

from corporation.serializer import Corporationserializer
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.
def corporation(request):
    if request.method == "POST":
        obj = Corporation()
        obj.name = request.POST.get("aname")
        obj.address = request.POST.get("aaddress")
        obj.phone = request.POST.get("aphone")
        obj.pin = request.POST.get("apin")
        obj.email = request.POST.get("aemail")
        obj.save()

    return render(request,'corporation/ACorp Level Reg.html')

def fn(requset):
    objlist = Corporation.objects.all()
    context = {
        'objval': objlist,
    }
    return render(requset,'corporation/AviewList.html',context)
def up(request,cid):
    if request.method=="POST":
        # tp=str(request.session['ex'])
        #
        # #return getvalues(request,cid)
        obj=Corporation.objects.get(cid=cid)
        obj.name = request.POST.get("aname")
        obj.address = request.POST.get("aaddress")
        obj.phone = request.POST.get("aphone")
        obj.pin = request.POST.get("apin")
        obj.email = request.POST.get("aemail")
        obj.save()
        return fn(request)

    else:
        objlist = Corporation.objects.get(cid=cid)
        context = {
            'objval': objlist,
        }
        return render(request,'corporation/Update.html',context)

def de(requset,cid):
    objlist = Corporation.objects.get(cid=cid)
    objlist . delete()
    return fn(requset)


class Corporationview(APIView):
    def get(self,request):
        s=Corporation.objects.all()
        ser=Corporationserializer(s,many=True)
        return Response(ser.data)

    def post(self,request):
        ser=Corporationserializer(data=request.data)
        if ser.is_valid():
           ser.save()
        return HttpResponse("ok")

            # obj=Feedback()
            # obj.uid=request.data["uid"]
            # obj.feedbk = request.data["feedbk"]
            # obj.date = request.data["date"]
            # obj.rating = request.data["rating"]
            # obj.save()
            # return HttpResponse(request.data["uid"])