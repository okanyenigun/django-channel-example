
from django.urls import path
from two.views import two

urlpatterns = [
    path('two/', two),
]
