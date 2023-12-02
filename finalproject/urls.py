from django.contrib import admin
from django.urls import path
from myapp import views  
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

 
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),  
    path('add',views.add, name='add'),
    path('login.html',views.loginPage, name='login'),   
    path('logout/',views.logoutUser, name='logout'),  
    path('register.html',views.register, name='register'),    
    path('show.html',views.show, name='show'),  
    path('home.html',views.home, name='home'),  
    path('edit/<int:id>', views.edit, name='edit'),  
    path('update/<int:id>', views.update, name='update'),  
    path('delete/<int:id>', views.destroy, name='destroy'),  
    
]

urlpatterns += staticfiles_urlpatterns()
