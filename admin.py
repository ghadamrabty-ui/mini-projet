
from django.contrib import admin
from .models import Categorie, Ressource


@admin.register(Categorie)
class CategorieAdmin(admin.ModelAdmin):
    list_display = ('id', 'nom', 'description')
    search_fields = ('nom',)
    ordering = ('nom',)


@admin.register(Ressource)
class RessourceAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'titre',
        'type',
        'categorie',
        'date_creation'
    )

    list_filter = ('type', 'categorie', 'date_creation')
    search_fields = ('titre', 'description')
    ordering = ('-date_creation',)
