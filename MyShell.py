import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "pizzeria.settings")

import django
django.setup()

from pizzas.models import Pizza

pizza = Pizza.objects.all()

for pizza in pizzas:
    print(pizza.id, pizza)

t = Pizza.objects.get(id=1)
print(t.name)
print(t.date_added)

toppings = t.topping_set.all()

for topping in toppings:
    print(topping)
    