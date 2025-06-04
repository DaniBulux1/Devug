from django.shortcuts import render, get_object_or_404, redirect
from .models import Tutorial
from .forms import TutorialForm
from django.views.decorators.csrf import csrf_exempt
import json

def lista_tutoriales(request):
    """Muestra la lista de tutoriales más recientes"""
    tutoriales = Tutorial.objects.all()
    return render(request, 'index.html', {'tutoriales': tutoriales})


def detalle_tutorial(request, pk):
    """Muestra el contenido completo de un tutorial"""
    tutorial = get_object_or_404(Tutorial, pk=pk)
    return render(request, 'post.html', {'tutorial': tutorial})


@csrf_exempt
def crear_tutorial(request):
    """
    Permite crear un nuevo tutorial. Se espera que el frontend
    envíe el UID de Firebase, nombre del autor y URL de la foto como parte del formulario.
    """
    if request.method == 'POST':
        form = TutorialForm(request.POST)
        if form.is_valid():
            tutorial = form.save(commit=False)
            # Recibe los datos del autor desde el frontend (debe enviarlos en el POST)
            tutorial.autor_uid = request.POST.get('autor_uid')
            tutorial.autor_nombre = request.POST.get('autor_nombre')
            tutorial.autor_foto_url = request.POST.get('autor_foto_url')
            tutorial.save()
            return redirect('detalle_tutorial', pk=tutorial.pk)
    else:
        form = TutorialForm()
    return render(request, 'forms.html', {'form': form})