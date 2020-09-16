from django.shortcuts import render
from django.shortcuts import HttpResponse,get_list_or_404
from coffee.models import Product, Pods, Machines
from django.http import JsonResponse

pods_options = [['large coffee pod', 'small coffee pod','espresso pod'],
           ['vanila', 'caramel', 'psi','mocha', 'hazelnut'],
            ['1 dozen', '3 dozen','5 dozen', '7 dozen']]
machines_options = [['espresso machine', 'large machine', 'small machine'],
                    ['base model', 'premium model', 'deluxe model']]

check3 = ['pods', 'coffee_flavor', 'pack_size']
check4 = ['machines', 'coffee_flavor']




# main coffee list
def machine_home(request):
    machines = Machines.objects.all().values()
    machines = list(machines)
    return JsonResponse(machines, safe=False)


# main pod list
def pod_home(request):
    pods = Pods.objects.all().values()
    pods = list(pods)
    return JsonResponse(pods, safe=False)


#machine filters
def check_machine(request):
    machines = Machines.objects.all()
    machine = []

    for y, z in zip(machines_options, check4):
        for i in y:
            req = request.POST.get(i)
            
            if req:
                machines = machines.filter(**{z: i})
                machine = machines
    
    machines = []
    for m in machine:
        machines.append(m.product.model)
    return JsonResponse(machines, safe=False)


#pod filters
def check_pod(request):
    pods = Pods.objects.all()
    pod = []
    for y, z in zip(pods_options, check3):
        for i in y:
            req = request.POST.get(i)
            if req:
                pods = pods.filter(**{z: i})
                pod = pods
    pods= []
    for p in pod:
        pods.append(p.product.model)
    return JsonResponse(pods, safe=False)
