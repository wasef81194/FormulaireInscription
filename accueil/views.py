from django.shortcuts import render, redirect
from .forms import VisiteurForm

def home(request):
    form = VisiteurForm()
    nom = None
    if request.method == "POST":
        form = VisiteurForm(request.POST)
        if form.is_valid():
            form.save()  # Enregistre en BDD !
            nom = form.cleaned_data['nom']
            return render(request, 'accueil/home.html', {'nom': nom, 'form': VisiteurForm()})
    return render(request, 'accueil/home.html', {'form': form, 'nom': nom})
