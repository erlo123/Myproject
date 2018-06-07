from django.urls import path

from . import views

urlpatterns = [
    path('', views.BlogView.as_view(), name='blog'),
    path('<int:title_text_id>/', views.single, name='single'),
    path('<int:title_text_id>/comment/', views.add_comment, name='add_comment')
]