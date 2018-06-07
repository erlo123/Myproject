from django.urls import path

from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('email/', views.emailView, name='email'),
    path('success/', views.successView, name='success'),
    path('<int:title_id>/', views.image, name='image'),
]