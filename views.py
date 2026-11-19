
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.db.models import Q

from .models import Categorie, Ressource
from .forms import RessourceForm


def accueil(request):
    context = {
        'total_ressources': Ressource.objects.count(),
        'total_categories': Categorie.objects.count(),
    }

    return render(request, 'ressources/accueil.html', context)

    return render(request, 'ressources/accueil.html', context)


def liste_ressources(request):
    ressources = Ressource.objects.select_related(
        'categorie'
    ).all()

    recherche = request.GET.get('q', '').strip()
    categorie_id = request.GET.get('categorie', '')

    if recherche:
        ressources = ressources.filter(
            Q(titre__icontains=recherche) |
            Q(description__icontains=recherche) |
            Q(type__icontains=recherche)
        )

    if categorie_id:
        ressources = ressources.filter(
            categorie_id=categorie_id
        )

    categories = Categorie.objects.all()

    context = {
        'ressources': ressources,
        'categories': categories,
        'recherche': recherche,
        'categorie_selectionnee': categorie_id,
    }

    return render(
        request,
        'ressources/liste_ressources.html',
        context
    )


def detail_ressource(request, id):
    ressource = get_object_or_404(Ressource, id=id)

    return render(
        request,
        'ressources/detail_ressource.html',
        {'ressource': ressource}
    )


def ajouter_ressource(request):
    if request.method == 'POST':
        form = RessourceForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(
                request,
                'Ressource ajoutée avec succès !'
            )
            return redirect('liste_ressources')
    else:
        form = RessourceForm()

    return render(
        request,
        'ressources/formulaire_ressource.html',
        {'form': form, 'titre': 'Ajouter une ressource'}
    )


def modifier_ressource(request, id):
    ressource = get_object_or_404(Ressource, id=id)

    if request.method == 'POST':
        form = RessourceForm(
            request.POST,
            instance=ressource
        )

        if form.is_valid():
            form.save()
            messages.success(
                request,
                'Ressource modifiée avec succès !'
            )
            return redirect(
                'detail_ressource',
                id=ressource.id
            )
    else:
        form = RessourceForm(instance=ressource)

    return render(
        request,
        'ressources/formulaire_ressource.html',
        {'form': form, 'titre': 'Modifier une ressource'}
    )


def supprimer_ressource(request, id):
    ressource = get_object_or_404(Ressource, id=id)

    if request.method == 'POST':
        ressource.delete()
        messages.success(
            request,
            'Ressource supprimée avec succès !'
        )
        return redirect('liste_ressources')

    return render(
        request,
        'ressources/supprimer_ressource.html',
        {'ressource': ressource}
    )


def liste_categories(request):
    categories = Categorie.objects.all()

    return render(
        request,
        'ressources/liste_categories.html',
        {'categories': categories}
    )


def ressources_categorie(request, id):
    categorie = get_object_or_404(Categorie, id=id)

    ressources = Ressource.objects.filter(
        categorie=categorie
    )

    return render(
        request,
        'ressources/ressources_categorie.html',
        {
            'categorie': categorie,
            'ressources': ressources
        }
    )
