from django.shortcuts import render
from django.http import HttpResponse
from transfer.models import Transfer

from transfer.serializer import Transferserializer
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.
from transfer.serializer import Transferserializer
from rest_framework.views import APIView
from rest_framework.response import Response
def trans(request):
    if request.method=="POST":
        obj=Transfer()
        obj.accno=request.POST.get("accno")
        obj.tof=request.POST.get("afundt")
        obj.tid=request.POST.get("aID")
        obj.amt=request.POST.get("aamt")
        obj.branch=request.POST.get("abranch")
        obj.bname=request.POST.get("abname")
        obj.save()

    return render(request,'transfer/Atransfer Fund.html')


class Transferview(APIView):
    def get(self,request):
        s=Transfer.objects.all()
        ser=Transferserializer(s,many=True)
        return Response(ser.data)

    def post(self,request):
        ser=Transferserializer(data=request.data)
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