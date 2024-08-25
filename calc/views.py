from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, 'home.html', {'name': 'Love'})


def add(request):
    val1 = request.POST['num1']
    val2 = request.POST['num2']
    print(type(val1))
    result = int(val1) + int(val2)
    print(result)
    return render(request, "result.html", {'result': result})