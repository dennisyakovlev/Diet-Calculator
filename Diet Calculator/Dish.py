import Element_Base as E_Base
from Food import Food as FoodType
from Nutrition_Fact import Nutrition_Fact as NutritionType
from File_Manager import File as FileType
import CONSTANTS as CONST

class Dish(E_Base.Element_Base):

    #name - name of dish
    #not actual tuples
    #values - [(food name, weight), (food name, weight), ...]

    #FINISH
    def get_nutritional_info(self):

        file = FileType(CONST.FOOD_FILE_NAME, FoodType)

        #get a nutritional info and its length then create list of 0's of the length got
        fact = [ 0 * item for item in range( len( file.get_elem(self.values[0]).get_nutritional_info() ) ) ]

        for i in range(0 , len(self.values), 2):
            
            #get food
            food = file.get_elem(self.values[i])

            #nutritional info
            nutritionalInfo = NutritionType("", food.get_nutritional_info())

            #how many more times than 100g there is
            multiplier = float(self.values[i + 1]) / 100

            fact = NutritionType("", fact) + NutritionType("", nutritionalInfo * multiplier)

        return fact



