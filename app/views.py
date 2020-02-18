from django.shortcuts import render
from django.views import View
from django.contrib.auth.models import User
# Create your views here.

class BugView(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'bugs/bugs.html')


class ProfileView(View):

    def get(self, request, *args, **kwargs):
        print('request',request.user)
        current_user = User.objects.get(username=request.user)
        print('jauu', current_user)
        print(current_user.username)
        print(current_user.last_login)
        print(current_user.date_joined)
        return render(request, 'profile/profile.html', {'user': current_user})

