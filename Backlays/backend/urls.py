from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns



urlpatterns = [
    path('',views.index, name='index'),
    path('test',views.test, name='sss'),
    path('getSports',views.SportList.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)
