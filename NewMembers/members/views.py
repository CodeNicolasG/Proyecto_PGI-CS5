from django.shortcuts import render

def IndexView(request):
    return render(request, 'newmembers.html')
