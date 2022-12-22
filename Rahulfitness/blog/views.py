from django.shortcuts import render,HttpResponse

# Create your views here.

def home(request):
    return render(request,'home.html')

def All_about_Abs(request):
    return render(request,'blog/All about abs.html')

def fat_loss(request,slug):
    return render(request,'/fatloss.html')  

def Nutrition(request,slug):
    return render(request,'blog/Nutrition.html')    

def Supplements(request,slug):
    return render(request,'blog/Supplements.html')    

def Training(request,slug):
    return render(request,'blog/Training.html')    