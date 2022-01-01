from django.shortcuts import render
from django.http import HttpResponse
from request.models import Request
# Create your views here.
from request.serializer import Requestserializer
from rest_framework.views import APIView
from rest_framework.response import Response

def req(request):
    objlist = Request.objects.all()
    context = {
        'objval': objlist,
    }
    return render(request,'request/capprove reject forward to admin.html',context)

def fn(requset):
    objlist = Request.objects.all()
    context = {
        'objval': objlist,
    }
    return render(requset,'request/Aapproverej.html',context)

def gn(requset):
    objlist = Request.objects.all()
    context = {
        'objval': objlist,
    }
    return render(requset,'request/Astatus.html',context)

class Requestview(APIView):
    def get(self,request):
        s=Request.objects.all()
        ser=Requestserializer(s,many=True)
        return Response(ser.data)

    def post(self,request):
        ser=Requestserializer(data=request.data)
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