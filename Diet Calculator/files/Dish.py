import Element_Base as E_Base
from Food import Food as FoodType
from Nutrition_Fact import Nutrition_Fact as NutritionType
from File_Manager import File as FileType
import CONSTANTS as CONST

class Dish(E_Base.Element_Base):

    #name - name of dish
    #values - [food name, weight, food name, weight, ...]

    #returns list of values corresponding to two added nutritional informations
    def __add__(self, other):

        return self.get_nutritional_info() + other.get_nutritional_info()

    #returns list of values corresponding to the total nutritional information of the dish
    def get_nutritional_info(self):

        file = FileType(CONST.FOOD_FILE_NAME, FoodType)

        #create list of 0's of length dependant on number of elements
        #in a nutritional information
        #                                 {     get first food elem    } { get the info list  }
        factInfo = [ 0 for _ in range( len(file.get_elem(self.values[0]).get_nutritional_info()) ) ]

        self.__remove_noexist_food()

        #every second values is the name of a food
        for i in range(0 , len(self.values), 2):
            
            #get food
            food = file.get_elem(self.values[i])

            #nutritional info
            nutritionalInfo = NutritionType("", food.get_nutritional_info())

            #how many more times than 100g there is
            multiplier = float(self.values[i + 1]) / 100

            factInfo = NutritionType("", factInfo) + NutritionType("", nutritionalInfo * multiplier)

        return factInfo

    #remove any foods that dont exist from this dish
    def __remove_noexist_food(self):
        food_file = FileType(CONST.FOOD_FILE_NAME, FoodType)
        
        new_values = []
        #go through all foods in this dish
        for i in range(0, len(self.values), 2):
            #check if food exists
            if food_file.elem_exists(self.values[i]):
                new_values.append(self.values[i])
        
        #all the missing foods
        missing = list(set([self.values[i] for i in range(0, len(self.values), 2)]) - set(new_values))
        if len(missing) != 0:
            #remove the corresponding food and weight of it
            for food in missing:
                index = self.values.index(food)
                self.values.pop(index)
                self.values.pop(index)

            dish_file = FileType(CONST.DISH_FILE_NAME, Dish)
            dish_file.remove_elem(self.name)
            dish_file.add_elem(Dish(self.name, self.values))




