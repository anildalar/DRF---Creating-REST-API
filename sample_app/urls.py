
from django.contrib import admin
from django.urls import path,include

from sample_app.views import StudentView

urlpatterns = [
    path('basic/',StudentView.as_view())  # /api/basic
]
