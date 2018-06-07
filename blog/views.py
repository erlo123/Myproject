from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.utils import timezone
from django.views import generic

from .models import Blog, Single
from .forms import CommentForm
# Create your views here.


class BlogView(generic.ListView):
    template_name = 'blog/blog-classic.html'
    context_object_name = 'latest_title_list'


    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

    def get_queryset(self):
        return Blog.objects.filter(
            pub_date__lte=timezone.now()
        ).order_by('-pub_date')



def single(request, title_text_id):
    title = get_object_or_404(Blog, pk=title_text_id)
    template= 'blog/single-post.html'
    return render(request, template, { 'title': title })

def add_comment(request, title_text_id):
    post = get_object_or_404(Blog, pk=title_text_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('single', title_text_id)
    else:
        form = CommentForm()
        template = 'blog/add_comment.html'
        return render(request, template, {'form': form})