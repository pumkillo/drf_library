from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import *
from rest_framework.response import Response
from rest_framework.generics import *
from rest_framework import filters

from .models import *
from .permissions import IsAdminUserOrReadOnly
from .serializers import *

# Create your views here.


class AllBooksViewSet(ModelViewSet):
    permission_classes = [IsAdminUserOrReadOnly]
    queryset = Book.objects.all()
    serializer_class = AllBooksSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['$title', '$genre', '$category',
                     "$author__name", '$author__last_name', '$author__middle_name']


class AuthorViewSet(ModelViewSet):
    permission_classes = [IsAdminUserOrReadOnly]
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

@api_view(['GET'])
def image(request, filepath):
    queryset = BookSerializer(Book.objects.all())
    return Response({'image': queryset.data}, content_type='image/png')
