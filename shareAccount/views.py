from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'shareAccount/index.html')

def add_accounShare(request):
    return render(request,'shareAccount/add-accountShare.html')

def view_shareSettings(request):
    return render(request,'shareAccount/view-shareSettings.html')

def add_shareSettings(request):
    return render(request,'shareAccount/add-shareSettings.html')