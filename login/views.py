from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from login.models import Login
from login.serializer import Loginserializer
from rest_framework.views import APIView
from rest_framework.response import Response

def log(request):
    uname = request.POST.get("usname")
    passw = request.POST.get("pass")

    obj = Login.objects.filter(username=uname, password=passw)
    tp = ""
    for ob in obj:
        tp = ob.type
        uid = ob.id
        if tp == "admin":
            request.session['uid'] = uid

            return render(request, 'login/adminhome.html')

        else:
            return render(request, 'login/login.html')
    return render(request,'login/login.html')


class Loginview(APIView):
    def get(self,request):
        s=Login.objects.all()
        ser=Loginserializer(s,many=True)
        return Response(ser.data)

    def post(self,request):
        def post(self, request):
            # ser=viewloginserializer(data=request.data)
            s = Login.objects.filter(username=request.data["username"], password=request.data["password"])
            ser = Loginserializer(s, many=True)
            return Response(ser.data)