
from users.views import display,register
from . import views
from django.urls import path
from django.conf.urls import url,include
urlpatterns=[
	path('display/',views.display,name='display'),
	url(r"^accounts/",include("django.contrib.auth.urls")),
	url(r"^register/",register,name="register"),
	path('setcookie',views.setcookie,name='setcookie'),
	path('getcookie',views.showcookie,name='showcookie'),
	path('setsession',views.create_session),
	path('getsession',views.get_session)

]