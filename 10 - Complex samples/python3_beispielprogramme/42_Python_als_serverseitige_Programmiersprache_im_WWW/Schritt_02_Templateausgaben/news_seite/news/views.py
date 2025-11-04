from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404
from django.template import RequestContext, loader

from .models import Meldung, Kommentar


def meldungen(request):
    return render(request, 'news/meldungen.html',
        context={'meldungen' : Meldung.objects.all()})

def meldungen_detail(request, meldungs_id):
    meldung = get_object_or_404(Meldung, id=meldungs_id)
    return render(request, 'news/meldungen_detail.html',
        context={'meldung' : meldung})
