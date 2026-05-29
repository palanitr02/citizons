from django.views import View
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import AdminLogin
from django.contrib.auth import authenticate, login, logout



# ---------------- SIGNUP ----------------
class SignupView(View):

    def get(self, request):
        return render(request, "register.html")

    def post(self, request):

        username = request.POST.get("username")
        password = request.POST.get("password")
        role = request.POST.get("role")

        # validation
        if not username or not password:
            messages.error(request, "All fields are required")
            return redirect("signup")

        # username exists
        if AdminLogin.objects.filter(username=username).exists():
            messages.error(request, "Username already exists")
            return redirect("signup")

        # save user
        AdminLogin.objects.create(
            username=username,
            password=password,
            role=role
        )

        messages.success(request, "Account created successfully")
        return redirect("login")


# ---------------- LOGIN ----------------
class LoginView(View):

    def get(self, request):
        return render(request, "login.html")

    def post(self, request):

        username = request.POST.get("username")
        password = request.POST.get("password")

        try:
            user = AdminLogin.objects.get(username=username)

            # check hashed password
            if user.check_password(password):

                request.session['admin_id'] = user.id
                request.session['username'] = user.username
                request.session['role'] = user.role
                
                messages.success(request, "Login successful")
                
                return redirect("person_list")

            else:
                
                messages.error(request, "Invalid password")
                return redirect("login")

        except AdminLogin.DoesNotExist:
            messages.error(request, "Username not found")
            

        return redirect("login")
    

# ---------------- LOGOUT CBV ----------------
class LogoutView(View):

    def get(self, request):
        logout(request)
        return redirect("login")