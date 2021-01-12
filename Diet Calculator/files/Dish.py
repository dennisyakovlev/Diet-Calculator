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

        #every second values is the name of a food
        for i in range(0 , len(self.values), 2):
            
            #get food
            food = file.get_elem(self.values[i])

            #nutritional info
            nutritionalInfo = NutritionType("", food.get_nutritional_info())

            #how many more times than 100g there is
            multiplier = float(self.values[i + 1]) / 100

            factInfo = NutritionType("", fact) + NutritionType("", nutritionalInfo * multiplier)

        return factInfo



