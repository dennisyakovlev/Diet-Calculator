import Element_Base as E_Base
from Food import Food as FoodType

class Dish(E_Base.Element_Base):

    #name - name of dish
    #values - [(food name, weight), (food name, weight), ...]

    def get_nutritional_info(self):

        foods = []
        for i in range(0 , len(self.values), 2):
            foods.append(self.values[i])

