from django.contrib import admin
from mydc.models import *


class AyantDroitAdmin(admin.ModelAdmin):
    list_display = ('nom', 'diminutif')
    ordering = ('nom',)
    search_fields = ('nom', 'diminutif')


class DroitAdmin(admin.ModelAdmin):
    list_display = ('nom',)
    ordering = ('nom',)
    search_fields = ('nom',)


class FilmAdmin(admin.ModelAdmin):

    ordering = ('titreVf',)
    search_fields = ('titreVf',)


class SerieAdmin(admin.ModelAdmin):

    ordering = ('titreVf',)
    search_fields = ('titreVf',)


class CatalogueAdmin(admin.ModelAdmin):

    ordering = ('nom',)
    search_fields = ('nom',)

# Register your models here.
admin.site.register(AyantDroit, AyantDroitAdmin)
admin.site.register(Droit, DroitAdmin)
admin.site.register(Genre, DroitAdmin)
admin.site.register(Langue, DroitAdmin)
admin.site.register(Rating, DroitAdmin)
admin.site.register(Categorie, DroitAdmin)
admin.site.register(Film, FilmAdmin)
admin.site.register(Serie, SerieAdmin)
admin.site.register(Catalogue, CatalogueAdmin)

