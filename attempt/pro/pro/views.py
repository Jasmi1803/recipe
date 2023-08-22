from django.shortcuts import render
from django.http import HttpResponse
def home(request):
    return render(request,'index.html')
def home1(request):
    return render(request,'about.html')
def home2(request):
    if request.method=="POST":
        contact=Contact()
        name=request.Post.get('name')
        email=request.Post.get('email')
        message=request.POST.get('message')
        contact.name=name
        contact.email=email
        contact.message=message
        contact.save()
        return HttpResponse("<h1>Thanks for messaging us</h1>")
    return render(request,'contact.html')
    