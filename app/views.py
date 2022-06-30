from django.shortcuts import render

# Create your views here.
def mouni(request):
    return render(request,'parent.html')
def latha(request):
    return render(request,'child.html')
