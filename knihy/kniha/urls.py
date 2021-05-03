from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('list', views.KnihaListView.as_view(), name='list'),
    path('detail/<int:pk>/', views.KnihaDetailView.as_view(), name='detail'),
]