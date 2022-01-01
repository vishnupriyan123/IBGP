from django.shortcuts import render
from django.http import HttpResponse
from register.models import Register

from register.serializer import Registerserializer
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.
def reg(request):
    if request.method == "POST":
        obj = Register()
        obj.name = request.POST.get("aname")
        obj.address = request.POST.get("aaddress")
        obj.phone = request.POST.get("aphone")
        obj.pin = request.POST.get("apin")
        obj.email = request.POST.get("aemail")
        obj.save()

    return render(request,'register/ACorp Level Reg.html')

def fn(requset):
    objlist = Register.objects.all()
    context = {
        'objval': objlist,
    }
    return render(requset,'register/AviewList.html',context)

class Registerview(APIView):
    def get(self,request):
        s=Register.objects.all()
        ser=Registerserializer(s,many=True)
        return Response(ser.data)

    def post(self,request):
        ser=Registerserializer(data=request.data)
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
