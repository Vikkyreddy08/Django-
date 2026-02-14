from django.shortcuts import render
from django.http import HttpResponse,JsonResponse

def view1(req):
    return HttpResponse("This is view1")

def view2(req):
    return JsonResponse({"mesg":"vikky","error":"no error"})

# Create your views here.

# dynamic
def personalInfo(req):
    name=req.GET.get("name")
    age=req.GET.get("age")
    city=req.GET.get("city")
    role=req.GET.get("role")
    info={"name":name,"age":age,"city":city,"role":role}
    return JsonResponse({"data":info})


def showtime(req):
    movie=req.GET.get("entern","RRR")
    time=req.GET.get("show",3)
    cost=req.GET.get("tiket",300)
    total=req.GET.get("occupying",5)
    info=({"entern":movie,"show":time,"tiket":cost,"occupying":total})
    return JsonResponse({"status":"sucess","success":"showtime","data":info})

    
