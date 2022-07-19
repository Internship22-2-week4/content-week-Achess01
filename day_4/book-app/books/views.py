from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets

from .serializers import CategorySerializer, AuthorSerializer, BookSerializer

from .models import Book, Author, Category


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


# def index(request):
#     books = Book.objects.all()
#     return render(request, 'books/index.html', {"books_list": books})
#     # return HttpResponse("app book")


# def author(request, author_id):
#     try:
#         authorFounded = Author.objects.get(id=author_id)
#     except:
#         return render(request, 'books/author.html', {})
#     print(authorFounded.first_name)
#     return render(request, 'books/author.html', {"author": authorFounded})
#     #return HttpResponse("author id: " + str(author_id))


# def category(request, category_id):
#     return HttpResponse("category id: " + str(category_id))
