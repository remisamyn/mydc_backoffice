from django.contrib.auth.decorators import login_required
from django.core import paginator
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, render_to_response
from django.template.context import RequestContext
from mydc.models import Film, Serie, Catalogue


@login_required
def home(request):
    return render(request, "home.html")


@login_required
def films(request):
    films = Film.objects.all().order_by('titreVf')
    paginator = Paginator(films, 25)
    page = request.GET.get('page')
    try:
        films = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        films = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        films = paginator.page(paginator.num_pages)
    c = {'films': films}
    return render(request, "films/gerer_films.html", c)


@login_required
def film(request,id):
    film = Film.objects.get(id=id)
    c = {'film': film}
    return render(request, "films/film.html", c)


@login_required
def series(request):
    s = Serie.objects.all()
    c = {'series': s}
    return render(request, "films/liste_series.html", c)


@login_required
def catalogues(request):
    catalogues = Catalogue.objects.all()
    c = {'catalogues': catalogues}
    return render(request, "films/liste_catalogues.html", c)


@login_required
def catalogue(request,id):
    catalogue = Catalogue.objects.get(id=id)
    c = {'catalogue': catalogue}
    return render(request, "films/catalogue.html", c)


