expected_size = int(input("Введите количество товаров: "))
product_list = []
while expected_size > len(product_list):
    name = input("Введите название товара: ")
    cost = int(input("Введите цену товара: "))
    amount = int(input("Введите количество данного товара: "))
    unit = input("Введите единицу измерения данного товара: ")
    each_product = (len(product_list) + 1, {"название": name, "цена": cost, "количество": amount, "ед": unit})
    product_list.append(each_product)
    print('_' * 50)
print(product_list)
names = set()
costs = set()
amounts = set()
units = set()
for product in product_list:
    names.add(product[1]["название"])
    costs.add(product[1]["цена"])
    amounts.add(product[1]["количество"])
    units.add(product[1]["ед"])
analytics_dict = {
    "название": list(names),
    "цена": list(costs),
    "количество": list(amounts),
    "ед": list(units)
}
print(analytics_dict)
