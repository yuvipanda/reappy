# Create your views here.
from models import Opinion
from django.http import HttpResponse
from django.shortcuts import render_to_response


def ILovePyConHandler(x):
    r = HttpResponse()
    r["Content-Type"]="text/html"
    r.content = x
    return r


def get_search_result(request):
    positive_ops = Opinion.objects.filter(opinion="R")
    negative_ops = Opinion.objects.filter(opinion="S")
    return render_to_response("demo_app/base.html",{"negative_tweets":negative_ops,"positive_tweets":positive_ops})
