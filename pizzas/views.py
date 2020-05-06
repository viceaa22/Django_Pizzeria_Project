from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from django.http import Http404

from .models import Pizza, Topping
from .forms import PizzaForm, ToppingForm

def index(request):
    return render(request, 'pizzas/index.html')

@login_required
def pizzas(request):
    
    pizzas = Pizza.objects.filter(owner=request.user).order_by('date_added')
    context = {'pizza': pizzas}
    return render(request, 'pizzas/pizzas.html', context)

@login_required
def pizza(request, pizza_id):
    pizza = Pizza.objects.get(id=pizza_id)
    if pizza.owner != request.user:
        raise Http404
    
    toppings = pizza.topping_set.order_by('-date_added')
    context = {'pizza': pizza, 'toppings': toppings}
    return render(request, 'pizzas/topic.html', context)

@login_required
def new_pizza(request):
    if request.method != 'POST':
        # No data submitted; create a blank form.
        form = PizzaForm()
    else:
        # POST data submitted; process data.
        form = PizzaForm(data=request.POST)
        if form.is_valid():
            new_pizza = form.save(commit=False)
            new_pizza.owner = request.user
            new_pizza.save()
            return redirect('pizzas:topics')

    # Display a blank or invalid form.
    context = {'form': form}
    return render(request, 'pizzas/new_pizza.html', context)

@login_required
def new_topping(request, pizza_id):
    pizza = Pizza.objects.get(id=pizza_id)

    if request.method != 'POST':
        # No data submitted; create a blank form.
        form = ToppingForm()
    else:
        # POST data submitted; process data.
        form = ToppingForm(data=request.POST)
        if form.is_valid():
            new_topping = form.save(commit=False)
            new_topping.pizza = pizza
            new_topping.save()
            return redirect('pizzas:pizza', pizza_id=pizza_id)

    # Display a blank or invalid form.
    context = {'pizza': pizza, 'form': form}
    return render(request, 'pizzas/new_topping.html', context)

@login_required
def edit_topping(request, topping_id):
    topping = Topping.objects.get(id=topping_id)
    pizza = topping.pizza
    if pizza.owner != request.user:
        raise Http404
    
    if request.method != 'POST':
        # Initial request; pre-fill form with the current entry.
        form = ToppingForm(instance=topping)
    else:
        # POST data submitted; process data.
        form = ToppingForm(instance=topping, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('pizzas:pizza', pizza_id=pizza.id)
    
    context = {'topping': topping, 'pizza': pizza, 'form': form}
    return render(request, 'pizzas/edit_topping.html', context)

