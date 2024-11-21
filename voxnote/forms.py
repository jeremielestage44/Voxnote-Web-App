# forms.py
from django import forms


class AudioForm(forms.Form):# form pour le fichier audio obtenu par le message vocal de l'utilisateur
    audio_file = forms.FileField()