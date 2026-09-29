class MenuItem:

      def __init__(self,name,price):

            self.name=name
            self.price=price

class Restaurant:

      def __init__(self,name):
              self.name=name
              self.menu=[]         

      def add_dish(self,item):
             self.menu.append(item)

      def show_menu(self):

             for item in self.menu:
                    print(f"{item.name} - ₹{item.price}")               


class order:

       def __init__(self,customer):
              self.customer=customer
              self.items=[]

       def add_item(self,item) :

              self.items.append(item)
              print(f'Added {item.name}')

       def total(self):

              return sum(item.price for item in self.items)  



pizza=MenuItem('Pizza',250)

coke = MenuItem('Cock',60)


r = Restaurant('Pizza Hut')
r.add_dish(pizza)
r.add_dish(coke)

print(f"{r.name} Menu")

r.show_menu()


print('––––––––––––––––––––––––––––––––––––––––––––––––')


order = order('Abhishek')

print(f'Customer Name :{order.customer}')

order.add_item(r.menu[0])
order.add_item(r.menu[1])

print(f'Total : ₹{order.total()}')


#       OUT PUT :-

#   Pizza Hut Menu                                 
# Pizza - ₹250
# Cock - ₹60
# ––––––––––––––––––––––––––––––––––––––––––––––––
# Customer Name :Abhishek
# Added Pizza
# Added Cock
# Total : ₹310
             



