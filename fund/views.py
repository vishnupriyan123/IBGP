from django.shortcuts import render
from django.http import HttpResponse
from fund.models import Fund
# Create your views here.
from fund.serializer import Fundserializer
from rest_framework.views import APIView
from rest_framework.response import Response
def fund(request):
    if request.method == "POST":
        obj = Fund()
        obj.amt = request.POST.get("aamount")
        obj.validity = request.POST.get("aval")

        obj.save()

    return render(request,'fund/fund.html')

def fn(requset):
    objlist = Fund.objects.all()
    context = {
        'objval': objlist,
    }
    return render(requset,'fund/Aadd type fund.html',context)
class Fundview(APIView):
    def get(self,request):
        s=Fund.objects.all()
        ser=Fundserializer(s,many=True)
        return Response(ser.data)

    def post(self,request):
        ser=Fundserializer(data=request.data)
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