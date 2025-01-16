from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('delete/<int:id>/',views.delete,name='delete'),
    path('update/<int:id>/',views.update,name='update'),
    path('show/',views.show,name='show'),
    path('login/',views.login_page,name='login'),
    path('register/',views.register,name='register'),
    path('logout/',views.logout_page,name="logout"),
]
