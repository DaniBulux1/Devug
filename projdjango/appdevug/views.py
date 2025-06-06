from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from .models import Tutorial, Reaccion
from .forms import TutorialForm
import json

def lista_tutoriales(request):
    """
    Vista principal que muestra todos los tutoriales
    """
    tutoriales = Tutorial.objects.all().order_by('-fecha_creacion')
    return render(request, 'index.html', {'tutoriales': tutoriales})

def detalle_tutorial(request, pk):
    """
    Vista que muestra el detalle de un tutorial específico
    """
    tutorial = get_object_or_404(Tutorial, pk=pk)
    return render(request, 'preview.html', {'tutorial': tutorial})

@csrf_exempt
def crear_tutorial(request):
    """
    Vista para crear un nuevo tutorial
    """
    if request.method == 'POST':
        form = TutorialForm(request.POST)
        if form.is_valid():
            tutorial = form.save(commit=False)
            # Obtener datos del autor desde el formulario (enviados por JavaScript)
            tutorial.autor_uid = request.POST.get('autor_uid', '')
            tutorial.autor_nombre = request.POST.get('autor_nombre', 'Usuario Anónimo')
            tutorial.autor_foto_url = request.POST.get('autor_foto_url', '')
            tutorial.save()
            return redirect('detalle_tutorial', pk=tutorial.pk)
        else:
            # Si hay errores en el formulario, regresa con los errores
            return render(request, 'forms.html', {'form': form})
    else:
        form = TutorialForm()
    return render(request, 'forms.html', {'form': form})

@csrf_exempt
def editar_tutorial(request, pk):
    """
    Permite editar un tutorial existente.
    """
    tutorial = get_object_or_404(Tutorial, pk=pk)
    if request.method == 'POST':
        form = TutorialForm(request.POST, instance=tutorial)
        if form.is_valid():
            tutorial = form.save(commit=False)
            # Mantener datos del autor (no cambiar en edición)
            # Si necesitas permitir cambio de autor, descomenta las siguientes líneas:
            # tutorial.autor_uid = request.POST.get('autor_uid', tutorial.autor_uid)
            # tutorial.autor_nombre = request.POST.get('autor_nombre', tutorial.autor_nombre)
            # tutorial.autor_foto_url = request.POST.get('autor_foto_url', tutorial.autor_foto_url)
            tutorial.save()
            return redirect('detalle_tutorial', pk=tutorial.pk)
    else:
        form = TutorialForm(instance=tutorial)
    return render(request, 'forms.html', {'form': form, 'tutorial': tutorial})

@csrf_exempt
@require_POST
def agregar_reaccion(request):
    """
    API endpoint para agregar reacciones a tutoriales
    """
    try:
        data = json.loads(request.body)
        tutorial_id = data.get('tutorial_id')
        emoji = data.get('emoji')
        usuario_uid = data.get('usuario_uid')
        
        if not all([tutorial_id, emoji, usuario_uid]):
            return JsonResponse({'error': 'Faltan datos requeridos'}, status=400)
        
        tutorial = get_object_or_404(Tutorial, pk=tutorial_id)
        
        # Verificar si ya existe una reacción del mismo usuario para el mismo tutorial y emoji
        reaccion, created = Reaccion.objects.get_or_create(
            usuario_uid=usuario_uid,
            tutorial=tutorial,
            emoji=emoji
        )
        
        if created:
            return JsonResponse({
                'status': 'success',
                'message': 'Reacción agregada',
                'reaccion_id': reaccion.id
            })
        else:
            # Si ya existe, la eliminamos (toggle)
            reaccion.delete()
            return JsonResponse({
                'status': 'success',
                'message': 'Reacción eliminada'
            })
            
    except json.JSONDecodeError:
        return JsonResponse({'error': 'JSON inválido'}, status=400)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)

def obtener_reacciones(request, tutorial_id):
    """
    API endpoint para obtener las reacciones de un tutorial
    """
    tutorial = get_object_or_404(Tutorial, pk=tutorial_id)
    reacciones = tutorial.reacciones.all()
    
    # Agrupar reacciones por emoji
    reacciones_agrupadas = {}
    for reaccion in reacciones:
        if reaccion.emoji not in reacciones_agrupadas:
            reacciones_agrupadas[reaccion.emoji] = 0
        reacciones_agrupadas[reaccion.emoji] += 1
    
    return JsonResponse({
        'tutorial_id': tutorial_id,
        'reacciones': reacciones_agrupadas
    })