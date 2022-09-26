from django.shortcuts import render

# Create your views here.
def introduce_view(request):
    return render(request, 'introduce/hello.html')