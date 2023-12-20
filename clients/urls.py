from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    # localhost:8000/1 -> ID do cliente -> Cliente 1 (Parâmetro da rota)
    path("<int:client_id>/", views.detail, name="detail"),
    path("cadastro/", views.create, name="create"),
    path("<int:client_id>/atualizar/", views.update, name="update"),
    path("<int:client_id>/remover/", views.delete, name="delete"),
]
