""""
Funkcja filter() w języku Python jest wbudowaną funkcją 
służącą do filtrowania elementów z sekwencji (np. listy) 
na podstawie określonego warunku.
"""
# Potrzebujesz wybrać tylko te procesory, które mają więcej niż 8 rdzeni
processors = [
    {'model': 'Intel Core i5-11600K', 'cores': 6},
    {'model': 'AMD Ryzen 5 5600X', 'cores': 6},
    {'model': 'Intel Core i9-11900K', 'cores': 8},
    {'model': 'AMD Ryzen 9 5900X', 'cores': 12},
    {'model': 'Intel Xeon W-3175X', 'cores': 28},
]

processors_filter = list(filter(lambda x: x['cores'] > 8, processors))

print(processors_filter)

print('---')

# Potrzebujesz wybrać tylko te zamówienia, które nie zostały jeszcze wysłane - mają status 'processing'
orders = [
    {'id': 1, 'product': 'laptop', 'status': 'processing'},
    {'id': 2, 'product': 'smartphone', 'status': 'shipped'},
    {'id': 3, 'product': 'tablet', 'status': 'processing'},
    {'id': 4, 'product': 'headphones', 'status': 'processing'},
    {'id': 5, 'product': 'monitor', 'status': 'shipped'},
]

orders_process = list(filter(lambda x: x['status'] == 'processing', orders))
print(orders_process)

print('---')

# Potrzebujesz wybrać tylko te produkty, które mają cenę powyżej 500, 
# należą do kategorii 'computers' i są dostępne w magazynie - klucz 'in_stock': True
products = [
    {
        'id': 1,
        'name': 'laptop',
        'category': 'computers',
        'price': 2000,
        'in_stock': True,
    },
    {
        'id': 2,
        'name': 'smartphone',
        'category': 'electronics',
        'price': 1000,
        'in_stock': True,
    },
    {
        'id': 3,
        'name': 'book',
        'category': 'books',
        'price': 50,
        'in_stock': False,
    },
    {
        'id': 4,
        'name': 'monitor',
        'category': 'computers',
        'price': 500,
        'in_stock': True,
    },
    {
        'id': 5,
        'name': 'headphones',
        'category': 'electronics',
        'price': 100,
        'in_stock': False,
    },
]

products_filter = list(filter(lambda x: x['price'] >= 500 and x['category'] == 'computers' and x['in_stock'] == True, products))

print(products_filter)

print('---')

# Potrzebujesz wybrać tylko te produkty, które są bezglutenowe, 
# wegańskie i mają mniej niż 100 kalorii na porcję. 
foods = [
    {
        'name': 'buckwheat',
        'gluten_free': True,
        'vegan': True,
        'calories': 90,
    },
    {
        'name': 'bulgur',
        'gluten_free': True,
        'vegan': True,
        'calories': 120,
    },
    {
        'name': 'natural yogurt',
        'gluten_free': True,
        'vegan': False,
        'calories': 70,
    },
    {
        'name': 'cashew nuts',
        'gluten_free': True,
        'vegan': True,
        'calories': 150,
    },
    {
        'name': 'cottage cheese',
        'gluten_free': False,
        'vegan': False,
        'calories': 80,
    },
    {
        'name': 'tofu',
        'gluten_free': True,
        'vegan': True,
        'calories': 70,
    },
    {
        'name': 'rice',
        'gluten_free': True,
        'vegan': True,
        'calories': 130,
    },
    {
        'name': 'wheat bread',
        'gluten_free': False,
        'vegan': True,
        'calories': 150,
    },
]

food_filter = list(filter(lambda x: x['gluten_free'] == True and x['vegan'] == True and 100 > x['calories'], foods))

print(food_filter)

print('---')

# Potrzebujesz wydobyć nazwy domów, których średnia miesięczna zużycia 
# energii dla drugiej połowy roku (ostatnie 6 wartości w każdej liście z pomiarami) jest mniejsza niż 1900 kWh. 
energy_usage = [
    (
        'House A',
        [
            1200,
            1300,
            1400,
            1500,
            1600,
            1700,
            1800,
            1900,
            2000,
            2100,
            2200,
            2300,
        ],
    ),
    (
        'House B',
        [
            1100,
            1200,
            1300,
            1400,
            1500,
            1600,
            1700,
            1800,
            1900,
            2000,
            2100,
            2200,
        ],
    ),
    (
        'House C',
        [
            1000,
            1100,
            1200,
            1300,
            1400,
            1500,
            1600,
            1700,
            1800,
            1900,
            2000,
            2100,
        ],
    ),
    (
        'House D',
        [
            900,
            1000,
            1100,
            1200,
            1300,
            1400,
            1500,
            1600,
            1700,
            1800,
            1900,
            2000,
        ],
    ),
]

def average_second_half_year(usage):
    return sum(usage[1][6:]) / 6 < 1900

energy_usage_filter = list(filter(average_second_half_year, energy_usage))
final_result = [house [0] for house in energy_usage_filter]
print(final_result[0])
print(final_result[1])