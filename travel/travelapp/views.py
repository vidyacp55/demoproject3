from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
# def demo(request):
#     # name='inmakes'
#     return render(request,"home.html",{'obj':name})
# def about(request):
#     return render(request,'about1.html')
# def contact(request):
#     return HttpResponse("hello contact")
# def addition(request):
#     x=int(request.GET['n1'])
#     y=int(request.GET['n2'])
#     res1=x+y
#     res2=x-y
#     res3=x*y
#     res4=x/y
#     return render(request,"result.html",{'addres':res1,'subres':res2,'mulres':res3,'divres':res4})

def demo(request):
    return render(request,"index.html")