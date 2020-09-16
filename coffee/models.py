
from django.db import models

# Create your models here.


class Product(models.Model):
    model = models.CharField(max_length=200)

    def __str__(self):
        return self.model


class Pods(models.Model):
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE)
    #size
    large = 'large coffee pod'
    small = 'small coffee pod'
    espresso = 'espresso pod'

    #flavor
    caramel= 'caramel'
    psi = 'psi'
    hazelnut = 'hazelnut'
    mocha= 'macha'
    vanila ='vanila'

    #pack size
    one = '1 dozen'
    three = '3 dozen'
    five = '5 dozen'
    seven= '7 dozen'
    #machine &product type
    pod = [
        (large, 'large coffee pod'),
        (small, 'small coffee pod'),
        (espresso, 'espresso pod'),
        ]
    #flavor
    flavor =[
        (vanila, 'vanila'),
        (caramel, 'caramel'),
        (psi,'psi'),
        (mocha, 'mocha'),
        (hazelnut, 'hazelnut'),

        ]
    #pack size
    pack=[
        (one, '1 dozen'),
        (three, '3 dozen'),
        (five, '5 dozen'),
        (seven, '7 dozen'),
    ]

  
    pods = models.CharField(max_length=20, choices=pod)
    coffee_flavor = models.CharField(max_length=20, choices=flavor )
    pack_size = models.CharField(max_length=20, choices=pack)
    product_name = models.CharField(max_length=200)
    def __str__(self):
        return self.product_name


class Machines(models.Model):
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE)
    #machines
    espresso_machine = 'espresso machine'
    large_machine = 'large machine'
    small_machine = 'small machine'

    machine = [(espresso_machine, 'espresso machine'),
               (large_machine, 'large machine'),
               (small_machine, 'small machine'), ]
    #flavor
    base = 'base model'
    premium = 'premium model'
    deluxe = 'deluxe model'

    flavor = [(base, 'base model'),
              (premium, 'premium model'),
              (deluxe, 'deluxe model')]



    machines = models.CharField(max_length=20, choices=machine)
    coffee_flavor = models.CharField(max_length=20, choices=flavor )
    water_line_compatible = models.BooleanField()
    product_name = models.CharField(max_length=200)

    def __str__(self):
        return self.product_name
