from django.shortcuts import render
from django.views import View
# Create your views here.

class BugView(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'bugs/bugs.html')