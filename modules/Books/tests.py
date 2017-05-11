from django.test import TestCase
from django.core.urlresolvers import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Book
from modules.Authors.models import Author
import json

# Create your tests here.

class BookListTest(APITestCase):

    def setUp(self):
        self.author = Author()
        self.author.nombre = "Un autor"
        self.author.apellidos = "apellidos"
        self.author.nacionalida = "Mexicana"
        self.author.biografia = ""
        self.author.sexo ="M"
        self.author.edad = 23
        self.author.save()
    
        self.book = {"nombre":"Un Libro",
        "ISBN":"232342342",
        "autor":self.author.id,
        "fecha_publicacio":"2017-01-01",
        "descripcion":"sdsdfdsfsd","raiting":0.0,
        "genero_literario":"DR"}
        self.url = reverse('list-books')

    def test_list_books(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_create_books(self):
        response = self.client.post(self.url,self.book, 
        format='json')

        self.assertEqual(response.status_code,status.HTTP_201_CREATED)
    


class BookDetailTest(APITestCase):
    
    def setUp(self):
        self.author = Author()
        self.author.nombre = "Un autor"
        self.author.apellidos = "apellidos"
        self.author.nacionalida = "Mexicana"
        self.author.biografia = ""
        self.author.sexo ="M"
        self.author.edad = 23
        self.author.save()

        self.book = Book(nombre="un libro",
        autor=self.author,ISBN="34234234235",
        descripcion="asdasdasdasdas",
        genero_literario="DR",
        rating=0.0)
        self.book.save()
        self.url = reverse('detail-books',args=[self.book.id])

    
    def test_retrieve_book(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code,status.HTTP_200_OK)
    

    def test_update_book(self):
        self.data = {"nombre":"Un Libro",
        "ISBN":"232342342",
        "autor":self.author.id,
        "fecha_publicacio":"2017-01-01",
        "descripcion":"sdsdfdsfsd","raiting":0.0,
        "genero_literario":"DR"}
        response = self.client.put(self.url,
        self.data,format='json')
        self.assertEqual(response.status_code,status.HTTP_200_OK)
        #self.assertEqual(response.data,self.data)

    
    def test_destroy_book(self):
        response = self.client.delete(self.url)
        self.assertEqual(response.status_code,status.HTTP_204_NO_CONTENT)

        
