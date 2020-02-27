from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.contrib.auth.models import User
# Create your views here.

from .forms import BugForm
from .models import Bug

class BugView(View):
    form_class = BugForm
    initial = {'key': 'value'}
    template_name = 'bugs/bugs.html'


    def get(self, request, *args, **kwargs):
        print('GET jou')
        form = self.form_class(initial=self.initial)
        return render(request, 'bugs/bugs.html', {'form': form})
    
    def post(self, request, *args , **kwargs):
        print('POST jou')
        form = self.form_class(request.POST)
        if form.is_valid():
            bug = form.save(commit=False)
            post.save()
            return HttpResponse('Jihuu')
        else:
            return HttpResponse('ei jihuu')


class ProfileView(View):

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            print('request', request.user)
            current_user = User.objects.get(username=request.user)
            return render(request, 'profile/profile.html', {'user': current_user})
        return render(request, 'profile/profile.html')
