from django.urls import path
from . import views
app_name="friends"
urlpatterns=[
path('fb',views.fb,name='fb')
]