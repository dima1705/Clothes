from django.urls import path, include

from users.views import login, registration

app_name = 'users'

urlpatterns = [
    path('lorin/', login, name='login'),
    path('registration/', registration, name='registration'),
]