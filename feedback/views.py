from django.shortcuts import render
from django.http import HttpResponse
from feedback.models import Feedback
# Create your views here.
from feedback.serializer import Feedbackserializer
from rest_framework.views import APIView
from rest_framework.response import Response


def feedback(request):
    objlist=Feedback.objects.all()
    context={
        'objval':objlist,
    }
    return render(request,'feedback/Aviewfeed.html', context)

class Feedbackview(APIView):
    def get(self,request):
        s=Feedback.objects.all()
        ser=Feedbackserializer(s,many=True)
        return Response(ser.data)

    def post(self,request):
        ser=Feedbackserializer(data=request.data)
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