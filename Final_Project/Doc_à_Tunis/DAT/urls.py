from django.urls import path
from . import views


urlpatterns = [
    path('', views.connexion, name="connexion"),

    # Connexion Resp_Insp
    path('connexion_resp_insp/', views.connexion_resp_insp, name="connexion_resp_insp"),
    path('traitement_connexion_resp_insp/', views.traitement_connexion_resp_insp, name="traitement_connexion_resp_insp"),
    
    # Connexion Resp_Prod
    path('connexion_resp_prod/', views.connexion_resp_prod, name="connexion_resp_prod"),
    path('traitement_connexion_resp_prod/', views.traitement_connexion_resp_prod, name="traitement_connexion_resp_prod"),

     # Connexion Jury
    path('connexion_jury/', views.connexion_jury, name="connexion_jury"),
    path('traitement_connexion_jury/', views.traitement_connexion_jury, name="traitement_connexion_jury"),

    #Responsable d'inspection
    path('resp_insp_voir_doc/', views.resp_insp_voir_doc, name="resp_insp_voir_doc"),
    path('resp_insp_gerer_doc/', views.resp_insp_gerer_doc, name="resp_insp_gerer_doc"),
    path('resp_insp_gerer_real/', views.resp_insp_gerer_real, name="resp_insp_gerer_real"),
    path('resp_insp_gerer_prod/', views.resp_insp_gerer_prod, name="resp_insp_gerer_prod"),
    path('resp_insp_enregistrer_doc/', views.resp_insp_enregistrer_doc, name="resp_insp_enregistrer_doc"),
    path('resp_insp_enregistrer_doc_traitement/', views.resp_insp_enregistrer_doc_traitement, name="resp_insp_enregistrer_doc_traitement"),
    path('resp_insp_modifier_doc/<str:arg>', views.resp_insp_modifier_doc, name="resp_insp_modifier_doc"),

]