from django.urls import path
from recipes.views import home, contato

urlpatterns = [
    path('', home),  # home
    path('contato/', contato),  # contato
]
