from monopoly.models import Profile
from django.shortcuts import render
from django.views import View
import hashlib


class JoinView(View):
    template_name = 'join_view.html'

    def get(self, request, *args, **kwargs):
        print(request.path)
        user = request.user
        host_name = kwargs.get('host_name', user.username)

        try:
            profile = Profile.objects.get(user=user)
        except Exception:
            profile = None

        if profile is None:
            avatar = "https://www.gravatar.com/avatar/" + hashlib.md5(
                user.email.encode()
            ).hexdigest() + "?d=robohash&f=y"
        else:
            avatar = profile.avatar.url

        return render(request, self.template_name, {
            "user": {
                "name": user.username,
                "avatar": avatar
            },
            "host_name": host_name if len(host_name) else user.username
        })
