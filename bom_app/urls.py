from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name='index'),
    path("bom/<int:product_id>/", views.bom_view, name='bom_view'),
]
