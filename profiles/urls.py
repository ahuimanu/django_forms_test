from django.urls import path

from . import views

namespace = "profiles"

urlpatterns = [
    path("profiles/<pid>", views.show_one),
    path("profiles/", views.show_all),
]
