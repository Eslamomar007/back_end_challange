from django.urls import path
from coffee.views import machine_home, pod_home, check_pod, check_machine

urlpatterns = [

    path('machines', machine_home, name='machine_home'),
    path('pods', pod_home, name='pod_home'),
    path('check-pod', check_pod, name='check_pod'),
    path('check-machine', check_machine, name='check_machine'),
]
