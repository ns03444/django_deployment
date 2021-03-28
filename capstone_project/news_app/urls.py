from django.conf.urls import url
from news_app import views
urlpatterns = [
    url(r'', views.index, name='index'),

]
