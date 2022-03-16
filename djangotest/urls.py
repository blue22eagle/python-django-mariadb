from django.contrib import admin
from django.urls import path#, re_path
from myapp import views
admin.autodiscover()

urlpatterns= [
   #re_path(r'^$', views.hello, name= 'hello'),
   path('', views.hello, name= 'hello'),
   #re_path(r'^admin/', admin.site.urls),
   path('admin', admin.site.urls),
   #re_path(r'^hello/', views.hello, name= 'hello'),
   path('hello/', views.hello, name= 'hello'),
   #re_path(r'^add/', views.add, name= 'add'),
   path('add/', views.add, name= 'add'),
   #re_path(r'^show/', views.show, name= 'show'),
   path('show/', views.show, name= 'show'),
   #re_path(r'^update/<int:id>', views.update, name= 'update'),
   path('update/<int:id>', views.update, name= 'update'),
   #url(r'^delete/<int:id>', views.delete, name= 'delete'),
   path('delete/<int:id>', views.delete, name= 'delete'),
]
