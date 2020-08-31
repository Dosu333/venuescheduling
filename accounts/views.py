from django.shortcuts import render, redirect
from django.views.generic import CreateView, FormView
from accounts.forms import LoginForm, RegisterForm
from django.utils.http import is_safe_url
from django.contrib import auth
from django.contrib.auth import authenticate, login, get_user_model
from django.urls import reverse_lazy

# Create your views here.
class LoginView(FormView):
    form_class = LoginForm
    template_name = 'accounts/login.html'
    success_url = 'land'

    def form_valid(self, form):
        request = self.request
        next_ =  request.GET.get('next')
        next_post = request.POST.get('next')
        redirect_path = next_ or next_post or None

        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")
        user = authenticate(request, username=email, password=password)

        context ={"form": form}

        if user is not None:
            login(request,user)
            try:
                del request.session['guest_mail_id']
            except:
                pass
            if is_safe_url(redirect_path, request.get_host()):
                return redirect(redirect_path)
            else:
                return redirect("land")
        else:
            print("Error")
            return render(request, "accounts/login.html", context)

        super(LoginView, self).form_invalid(form)


def logout(request):
    auth.logout(request)
    return redirect('/')

# def login_page(request):
#     form = LoginForm(request.POST or None)
#     context ={
#         "form": form
#     }
   #
#         else:
#             print("Error")
#         return render(request, "accounts/login.html", context)

class RegisterView(CreateView):
    form_class = RegisterForm
    template_name = 'accounts/signup.html'
    success_url = reverse_lazy('login')



# User = get_user_model()
# def register_page(request):
#     form = RegisterForm(request.POST or None)
#     context ={
#         'form':form
#     }
#     if form.is_valid():
#         form.save()
#     return render(request, "accounts/signup.html", context)
