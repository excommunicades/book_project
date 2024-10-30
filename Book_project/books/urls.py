from rest_framework.routers import DefaultRouter

from django.urls import path, include

from books.views import BookViewSet


router = DefaultRouter()
router.register(r'books', BookViewSet, basename='books')

urlpatterns = [
    path('', include(router.urls)),
    path('<int:pk>', include(router.urls)),
]
