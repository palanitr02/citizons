# from django.views import View
# from django.shortcuts import render, redirect
# from django.contrib import messages

# from .forms import RegisterForm, LoginForm
# from .models import AdminLogin


# class RegisterView(View):

#     def get(self, request):

#         form = RegisterForm()

#         return render(request, 'register.html', {
#             'form': form
#         })

#     def post(self, request):

#         form = RegisterForm(request.POST)

#         if form.is_valid():

#             form.save()

#             messages.success(request, 'User Registered')

#             return redirect('login')

#         return render(request, 'register.html', {
#             'form': form
#         })


# class LoginView(View):

#     def get(self, request):

#         form = LoginForm()

#         return render(request, 'login.html', {
#             'form': form
#         })

#     def post(self, request):

#         form = LoginForm(request.POST)

#         if form.is_valid():

#             username = form.cleaned_data['username']
#             password = form.cleaned_data['password']

#             try:
#                 user = AdminLogin.objects.get(
#                     username=username
#                 )

#                 if user.check_password(password):

#                     request.session['user_id'] = user.id
#                     request.session['username'] = user.username
#                     request.session['role'] = user.role

#                     if user.role == 'admin':
#                         return redirect('admin_dashboard')

#                     elif user.role == 'staff':
#                         return redirect('staff_dashboard')

#                     elif user.role == 'viewer':
#                         return redirect('viewer_dashboard')

#                 else:
#                     messages.error(request, 'Invalid Password')

#             except AdminLogin.DoesNotExist:
#                 messages.error(request, 'User Not Found')

#         return render(request, 'login.html', {
#             'form': form
#         })