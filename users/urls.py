from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('login', views.login, name='login'),
    path('index', views.index, name='index'),
    path('lenditems', views.lenditems, name='lenditems'),
    path('additems', views.additems, name='additems'),
    path('lentlist', views.lentlist, name='lentlist'),
    path('returnitems', views.returnitems, name='returnitems'),
    path('<int:_id>/lenditem', views.lenditem, name='lenditem'),

]
