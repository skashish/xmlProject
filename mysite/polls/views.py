from django.http  import HttpResponse

def index(request):
    return HttpResponse("<body align = 'center'><h3><u>XML Generator</u></h3></body>")
