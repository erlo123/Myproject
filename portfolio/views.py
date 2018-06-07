from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.core.mail import send_mail, BadHeaderError
from django.utils import timezone
from django.views import generic

from .models import Pics
from .forms import ContactForm
from blog.models import Blog

class IndexView(generic.ListView):
    template_name = 'portfolio/index.html'
    context_object_name = 'latest_pics_list'


    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context.update({'latest_blog_list': Blog.objects.filter(pub_date__lte=timezone.now()
        ).order_by('-pub_date')[:3],})
        return context

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

    def get_queryset(self):
        return Pics.objects.filter(
            pub_date__lte=timezone.now()
        ).order_by('-pub_date')

def image(request, title_id):
    pic = Pics.objects.get(pk = title_id)
    return render(request, 'portfolio/img.html', {'pic': pic })

def emailView(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']
            try:
                send_mail(subject, from_email, subject, ['admin@example.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('success')
    return render(request, "portfolio/contact2w.html", {'form': form})

def successView(request):
    return HttpResponse('Sukces! Wiadomosc zostala wyslana.')

