from django.shortcuts import render
from django.http import HttpResponse
from users.models import Users
# Create your views here.
from users.serializer import Usersserializer
from rest_framework.views import APIView
from rest_framework.response import Response
def users(request):
    objlist = Users.objects.all()
    context = {
        'objval': objlist,
    }
    return render(request, 'users/capprove reject forward to admin.html',context)

def fn(requset):
    objlist = Users.objects.all()
    context = {
        'objval': objlist,
    }
    return render(requset,'request/Aapproverej.html',context)


class Userview(APIView):
    def get(self,request):
        s=Users.objects.all()
        ser=Usersserializer(s,many=True)
        return Response(ser.data)

    def post(self,request):
        ser=Usersserializer(data=request.data)
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