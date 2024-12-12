from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'projecthe/home.html')

def about(request):
    return render(request, 'projecthe/about.html')

def codeurl(request):
    return render(request, 'projecthe/codeurl.html')

def more(request):
    return render(request, 'projecthe/more.html')
