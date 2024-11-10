from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Resp_Insp, Resp_Prod, Jury, Realisateur, Producteur, Documentaire
from datetime import datetime


personnage = None
conn = 0
error = 0
successful_add = False


# Create your views here.
def connexion(request):
    global error
    error = 0
    return render(request, "DAT/connexion.html")

# Connexion resp_insp
def connexion_resp_insp(request):
    print(error)
    return render(request, "DAT/connexion_resp_insp.html", {"error" : error})

def traitement_connexion_resp_insp(request):
    if request.method == 'POST':
        global error
        email = request.POST.get('email')
        password = request.POST.get('password')
        print(email,password)
        objet = Resp_Insp.objects.filter(email=email, password = password )
        if objet:
            error = 0
            global personnage
            global conn
            personnage = objet[0]
            conn = 1
            print(personnage.nom)
            return redirect('resp_insp_voir_doc')
        else: 
          error = 1
          return redirect('connexion_resp_insp')
    print("GET",error)
    return render(request, "DAT/connexion_resp_insp.html")

# Connexion resp_Prod
def connexion_resp_prod(request):
    print(error)
    return render(request, "DAT/connexion_resp_prod.html", {"error" : error})

def traitement_connexion_resp_prod(request):
    print("POST OU GET")
    if request.method == 'POST':
        global error
        email = request.POST.get('email')
        password = request.POST.get('password')
        print(email,password)
        objet = Resp_Prod.objects.filter(email=email, password = password )
        if objet:
            error = 0
            return HttpResponse("connexion réussie")
        else: 
          error = 1
          return redirect('connexion_resp_prod')
    print("GET",error)
    return render(request, "DAT/connexion_resp_prod.html")

# Connexion Jury
def connexion_jury(request):
    print(error)
    return render(request, "DAT/connexion_jury.html", {"error" : error})

def traitement_connexion_jury(request):
    print("POST OU GET")
    if request.method == 'POST':
        global error
        email = request.POST.get('email')
        password = request.POST.get('password')
        print(email,password)
        objet = Resp_Prod.objects.filter(email=email, password = password )
        if objet:
            error = 0
            return HttpResponse("connexion réussie")
        else: 
          error = 1
          return redirect('connexion_jury')
    print("GET",error)
    return render(request, "DAT/connexion_jury.html")


#RESPONSABLE D'INSPECTION
def resp_insp_voir_doc(request):
    if conn == 1 : 
        global personnage
        global successful_add
        successful_add = False
        all_docs = Documentaire.objects.all()
        return render(request, "DAT/resp_insp_voir_doc.html", {"personnage" : personnage, "documentaires" : all_docs})
    else : 
        return redirect('connexion')

def resp_insp_gerer_doc(request):
    if conn == 1 : 
        global personnage
        global successful_add
        successful_add = False
        all_docs = Documentaire.objects.all()
        return render(request, "DAT/resp_insp_gerer_doc.html", {"personnage" : personnage, "documentaires" : all_docs})
    else :
        return redirect('connexion')
    

def resp_insp_gerer_real(request):
    if conn == 1 : 
        global personnage
        global successful_add
        successful_add = False
        all_reals = Realisateur.objects.all()
        return render(request, "DAT/resp_insp_gerer_real.html", {"personnage" : personnage, "realisateurs" : all_reals})
    else :
        return redirect('connexion')

def resp_insp_gerer_prod(request):
    if conn == 1 : 
        global personnage
        global successful_add
        successful_add = False
        all_prods = Producteur.objects.all()
        return render(request, "DAT/resp_insp_gerer_prod.html", {"personnage" : personnage, "producteurs" : all_prods})
    else :
        return redirect('connexion')

def resp_insp_enregistrer_doc(request):
    if conn == 1 : 
        global personnage
        global successful_add
        print(successful_add)
        all_reals, all_prods = Realisateur.objects.all(), Producteur.objects.all()
        return render(request, "DAT/resp_insp_enregistrer_doc.html", {"personnage" : personnage, "producteurs" : all_prods, "realisateurs" : all_reals, 'successful_add': successful_add})
    else :
        return redirect('connexion')
    

def resp_insp_enregistrer_doc_traitement(request):
    if conn == 1:
        if request.method == 'POST':
            code = request.POST.get('code')
            titre = request.POST.get('titre')
            sortie = request.POST.get('datedesortie')
            cover = request.FILES['cover']
            realisateur = request.POST.get('realisateur')
            producteur = request.POST.get('producteur')
            sujet = request.POST.get('description')
            print(code, titre, sortie,realisateur, producteur, sujet)
            try:
                # date_obj = datetime.strptime(sortie, "%Y-%m-%d").date()
                realisateur = Realisateur.objects.get(code = realisateur)
                producteur = Producteur.objects.get(code = producteur)
                new_doc = Documentaire(code = code, titre = titre, sortie = sortie, sujet = sujet, realisateur = realisateur, producteur = producteur, cover = cover)
                new_doc.save()
                global successful_add
                successful_add = True
                return redirect('resp_insp_enregistrer_doc')
            except Exception as e:
                print(f"il s'est produit une erreur : {e}")
                return HttpResponse(f"il s'est produit une erreur : {e}", status = 400)
    else:
        return redirect('connexion')

        

def resp_insp_modifier_doc(request, arg):
    if conn == 1 : 
        global personnage
        edit_doc = Documentaire.objects.get(code = arg)
        all_reals, all_prods = Realisateur.objects.all(), Producteur.objects.all()
        return render(request, "DAT/resp_insp_modifier_doc.html", {"personnage" : personnage, "producteurs" : all_prods, "realisateurs" : all_reals, "documentaire": edit_doc})
    else :
        return redirect('connexion')