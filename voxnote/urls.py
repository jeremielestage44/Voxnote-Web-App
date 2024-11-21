from django.urls import path
from . import views
from .views import NoteDeleteView,NoteDetailView

urlpatterns = [
    path('', views.accueil, name='voxnote-accueil'),# lien vers la page d'accueil en arrivant sur le site
    path ('notes/', views.mesNotes, name='voxnote-notes'), # lien vers l'onglet où l'utilisateur peut aller voir ses notes
    path('about/', views.about, name='voxnote-about'),# lien vers la page à propos du site web
    path('notes/<int:pk>/delete/', NoteDeleteView.as_view(), name='voxnote-delete'),# lien vers la page ou on demande à l'utilisateur de confirmer si il veut vraiment delete la note
    path('notes/<int:pk>/', NoteDetailView.as_view(),name="voxnote-detail"),# lien vers la page ou l'utilisateur peut voir une note qu'il a choisi afin de la voir de manière plus détaillée

]