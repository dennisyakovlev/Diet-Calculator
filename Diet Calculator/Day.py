import Element_Base as E_Base
import CONSTANTS as CONST
from File_Manager import File as FileType
from Dish import Dish as DishType
from Nutrition_Fact import Nutrition_Fact as NutritionType

class Day(E_Base.Element_Base):

    #name - name of day
    #values - [name of dish, name of dish, ...]

    #returns list of values corresponding to nutritional information
    def get_nutritional_info(self):

        file = FileType(CONST.DISH_FILE_NAME, DishType)

        fact = [ 0 * item for item in range(len(file.get_elem(self.get_values()[0]).get_nutritional_info())) ]

        #for each name of the dishes that make up the day
        for item in self.values:

            #get dish
            dish = file.get_elem(item)

            fact = NutritionType("", fact) + NutritionType("", dish.get_nutritional_info())

        return fact