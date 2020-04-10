from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import F
import json
# Create your views here.

from .forms import BugForm, CommentForm
from .models import Bug, Comment

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
            return HttpResponse('Something went wrong, sorry')


class CommentsView(View):
    form_class = CommentForm
    initial = {'key': 'value'}

    def post(self, request, *args, **kwargs):
        print('POST comment')
        form = self.form_class(request.POST)
        if form.is_valid():
            comment = request.POST.dict()
            del comment['csrfmiddlewaretoken']
            comment['commented_by'] = request.user
            comment['bug'] = Bug.objects.get(pk=kwargs['pk'])
            Comment.objects.create(**comment)
            return redirect(f"/bugs/{kwargs['pk']}")
        else:
            return HttpResponse('Something went wrong, sorry')
    def put(self, request, *args, **kwargs):
        body = json.loads(request.body)
        user = request.user
        vote = body['vote']
        commentId = body['comment']
        comment = Comment.objects.get(pk=commentId)
        if str(user) not in comment.voters:
            comment.score += vote
            comment.voters.append(user)
            comment.save()
            return HttpResponse('vote counted')
        else:
            return HttpResponse('vote already counted')
        

class singleBugView(View):
    form_class = CommentForm
    initial = {'key': 'value'}
    template_name = 'bugs/singleBug.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        try:
            bug = Bug.objects.get(pk=kwargs['pk'])
            comments = Comment.objects.filter(bug=kwargs['pk']).order_by('-created_at')
            print(comments)
        except ObjectDoesNotExist as error:
            return HttpResponse(error)
        return render(request, 'bugs/singleBug.html', {'form': form, 'bug': bug, 'comments': comments})
    
    def put(self, request, *args, **kwargs):
        body = json.loads(request.body)
        if 'vote' in body:
            user = request.user
            vote = body['vote']
            bug = Bug.objects.get(pk=kwargs['pk'])
            if str(user) not in bug.voters:
                bug.score += vote
                bug.voters.append(user)
                bug.save()
                return HttpResponse('vote counted')
            else:
                return HttpResponse('vote already counted')
        else:
            try:
                if request.user.is_authenticated:
                    bug = Bug.objects.filter(pk=kwargs['pk'])
                    bug.update(**body)
                    return HttpResponse('Resource updated')
                else:
                    return HttpResponse('Not logged in')
            except ObjectDoesNotExist as error:
                return HttpResponse(error)

    def delete(self, request, *args, **kwargs):
        try:
            if request.user.is_authenticated:
                bug = Bug.objects.get(pk=kwargs['pk'], reported_by=request.user)
                bug.delete()
                return HttpResponse('Resource deleted')
            else:
                return HttpResponse('Not logged in')
        except ObjectDoesNotExist as error:
            return HttpResponse(error)

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
