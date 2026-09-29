class car :
    def set_details(self,brand,model):
        self.brand = brand
        self.model = model

    def show_details(self):
        print(f'The car Brand is {self.brand} and the Model of car is {self.model}')

car1 = car()

car1.set_details('tesla','2026')

car1.show_details()