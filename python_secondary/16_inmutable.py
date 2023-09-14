items = [
    {
        "product": "camisa",
        "price": 100
    },
    {
        "product": "pantalones",
        "price": 300
    },
    {
        "product": "pantalones 2",
        "price": 200
    }
]

"""
prices = list(map(lambda item: item["price"], items))
print(prices)
print(items)
"""

def add_taxes(item):
    new_item = item.copy()
    item["taxes"] = item["price"] * .19
    return new_item

new_items = list(map(add_taxes, items))

print("new items")
print(new_items)
print(" Old items")
print(items)
