from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('kniha', views.KnihaListView.as_view(), name='list'),
    path('kniha/<int:pk>/', views.KnihaDetailView.as_view(), name='detail'),
    path('kniha/create/', views.KnihaCreate.as_view(), name='kniha-create'),
    path('kniha/<int:pk>/update/', views.KnihaUpdate.as_view(), name='kniha-update'),
    path('kniha/<int:pk>/delete/', views.KnihaDelete.as_view(), name='kniha-delete'),
]