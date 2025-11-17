from django.urls import path
from . import views

urlpatterns = [
    path("", views.registrar_incidente, name="form_incidente"),
    path("success/<int:pk>/", views.success, name="success"),
    path('incidentes/', views.lista_incidentes, name='lista_incidentes'),
]
