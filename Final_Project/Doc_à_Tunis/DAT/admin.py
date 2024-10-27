# admin.py
from django.contrib import admin
from .models import Resp_Insp, Resp_Prod, Jury, Realisateur, Documentaire

@admin.register(Resp_Insp)
class RespInspAdmin(admin.ModelAdmin):
    list_display = ('id', 'nom', 'prenoms', 'phone', 'email') 
    list_filter = ['nom',] 
    search_fields = ('nom', 'prenoms', 'email') 

@admin.register(Resp_Prod)
class RespProdAdmin(admin.ModelAdmin):
    list_display = ('id', 'nom', 'prenoms', 'phone', 'email')
    list_filter = ['nom']
    search_fields = ('nom', 'prenoms', 'email')

@admin.register(Jury)
class JuryAdmin(admin.ModelAdmin):
    list_display = ('id', 'code', 'nom', 'prenoms', 'email', 'president')
    list_filter = ['president', 'nom']
    search_fields = ('nom', 'prenoms', 'email', 'code')

@admin.register(Realisateur)
class RealisateurAdmin(admin.ModelAdmin):
    list_display = ('id', 'code', 'nom', 'prenoms', 'email')
    list_filter = ['nom',]
    search_fields = ('nom', 'prenoms', 'email', 'code')

@admin.register(Documentaire)
class DocumentaireAdmin(admin.ModelAdmin):
    list_display = ('id', 'code', 'titre', 'realisateur', 'producteur', 'note')
    list_filter = ['realisateur', 'producteur']
    search_fields = ('titre', 'code', 'sujet')
