from django.conf.urls import url

from accounts.views import loginview, auth_and_login, sign_up_in

urlpatterns = [
                       url(r'^login/', loginview),
                       url(r'^auth/', auth_and_login),
                       url(r'^signup/', sign_up_in),
                       ]
