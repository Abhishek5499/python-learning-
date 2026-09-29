class Employee:

      def __init__(self,name,salary):
            self.name=name
            self.salary=salary
      def show(self):


            print(f'{self.name} with ₹{self.salary}')


class Manager(Employee):

      def __init__(self,name,salary,team):

            super().__init__(name,salary)

            self.team =team

      def show(self):
            super().show() 

            print(f'Manager with team member :{self.team}')     

e=Employee('Abhisek',50000)
e.show()

m=Manager("Abhishek",55000,8)

m.show()

           