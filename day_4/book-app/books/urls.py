from django.urls import path
from django.db import router


# Django rest framework
from rest_framework.routers import DefaultRouter

# Views
from .views import CategoryViewSet, BookViewSet, AuthorViewSet

router = DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'authors', AuthorViewSet)
router.register(r'books', BookViewSet)
urlpatterns = router.urls

urlpatterns += [

# path('', views.index, name='index'),
# path('author/<int:author_id>', views.author, name='author'),
# path('category/<int:category_id>', views.category, name='category'),
]
