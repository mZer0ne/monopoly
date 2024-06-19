from django.contrib.auth import login, authenticate
from django.utils.translation import gettext as _
from django.shortcuts import render, redirect
from django.views import View


class LoginView(View):
    initial = {
        'active_page': 'register',
        'action': _('Register')
    }
    template_name = 'login_view.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {
            'active_page': 'login',
            'action': _('Login'),
            "error": None
        })

    def post(self, request, *args, **kwargs):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user is not None:
            if user.is_active:
                login(request, user)
                if 'next' in request.GET:
                    return redirect(request.GET['next'])
                else:
                    return redirect("/join")
            else:
                res = {
                    'error': _('Inactive user.'),
                    'active_page': 'login',
                    'action': _('Login'),
                }
                return render(request, self.template_name, res)
        else:
            res = {
                'error': _('Invalid username or password.'),
                'active_page': 'login',
                'action': _('Login'),
            }
            return render(request, self.template_name, res)
