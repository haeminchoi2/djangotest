from django.shortcuts import render, redirect
from accesslog.models import AccessLog

# Create your views here.

def accesslog(request):
    if request.method == "GET":
        url_address = request.get_host()
        template_name = request.template_name
        sparta_log = AccessLog()
        sparta_log.location = f"{url_address}, {template_name}"
        sparta_log.save()
        return redirect(f'/{url_address}')