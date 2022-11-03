from django.shortcuts import render
from .models import HomeBg, Post
from django.views.generic import ListView
# Create your views here.

class HomeListView(ListView):
    template_name = 'index.html'

    def get(self, request):
        homebg = HomeBg.objects.all()
        post = Post.objects.all()
        return render(request, self.template_name, {'homebg':homebg, 'post':post})


