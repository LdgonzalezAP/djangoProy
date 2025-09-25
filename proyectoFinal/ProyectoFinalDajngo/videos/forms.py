from django import forms
from .models import Video

class VideoForm(forms.ModelForm):
    class Meta:
        model = Video
        fields = ["archivo"]

    def save(self, commit=True, usuario=None):
        instance = super().save(commit=False)

        # Extraer nombre, extensión y tamaño
        archivo = self.cleaned_data["archivo"]
        instance.nombre = archivo.name.rsplit(".", 1)[0]
        instance.extension = archivo.name.rsplit(".", 1)[-1].lower()
        instance.tamaño = round(archivo.size / (1024 * 1024), 2)  # en MB

        if usuario:
            instance.usuario = usuario

        if commit:
            instance.save()
        return instance