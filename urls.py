
from django.urls import path
from . import views

urlpatterns = [
    path('', views.accueil, name='accueil'),

    path(
        'ressources/',
        views.liste_ressources,
        name='liste_ressources'
    ),

    path(
        'ressources/ajouter/',
        views.ajouter_ressource,
        name='ajouter_ressource'
    ),

    path(
        'ressources/<int:id>/',
        views.detail_ressource,
        name='detail_ressource'
    ),

    path(
        'ressources/<int:id>/modifier/',
        views.modifier_ressource,
        name='modifier_ressource'
    ),

    path(
        'ressources/<int:id>/supprimer/',
        views.supprimer_ressource,
        name='supprimer_ressource'
    ),

    path(
        'categories/',
        views.liste_categories,
        name='liste_categories'
    ),

    path(
        'categories/<int:id>/ressources/',
        views.ressources_categorie,
        name='ressources_categorie'
    ),
]
