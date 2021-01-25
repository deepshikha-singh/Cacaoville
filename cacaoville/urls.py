from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.conf import settings
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('about-cacaoville', views.about, name='about'),
    path('cacaoville-product', views.product, name='product'),
    path('contact-cacaoville', views.contact, name='contact'),
    path('register-into-cacaoville', views.signup, name='signup'),
    path('login-into-cacaoville', views.signin, name='signin'),
   
    
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)