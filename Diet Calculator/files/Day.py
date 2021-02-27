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

        factInfo = [0 for _ in range(CONST.NUTRITION_ITEMS)]

        self.__remove_noexist_dish()

        #for each name of the dishes that make up the day
        for item in self.values:
            #get dish
            dish = file.get_elem(item)

            #add to total if dish get was successful
            factInfo = NutritionType("", factInfo) + NutritionType("", dish.get_nutritional_info())

        return factInfo

    #remove any dishes that dont exist from this dish
    def __remove_noexist_dish(self):
        dish_file = FileType(CONST.DISH_FILE_NAME, DishType)
        
        new_values = []
        #go through all foods in this dish
        for item in self.values:
            #check if food exists
            if dish_file.elem_exists(item):
                new_values.append(item)
        
        #all the missing foods
        missing = list(set(self.values) - set(new_values))
        if len(missing) != 0:
            #remove the corresponding dish
            for dish in missing:
                index = self.values.index(dish)
                self.values.pop(index)

            day_file = FileType(CONST.DAY_FILE_NAME, Day)
            day_file.remove_elem(self.name)
            day_file.add_elem(Day(self.name, self.values))