
from django.urls import path
from .views import current_user, UserList, temperature_list

urlpatterns = [
    path('current_user/', current_user),
    path('users/', UserList.as_view()),
    path('temperature/', temperature_list),
]