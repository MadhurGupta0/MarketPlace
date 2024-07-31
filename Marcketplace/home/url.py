from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import index,contact,base,detail,signup,new,dashboard,delete,edit,item,new_coversation,Inbox,det,lout
from django.contrib.auth import views as auth_views
from .forms import LoginForm

urlpatterns = [
    path('', index,  name='index'),
    path('item/',item,name='items'),
    path('new/',new, name="new"),
    path('dashboard',dashboard, name="dashboard"),
    path('contact/', contact,  name='contact/'),
    path('base',base, name="base"),
    path('signup/',signup, name="signup"),
    path('login/',auth_views.LoginView.as_view(authentication_form=LoginForm,template_name="login.html"), name="login"),
    path('<int:pk>/',detail, name="detail"),
    path('<int:pk>/delete/',delete, name='delete'),
    path('<int:pk>/edit/',edit,name='edit'),
    path('conversation/<int:pk>/',new_coversation,name="new"),
    path('inbox/',Inbox,name="inbox"),
    path('messages/<int:pk>/',det,name="messages"),
    path('logout/',lout,name="logout")
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

