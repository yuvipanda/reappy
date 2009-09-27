# Create your views here.
from reappy import Application
from django.http import HttpResponse


def ILovePyConHandler(x):
    r = HttpResponse()
    r["Content-Type"]="text/html"
    r.content = x
    return r


def get_search_result(request):
    a = Application("#pyconindia",
                  [(r'.*', ILovePyConHandler)])
    return a.run()