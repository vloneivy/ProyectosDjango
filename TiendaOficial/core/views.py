from django.shortcuts import redirect, render
from .models import servicio, Categoria
from .forms import servicioForm

# Create your views here.

def home(request):
    return render(request, "core/home.html")

def servicio_tienda(request):
    data = {"list": servicio.objects.all().order_by('codigo')}
    return render(request, "core/servicio_tienda.html", data)

def servicio_ficha(request, id):
    servicio = servicio.objects.get(codigo=id)
    data = {"servicio":  servicio}
    return render(request, "core/servicio_ficha.html", data)

def servicio(request, action, id):
    data = {"mesg": "", "form": servicioForm, "action": action, "id": id}

    if action == 'ins':
        if request.method == "POST":
            form = servicioForm(request.POST, request.FILES)
            if form.is_valid:
                try:
                    form.save()
                    data["mesg"] = "¡El servicio fue creado correctamente!"
                except:
                    data["mesg"] = "¡No se puede crear dos servicios con el mismo codigo!"

    elif action == 'upd':
        objeto = servicio.objects.get(codigo=id)
        if request.method == "POST":
            form = servicioForm(data=request.POST, files=request.FILES, instance=objeto)
            if form.is_valid:
                form.save()
                data["mesg"] = "¡El servicio fue actualizado correctamente!"
        data["form"] = servicioForm(instance=objeto)

    elif action == 'del':
        try:
            servicio.objects.get(codigo=id).delete()
            data["mesg"] = "¡El servicio fue eliminado correctamente!"
            return redirect(servicio, action='ins', id = '-1')
        except:
            data["mesg"] = "¡El servicio ya estaba eliminado!"

    data["list"] = servicio.objects.all().order_by('codigo')
    return render(request, "core/servicio.html", data)
def poblar_bd(request):
    servicio.objects.all().delete()
    servicio.objects.create(codigo="jg-01", nombre='Motor', servicios="Servicio,Instalado", imagen="images/motor1.webp", categoria=Categoria.objects.get(idCategoria=2))
    servicio.objects.create(codigo="jg-02", nombre='Neumaticos', servicios="Compra", imagen="images/neumaticos2.jpg", categoria=Categoria.objects.get(idCategoria=2))
    servicio.objects.create(codigo="jg-03", nombre='Frenos', servicios="Servicio,Instalado", imagen="images/frenos3.jpg", categoria=Categoria.objects.get(idCategoria=2))
    servicio.objects.create(codigo="jg-04", nombre='Caja de cambios', servicios="Servicio,Instalado", imagen="images/cajacambio4.jpg", categoria=Categoria.objects.get(idCategoria=2))
    servicio.objects.create(codigo="jg-05", nombre='Bujias', servicios="Compra", imagen="images/bujias5.webp", categoria=Categoria.objects.get(idCategoria=3))
    servicio.objects.create(codigo="jg-06", nombre='Amortiguador', servicios="Compra", imagen="images/amortiguador6.jpg", categoria=Categoria.objects.get(idCategoria=3))
    servicio.objects.create(codigo="jg-07", nombre='Llanta', servicios="Compra", imagen="images/llanta7.webp", categoria=Categoria.objects.get(idCategoria=3))
    servicio.objects.create(codigo="jg-08", nombre='Volante', servicios="Servicio,Instalado", imagen="images/volante.webp", categoria=Categoria.objects.get(idCategoria=1))
    servicio.objects.create(codigo="jg-09", nombre='Capo', servicios="Servicio,Instalado", imagen="images/capo9.jpg", categoria=Categoria.objects.get(idCategoria=1))
    servicio.objects.create(codigo="jg-10", nombre='Parachoque', servicios="Servicio,Instalado", imagen="images/parachoque.jpg", categoria=Categoria.objects.get(idCategoria=3))
    return redirect(servicio, action='ins', id = '-1')
