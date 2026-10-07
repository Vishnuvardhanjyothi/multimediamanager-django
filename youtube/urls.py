from django.urls import path
from . import views

urlpatterns=[
    path('you/',views.you,name='you'),
    path('media_all/',views.media_all,name='media'),
    path('update/<int:id>/', views.update, name='update'),
    path('delete/<int:id>/',views.delmedia,name='delete'),
    path('single/<int:id>/', views.single_media, name='single'),
]