from django.shortcuts import render
# from django.http import HttpResponse
# Create your views here.


# def home(request):
#     return HttpResponse("<h1>Hello EveryOne</h1>")
def home(request):
    return render(request, 'resume/home.html')


def about(request):
    return render(request, 'resume/about.html')
