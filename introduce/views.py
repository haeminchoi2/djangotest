from django.shortcuts import render
from accesslog.views import accesslog
# Create your views here.
def introduce(request):
    accesslog(request)
    return render(request, 'introduce/hello.html')