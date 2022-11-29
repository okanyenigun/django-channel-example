
from django.urls import path
from one.views import one

urlpatterns = [
    path('one/', one),
]
