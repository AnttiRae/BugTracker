from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
# Create your views here.

from .forms import BugForm
from .models import Bug

class BugView(View):
    form_class = BugForm
    initial = {'key': 'value'}
    template_name = 'bugs/bugs.html'


    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        bugs = Bug.objects.all()
        return render(request, 'bugs/bugs.html', {'form': form, 'bugs': bugs})

    ## new bug posting
    def post(self, request, *args , **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            bug = request.POST.dict()
            del bug['csrfmiddlewaretoken']
            bug['reported_by'] = request.user
            bug = Bug.objects.create(**bug)
            bug.refresh_from_db()
            return redirect(f'/bugs/{bug.pk}')
        else:
            return HttpResponse('ei jihuu')


class singleBugView(View):

    def get(self, request, *args, **kwargs):
        try:
            bug = Bug.objects.get(pk=kwargs['pk'])
        except ObjectDoesNotExist as error:
            return HttpResponse(error)
        return render(request, 'bugs/singleBug.html', {'bug': bug})
    
    def put(self, request, *args, **kwargs):
        bug = Bug.objects.get(pk=kwargs['pk'])
        print(bug)
        return HttpResponse('PUTattu')

class ProfileView(View):

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            current_user = User.objects.get(username=request.user)
            return render(request, 'profile/profile.html', {'user': current_user})
        return render(request, 'profile/profile.html')

class HomeView(View):

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            current_user = User.objects.get(username=request.user)
            all_bugs = Bug.objects.all()
            bugs_by_user = all_bugs.filter(reported_by=current_user)
            
            return render(request, 'home.html', {'current_user': current_user, 'all_bugs': all_bugs ,'bugs_by_user': bugs_by_user})
        return render(request, 'home.html')
