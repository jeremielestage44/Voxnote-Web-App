from django.shortcuts import render, redirect
from django.views.generic import DeleteView, DetailView
from django.conf import settings
from .models import Note, Message  # Import des modèles Note et Message depuis le fichier models.py
from .forms import AudioForm  # Import du formulaire AudioForm depuis le fichier forms.py
import os  # Import du module os pour les opérations liées au système d'exploitation
import random  # Import du module random pour la génération de texte aléatoire
import string  # Import du module string pour manipuler les chaînes de caractères
from django.urls import reverse_lazy
import torch






def generate_random_string(length=100):
    # Fonction pour générer une chaîne de caractères aléatoire
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for _ in range(length))


class NoteDetailView(DetailView):
    # Vue pour afficher le détail d'une note
    model = Note
    template_name = "voxnote/note_detailView.html"


class NoteDeleteView(DeleteView):
    # Vue pour supprimer une note
    model = Note
    success_url = reverse_lazy('voxnote-notes')  # Redirection après suppression
    template_name = "voxnote/note_confirm_delete.html"  # Template de confirmation de suppression


# Vue pour la page d'accueil de l'application
def accueil(request):
    # Récupération du dernier message enregistré par l'utilisateur s'il existe
    user_message = Message.objects.filter().order_by('-date')
    if not user_message:
        recognized_text = 'Texte généré par Voxnote'
    else:
        recognized_text = user_message[0].message

    audio_form = AudioForm()  # Formulaire pour télécharger un fichier audio

    if request.method == 'POST':
        audio_form = AudioForm(request.POST, request.FILES)
        if audio_form.is_valid():
            audio_file = request.FILES['audio_file']

            # Enregistrement du fichier audio dans le répertoire dédié(pour tester si le fichier audio est vraiment la voix de l'utilisateur)
            media_directory = os.path.join(settings.MEDIA_ROOT, 'message_vocaux')
            os.makedirs(media_directory, exist_ok=True)
            file_path = os.path.join(settings.MEDIA_ROOT, 'message_vocaux', audio_file.name)
            with open(file_path, 'wb') as destination:
                for chunk in audio_file.chunks():
                    destination.write(chunk)

            # Génération d'un texte aléatoire (simule la reconnaissance vocale)
            recognized_text=generate_random_string()
            #device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
            #print('device enregistré')
            #model = torch.load('modele.pth',map_location=device)
            #recognized_text=modele.audiotraite(audio_file)
            #print('model enregistré')
            # Enregistrement du texte reconnu dans la base de données
            Message.objects.create(message=recognized_text)

            # Si l'utilisateur est connecté, enregistrement de la note associée au texte reconnu
            if request.user.is_authenticated:
                note = Note.objects.create(user=request.user, message=recognized_text)

            return redirect('voxnote-notes')  # Redirection vers la page des notes après traitement du formulaire

    return render(request, "voxnote/accueil.html", {'recognized_text': recognized_text, 'audio_form': audio_form})


# Vue pour afficher les notes de l'utilisateur
def mesNotes(request):
    user_notes = []  # Initialisation de la liste des notes de l'utilisateur à une liste vide
    # Vérification si l'utilisateur est connecté
    if request.user.is_authenticated:
        # Récupération des notes de l'utilisateur depuis la base de données et tri par date
        user_notes = Note.objects.filter(user=request.user).order_by('-date')
    # Rendu de la page des notes avec les données nécessaires pour l'affichage
    return render(request, "voxnote/notes.html", {'user_notes': user_notes})


def about(request):
    # Vue pour afficher la page "À propos"
    return render(request, "voxnote/about.html")
