from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.core.exceptions import *
from xmldata.xml_functions import xml_output

def index(request):
    return render(request, 'xmldata/form.html')

def result(request):
    try:
        if request.method == 'POST':
            root_path = request.POST.get('textfield', "")
            html = xml_output(root_path)
            context = {'html' : html}
            return(render(request, 'xmldata/myfile.xml',context,content_type="xml/force-download"))
    except FileNotFoundError:
        return(HttpResponse("Entered Directory does not exist.<br><br><a href='/xmldata/index'>Try Again</a>"))
    except PermissionError:
        return(HttpResponse("You don't have permission to access (some) contents of this Directory.<br><br><a href='/xmldata/index'>Try Again</a"))

def realview(request):
    return(HttpResponse("XML Creator main Page<br><br><a href='/xmldata/index'>Create XML</a>"))


