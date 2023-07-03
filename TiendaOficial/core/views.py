from django.shortcuts import redirect, render
from .models import Juego, Categoria
from .forms import JuegoForm

# Create your views here.

def home(request):
    return render(request, "core/home.html")

def juego_tienda(request):
    data = {"list": Juego.objects.all().order_by('codigo')}
    return render(request, "core/juego_tienda.html", data)

def juego_ficha(request, id):
    juego = Juego.objects.get(codigo=id)
    data = {"juego":  juego}
    return render(request, "core/juego_ficha.html", data)

def juego(request, action, id):
    data = {"mesg": "", "form": JuegoForm, "action": action, "id": id}

    if action == 'ins':
        if request.method == "POST":
            form = JuegoForm(request.POST, request.FILES)
            if form.is_valid:
                try:
                    form.save()
                    data["mesg"] = "¡El juego fue creado correctamente!"
                except:
                    data["mesg"] = "¡No se puede crear dos juego el mismo codigo!"

    elif action == 'upd':
        objeto = Juego.objects.get(codigo=id)
        if request.method == "POST":
            form = JuegoForm(data=request.POST, files=request.FILES, instance=objeto)
            if form.is_valid:
                form.save()
                data["mesg"] = "¡El juego fue actualizado correctamente!"
        data["form"] = JuegoForm(instance=objeto)

    elif action == 'del':
        try:
            Juego.objects.get(codigo=id).delete()
            data["mesg"] = "¡El juego fue eliminado correctamente!"
            return redirect(juego, action='ins', id = '-1')
        except:
            data["mesg"] = "¡El juego ya estaba eliminado!"

    data["list"] = Juego.objects.all().order_by('codigo')
    return render(request, "core/juego.html", data)
def poblar_bd(request):
    Juego.objects.all().delete()
    Juego.objects.create(codigo="jg-01", nombre='Diablo', plataforma="Playstation,Xbox", imagen="images/diablo.jpg", categoria=Categoria.objects.get(idCategoria=2))
    Juego.objects.create(codigo="jg-02", nombre='Fifa23', plataforma="SNintendo,PS,Xbox", imagen="images/fifa23.jpg", categoria=Categoria.objects.get(idCategoria=2))
    Juego.objects.create(codigo="jg-03", nombre='Gta', plataforma="Playstation,Xbox", imagen="images/gta.jpg", categoria=Categoria.objects.get(idCategoria=2))
    Juego.objects.create(codigo="jg-04", nombre='Halo', plataforma="Xbox", imagen="images/halo.jpg", categoria=Categoria.objects.get(idCategoria=2))
    Juego.objects.create(codigo="jg-05", nombre='Hogwarts', plataforma="Playstation", imagen="images/hogwarts.jpg", categoria=Categoria.objects.get(idCategoria=3))
    Juego.objects.create(codigo="jg-06", nombre='Mario', plataforma="Nintendo Switch", imagen="images/mario.jpg", categoria=Categoria.objects.get(idCategoria=3))
    Juego.objects.create(codigo="jg-07", nombre='Minecraft', plataforma="Nintendo,PS,Xbox", imagen="images/minecraft.jpg", categoria=Categoria.objects.get(idCategoria=3))
    Juego.objects.create(codigo="jg-08", nombre='Mortalkombat', plataforma="Playstation,Xbox", imagen="images/mortalkomat.jpg", categoria=Categoria.objects.get(idCategoria=1))
    Juego.objects.create(codigo="jg-09", nombre='Spiderman', plataforma="PlayStation", imagen="images/spiderman.jpg", categoria=Categoria.objects.get(idCategoria=1))
    Juego.objects.create(codigo="jg-10", nombre='Zelda', plataforma="Nintendo Switch", imagen="images/zelda.jpg", categoria=Categoria.objects.get(idCategoria=3))
    return redirect(Juego, action='ins', id = '-1')
