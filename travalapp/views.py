from django.shortcuts import render
from django.http import HttpResponse
from .models import place
from .models import vlog


# Create your views here.
def fun(request):
    obj = vlog.objects.all()
    plc = place.objects.all()

    return render(request, "index.html", {"v": obj,"results": plc})



# def addition(request):
#     num1 = int(request.POST["num1"])
#     num2 = int(request.POST["num2"])
#     num3 = num1 + num2
#     return render(request, "result.html", {"add": num3})
