# B1. Make a Car class with attributes brand and speed. Add a method show() that prints them nicely.

class Car :

      def __init__(self,brand,speed):

            self.brand = brand
            self.speed= speed

      def show(self):

            print(f'Car brand is {self.brand}, having speed of {self.speed}')


info = Car('Tata',280)

info.show()
                 