# views.py (Fragmento, para referencia)
from django.shortcuts import render, get_object_or_404, redirect
from .models import Tutorial
from .forms import TutorialForm
from django.views.decorators.csrf import csrf_exempt # ¡Cuidado con csrf_exempt en producción!
# import json # No necesario para este fragmento

# ... (tus otras vistas: lista_tutoriales, detalle_tutorial, crear_tutorial) ...

@csrf_exempt # Considera usar @login_required y un método más seguro para CSRF en producción
def editar_tutorial(request, pk):
    """
    Permite editar un tutorial existente.
    Carga el tutorial por su PK.
    """
    tutorial = get_object_or_404(Tutorial, pk=pk)
    if request.method == 'POST':
        form = TutorialForm(request.POST, instance=tutorial) # Pasa la instancia para editar
        if form.is_valid():
            tutorial = form.save(commit=False)
            # Los campos de autor ya deberían estar en la instancia si se cargó desde la DB
            # Si permites que el autor cambie, necesitarías lógica aquí.
            # tutorial.autor_uid = request.POST.get('autor_uid', tutorial.autor_uid)
            # tutorial.autor_nombre = request.POST.get('autor_nombre', tutorial.autor_nombre)
            # tutorial.autor_foto_url = request.POST.get('autor_foto_url', tutorial.autor_foto_url)
            tutorial.save()
            return redirect('detalle_tutorial', pk=tutorial.pk) # Redirige a la vista de detalle
    else:
        form = TutorialForm(instance=tutorial) # Carga el formulario con los datos existentes
    return render(request, 'forms.html', {'form': form, 'tutorial': tutorial}) # Pasa 'tutorial' para el título dinámico