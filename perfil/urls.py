from django.urls import path
from .views import CreateImageUserView, ListImageUserView


urlpatterns = [
    path('show/', ListImageUserView.as_view(), name='show_user'),
    path('new/', CreateImageUserView.as_view(), name='new_image'),
]