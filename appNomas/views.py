from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,login,logout as do_logout
from .backend import MyBackend
from .forms import PostForm ,LoginPostForm,postcontrato

# Create your views here.
def welcome(request):
    return render(request,'appNomas/welcome.html',{})
def form(request):
    forms=postcontrato()
    return render(request, 'appNomas/form.html', {'forms':forms})
myBakend=MyBackend()
def index(request):
    return render(request,'appNomas/index.html',{})
def register(request):
    # Creamos el formulario de autenticación vacío
    form = PostForm()
    if request.method == "POST":
        # Añadimos los datos recibidos al formulario
        form = PostForm(request.POST)     

        if form.is_valid():
            form.save()  
            # Creamos la nueva cuenta de usuario

            # Si el usuario se crea correctamente 
            if form is not None:
                # Hacemos el login manualmente
                # Y le redireccionamos a la portada
                return redirect('/login')

    # Si llegamos al final renderizamos el formulario
    return render(request, "appNomas/register.html", {'form': form})
def login_user(request):
    # Creamos el formulario de autenticación vacío
    
    form = LoginPostForm()
    if request.method == "POST":
        print("llegue al post")
        # Añadimos los datos recibidos al formulario
        form = LoginPostForm(data=request.POST)
        # Si el formulario es válido...
            # Recuperamos las credenciales validadas
        rut = form['rut'].value()
        clave = form['password'].value()
        print(rut)
            #Ejemplo
        user=myBakend.authenticate(request,username=rut,password=clave)
           
           
        if user is not None:
            login(request,user,backend='appNomas.backend.MyBackend')
            return render(request, 'appNomas/welcome.html')
            

    # Si llegamos al final renderizamos el formulario
    return render(request, "appNomas/login.html", {'form': form})
def logout(request):
    # Finalizamos la sesión
    do_logout(request)
    # Redireccionamos a la portada
    return redirect('/')
