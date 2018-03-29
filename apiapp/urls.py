from django.conf.urls import url, include

from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.authtoken.views import obtain_auth_token

from .views import (
    CreateView,
    DetailsView,
    UserView,
    UserDetailsView,
    BucketView
    )
#  create_user, update_user, delete_user




urlpatterns = {
    url(r'^bucketlists/$', CreateView.as_view(), name="create"),

    url(r'^bucketlists/(?P<pk>[0-9]+)/$', DetailsView.as_view(), name="details"),

    url(r'^buck/', BucketView.as_view(), name="Bucket"),

    url(r'^auth/', include('rest_framework.urls', namespace='rest_framework')),

    url(r'^users/$', UserView.as_view(), name="users"),

    # url(r'^users/new', create_user, name="Nuevo_usuario"),

    # url(r'^users/delete/(?P<pk>[0-9]+)/$', delete_user, name="Borrar_usuario"),

    url(r'users/(?P<pk>[0-9]+)/$', UserDetailsView.as_view(), name="user_crud"),

    # url(r'users/update/(?P<pk>[0-9]+)/$', update_user, name="user_update"),

    url(r'^get-token/', obtain_auth_token),
}

urlpatterns = format_suffix_patterns(urlpatterns)