# coding: utf-8
from django.conf.urls import patterns, url
#from accounts import views
from accounts.forms import LoginForm, PasswordChangeForm

urlpatterns = patterns('',
    url(r'^login/$', 'django.contrib.auth.views.login',
        {'authentication_form': LoginForm, 'template_name': 'accounts/login.html'}, name='login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout',
        {'next_page': '/accounts/login/'}, name='logout'),
    url(r'^password_change/$', 'django.contrib.auth.views.password_change',
        {'template_name': 'accounts/password_change.html',
         'post_change_redirect': '/accounts/passwordchangedone/',
         'password_change_form': PasswordChangeForm},
        name='password_change'),
    url(r'^password_change_done/$',
        'django.contrib.auth.views.password_change_done',
        {'template_name': 'accounts/password_change_done.html', },
        name='password_change_done'),
#    url(r'^profile/$', views.ProfileView.as_view(), name='profile'),
#    url(r'^register/$', views.RegisterView.as_view(), name='register')
)

