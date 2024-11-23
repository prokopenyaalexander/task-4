purchases = [
    {"item": "apple", "category": "fruit", "price": 1.2, "quantity": 10},
    {"item": "banana", "category": "fruit", "price": 0.5, "quantity": 5},
    {"item": "milk", "category": "dairy", "price": 1.5, "quantity": 2},
    {"item": "bread", "category": "bakery", "price": 2.0, "quantity": 3},
]


def total_revenue(arg):
    # Рассчитайте и верните общую выручку (цена * количество для всех записей).
    tl_revenue = 0
    for item in arg:
        tl_revenue += item["price"] * item["quantity"]

    print(f'Общая выручка: {tl_revenue}')


def items_by_category(arg):
    # Верните словарь, где ключ — категория, а значение — список уникальных товаров в этой категории.
    new_items_by_category = {}
    for item in arg:
        if item["category"] not in new_items_by_category:
            new_items_by_category[item["category"]] = []
        if item["item"] not in new_items_by_category[item["category"]]:
            new_items_by_category[item["category"]].append(item["item"])
    print(f'Товары по категориям: {new_items_by_category}')


def expensive_purchases(arg, min_price=1.0):
    # Выведите все покупки, где цена товара больше или равна min_price.
    purchases_ = []
    for item in arg:
        if item["price"] > min_price:
            purchases_.append(item)
    print(f'Покупки дороже {min_price}: {purchases_}')


def average_price_by_category(arg):
    # Рассчитайте среднюю цену товаров по каждой категории.
    avg_price_by_category = {}
    for item in arg:
        if item["category"] not in avg_price_by_category:
            avg_price_by_category[item["category"]] = round(item["price"] / item["quantity"], 2)
        else:
            avg_price_by_category[item["category"]] += item["price"] / item["quantity"]
    print(f'Товары по категориям: {avg_price_by_category}')

def most_frequent_category(arg):
    # Найдите и верните категорию, в которой куплено больше всего единиц товаров (учитывайте поле quantity).
    new_items_by_category = {}
    for item in arg:
        if item["category"] not in new_items_by_category:
            new_items_by_category[item["category"]] = item["quantity"]
        else:
            new_items_by_category[item["category"]] += item["quantity"]
    keys = new_items_by_category.keys()
    values = new_items_by_category.values()
    quantity_items_by_category = dict(zip(values, keys))
    max_quantity = max(quantity_items_by_category.keys())
    print(f'Категория с наибольшим количеством проданных товаров: {quantity_items_by_category[max_quantity]}')


total_revenue(purchases)
items_by_category(purchases)
expensive_purchases(purchases)
average_price_by_category(purchases)
most_frequent_category(purchases)
