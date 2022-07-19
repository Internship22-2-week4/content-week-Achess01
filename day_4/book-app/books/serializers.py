# Django rest framework serializars
from unicodedata import category
from rest_framework import serializers
# Models
from .models import Author, Category, Book

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'


class BookSerializer(serializers.ModelSerializer):
    # Method to show data from FK
    # author = AuthorSerializer()
    # category = CategorySerializer()

    # Serializer method
    # category = serializers.SlugRelatedField(many=False, read_only=True, slug_field='name')
    # author = serializers.SlugRelatedField(many=False, read_only=True, slug_field='first_name')

    # Reassign
    # author = serializers.PrimaryKeyRelatedField(queryset=Author.objects.all())
    # category = serializers.PrimaryKeyRelatedField(
    #     queryset=Category.objects.all())

    class Meta:
        model = Book
        # exclude = ('id',)
        # fields = ['title', 'author', 'category']
        fields = '__all__'

    def to_representation(self, instance):
        return {
            'id': instance.id,
            'title': instance.title,
            'image': instance.image,
            'isbn': instance.isbn,
            'author': instance.author.first_name,
            'category': {
                'id': instance.category.id,
                'name': instance.category.name,
                'description': instance.category.description,
            }
        }
