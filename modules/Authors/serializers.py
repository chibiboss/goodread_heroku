from rest_framework import serializers
from .models import Author
from modules.Books.serializers import BookNewSerializer

class AuthorSerializer(serializers.ModelSerializer):
    libros = BookNewSerializer(read_only=True,many=True)
    class Meta:
        model = Author
        fields = ("id","nombre","apellidos","nacionalidad",
        "biografia","libros")
        #exclude = ('sexo',)

