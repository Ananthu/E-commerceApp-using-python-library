from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from . import views

urlpatterns = [
    url(r'^$',views.index,name="index"),
    url(r'^(?P<id>\d+)/$',views.detail,name="detail"),
    url(r'^register/$',views.RegistrationView.as_view(), name='registration'),
    url(r'^login/$',views.LoginView.as_view(), name='login'),
	url(r'^logout$',views.logout_view,name="logout"),
	url(r'^add/$', views.PostCreate.as_view(), name='addpost'),
]