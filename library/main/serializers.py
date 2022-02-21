from pyexpat import model
from django.utils.translation import gettext_lazy as _
from rest_framework.serializers import *

from .models import *

class SearchSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Book
        validators = []
        fields = '__all__'


class AllBooksSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Book
        validators = []
        fields = ['url', 'title', 'author', 'year_of_release', 'genre',
                  'category', 'publisher', 'photo_preview', 'book_file']

    def validate(self, data):
        if(data.get('category') == 'Зарубежная художественная литература'):
            validator = UniqueTogetherValidator(
                Book.objects.all(),
                ['title', 'author', 'publisher'],
                'Такая книга от этого издателя уже существует'
            )
        elif(data.get('category') == 'Учебник'):
            validator = UniqueTogetherValidator(
                Book.objects.all(),
                ['title', 'author', 'publisher', 'year_of_release'],
                'Такой учебник уже существует'
            )
        else:
            validator = UniqueTogetherValidator(
                Book.objects.all(),
                ['title', 'author', 'publisher'],
                'Такая книга уже существует'
            )
        
        validator(data, self)
        return data


class AuthorSerializer(HyperlinkedModelSerializer):
    class Meta:
        validators = []
        model = Author
        fields = '__all__'

    def validate(self, data):
        validator = UniqueTogetherValidator(
            Author.objects.all(),
            ['name', 'last_name', 'middle_name', 'date_of_birth'],
            'Данный автор уже существует'
        )
        validator(data, self)
        return data

class BookSerializer(ModelSerializer):
    class Meta:
        model = Book
        fields = ['photo_preview']