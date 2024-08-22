from django.urls import path

from api_v1.views import add, multiply, subtract, divide, get_csrf_token, index

app_name = 'api_v1'

urlpatterns = [
    path('', index, name='index'),
    path('get-token/', get_csrf_token, name='get_token'),
    path('add/', add, name='echo'),
    path('subtract/', subtract, name='echo'),
    path('multiply/', multiply, name='echo'),
    path('divide/', divide, name='echo'),
]
