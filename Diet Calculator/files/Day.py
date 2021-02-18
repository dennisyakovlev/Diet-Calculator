import CONSTANTS as CONST
from File_Manager import File as FileType
from Dish import Dish as DishType
import Element_Base as E_Base
from Nutrition_Fact import Nutrition_Fact as NutritionType

class Day(E_Base.Element_Base):

    #name - name of day
    #values - [name of dish, name of dish, ...]

    #returns list of values corresponding to the total nutritional information in the day
    def get_nutritional_info(self):

        file = FileType(CONST.DISH_FILE_NAME, DishType)

        #create list of 0's of length dependant on number of elements
        #in a nutritional information
        #                                 {     get first dish elem    } { get the info list  }
        factInfo = [ 0 for _ in range( len(file.get_elem(self.values[0]).get_nutritional_info()) ) ]

        #for each name of the dishes that make up the day
        for item in self.values:
            #get dish
            dish = file.get_elem(item)
            
            #add to total
            factInfo = NutritionType("", factInfo) + NutritionType("", dish.get_nutritional_info())

        return factInfo