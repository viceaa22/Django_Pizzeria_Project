from django.urls import path

from . import views

app_name = 'pizzas'
urlpatterns = [
    # Home page
    path('', views.index, name='index'),
    # Page that shows all topics.
    path('pizzas/', views.pizzas, name='pizzas'),
    # Detail page for a single topic.
    path('pizzas/<int:pizza_id>/', views.pizza, name='pizza'),
    # Page for adding a new topic
    path('new_pizza/', views.new_pizza, name='new_pizza'),
    # Page for adding a new entry
    path('new_topping/<int:pizza_id>/', views.new_topping, name='new_topping'),
    # Page for editing an entry.
    path('edit_topping/<int:topping_id>/', views.edit_topping, name='edit_topping'),
]
