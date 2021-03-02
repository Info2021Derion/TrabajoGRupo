
from django.urls import path
from . import views
from . views import *

# Un home esta de mas, nuevo y crear hacen lo mismo, dejo crear porque se usa la clase
urlpatterns = [
  path('', Home.as_view(), name = 'home'),
  #path('home/', Home.as_view(), name = 'home'),
  path('posts/<int:pk>', post , name = 'posts'),
  path('crear/', views.Alta_post.as_view(), name = 'alta_post'),
  #path('nuevo/', post_nuevo, name = 'nuevo'),
  path('editar/<int:pk>/',views.Editar_post.as_view(), name= 'editar'),
  path('eliminar/<int:pk>/',views.Eliminar_post.as_view(), name= 'eliminar'),
]