# 2.Create a Rectangle class with width and height. Add methods area() and perimeter().


class Rectangle:

      def __init__(self,width,hight):

            self.width=width
            self.hight=hight

      def area(self):

            areaR =   self.width *self.hight

            return areaR

      def perimeter(self):

            perimeterR= 2*( self.width + self.hight)

            return perimeterR
       
result = Rectangle(10,45)

print(result.area())
print(result.perimeter())