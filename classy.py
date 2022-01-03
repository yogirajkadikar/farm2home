# class Store:
#     def __init__(self, name, items):
#         self.name = name
#         self.items = []
#     def add_item(self, name, price):
#         item = {"name": name, "price": price}
#         self.items.append(item)
#     def stock_price(self):
#         return sum([item["price"] for item in self.items])
#         # total = 0
#         # for item in self.items:
#         #     total+= item["price"]
#         # return total

class ClassTest:
    def instance_method(self):
        print(f'Called instance method of {self}')

test = ClassTest()

test.instance_method()
