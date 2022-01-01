from django.shortcuts import render
from django.http import HttpResponse
from funduser.models import Fundtouser
# Create your views here.
from funduser.serializer import Fundtouserserializer
from rest_framework.views import APIView
from rest_framework.response import Response

def fuser(request):
    if request.method=="POST":
        obj=Fundtouser()
        obj.username=request.POST.get("uname")
        obj.accno=request.POST.get("pass")
        obj.save()

    #return HttpResponse("hellow")
    return render(request,'funduser/cproceedfundtouser.html')

class Fundtouserview(APIView):
    def get(self,request):
        s=Fundtouser.objects.all()
        ser=Fundtouserserializer(s,many=True)
        return Response(ser.data)

    def post(self,request):
        ser=Fundtouserserializer(data=request.data)
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