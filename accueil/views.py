from django.shortcuts import render

def home(request):
    nom = None
    if request.method == "POST":
        nom = request.POST.get('nom')
    return render(request, 'accueil/home.html', {'nom': nom})
