 orders = [
    {"item": "pen", "quantity": 3},
    {"item": "book", "quantity": 2},
    {"item": "pen", "quantity": 4},
    {"item": "pencil", "quantity": 5}
]

dic= {}
for order in orders:
    item = order["item"]
    dic[item] = dic.get(item, 0) + order["quantity"]

print(dic)
