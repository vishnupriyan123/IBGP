from django.shortcuts import render
from django.http import HttpResponse
from info.models import Info

from info.serializer import Infoserializer
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.
def info(request):
    if request.method=="POST":
        obj=Info()
        obj.info = request.POST.get("info")
        obj.save()
    return render(request,'info/cadditional info.html')

class Infoview(APIView):
    def get(self,request):
        s=Info.objects.all()
        ser=Infoserializer(s,many=True)
        return Response(ser.data)

    def post(self,request):
        ser=Infoserializer(data=request.data)
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