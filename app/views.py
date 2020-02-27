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
        bugs = Bug.objects.all()
        print(bugs)
        return render(request, 'bugs/bugs.html', {'form': form, 'bugs': bugs})

    ## new bug posting
    def post(self, request, *args , **kwargs):
        print('POST jou')
        form = self.form_class(request.POST)
        print(request.POST)
        if form.is_valid():
            bug = request.POST.dict()
            del bug['csrfmiddlewaretoken']
            bug['reported_by'] = request.user
            Bug.objects.create(**bug)
            return HttpResponse('Jihuu')
        else:
            return HttpResponse('ei jihuu')


class singleBugView(View):

    def get(self, request, *args, **kwargs):
        return HttpResponse('moi')

class ProfileView(View):

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            print('request', request.user)
            current_user = User.objects.get(username=request.user)
            return render(request, 'profile/profile.html', {'user': current_user})
        return render(request, 'profile/profile.html')
