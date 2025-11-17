from django.shortcuts import render, redirect, get_object_or_404
from .forms import IncidenteForm
from .models import Incidente


def registrar_incidente(request):
    if request.method == "POST":
        form = IncidenteForm(request.POST, request.FILES)
    if request.method == "POST":
        form = IncidenteForm(request.POST, request.FILES)
        if form.is_valid():
            incidente = form.save()

            # REDIRECCIÓN correcta
            return redirect("success", pk=incidente.pk)
    else:
        form = IncidenteForm()

    return render(request, "formulario/form_incidente.html", {"form": form})


def success(request, pk):
    incidente = get_object_or_404(Incidente, pk=pk)
    return render(request, "formulario/success.html", {"incidente": incidente})

def lista_incidentes(request):
    incidentes = Incidente.objects.all().order_by('-fecha', '-hora')
    return render(request, 'formulario/lista_incidentes.html', {'incidentes': incidentes})
