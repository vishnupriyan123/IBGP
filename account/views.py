from django.shortcuts import render
from django.http import HttpResponse
from account.models import Account


from account.serializer import Accountserializer
from rest_framework.views import APIView
from rest_framework.response import Response


# Create your views here.
def account(request):
    if request.method=="POST":
        obj=Account()
        obj.accno=request.POST.get("accno")

        obj.save()


    return render(request,'account/Atransfer Fund.html')




class Accountview(APIView):
    def get(self,request):
        s=Account.objects.all()
        ser=Accountserializer(s,many=True)
        return Response(ser.data)

    def post(self,request):
        ser=Accountserializer(data=request.data)
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