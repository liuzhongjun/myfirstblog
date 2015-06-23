# I just kept the original codes above and commented them out.
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.post_list),
]
