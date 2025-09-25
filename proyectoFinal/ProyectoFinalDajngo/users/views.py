from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from videos.models import Video

def signup(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        email = request.POST.get("email", "")
        first_name = request.POST.get("first_name", "")
        last_name = request.POST.get("last_name", "")

        user = User.objects.create_user(
            username=username,
            password=password,
            email=email,
            first_name=first_name,
            last_name=last_name
        )
        login(request, user)  # inicia sesión automáticamente
        return redirect("dashboard")

    return render(request, "users/signup.html")


def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect("dashboard")
        else:
            return render(request, "users/login.html", {"error": "Usuario o contraseña incorrectos"})

    return render(request, "users/login.html")

def logout_view(request):
    logout(request)
    return redirect("login")



# Dashboard 
@login_required
def dashboard(request):
    videos = Video.objects.filter(usuario=request.user).order_by("-creado_en")[:5]  # últimos 5
    return render(request, "users/dashboard.html", {"videos": videos})


# CRUD de usuarios

# Listar usuarios
@login_required
def list_users(request):
    users = User.objects.all()
    return render(request, "users/list_users.html", {"users": users})


# Editar usuario
@login_required
def edit_user(request, user_id):
    user = get_object_or_404(User, id=user_id)

    if request.method == "POST":
        user.username = request.POST["username"]
        user.email = request.POST["email"]
        user.first_name = request.POST["first_name"]
        user.last_name = request.POST["last_name"]

        if request.POST.get("password"):
            user.set_password(request.POST["password"])

        user.save()
        return redirect("dashboard")

    return render(request, "users/edit_user.html", {"user": user})



@login_required
def delete_user(request, user_id):
    user = get_object_or_404(User, id=user_id)

    if request.method == "POST":
        user.delete()
        return redirect("login")

    return render(request, "users/delete_user.html", {"user": user})