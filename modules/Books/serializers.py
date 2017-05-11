from rest_framework import serializers
from .models  import Book,Comments
from modules.Users.serializers import UserSerializer
#from modules.Authors.serializers import AuthorSerializer
class CommentSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    class Meta:
        model = Comments
        fields = ('user','commentario')

class BookSerializer(serializers.ModelSerializer):
    #author_name =  serializers.CharField(source="autor.nombre")
    #author_lastname = serializers.CharField(source="autor.apellidos")
    #autor = AuthorSerializer(read_only=True)
    comentarios = CommentSerializer(read_only=True,many=True)
    class Meta:
        model = Book
        #exclude = ("rating",)
        fields = ('id','nombre','descripcion','ISBN','comentarios','autor')
    
class BookNewSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = ("__all__")