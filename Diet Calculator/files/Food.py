from Nutrition_Fact import Nutrition_Fact as NutritionType
import CONSTANTS as CONST
from File_Manager import File as FileType

class Food(E_Base.Element_Base):

    #name - name of food
    #values - [nutrition fact name, weight]

    #returns list of values corresponding to the total nutritional information of the dish
    def get_nutritional_info(self):
        file = FileType(CONST.NUTRITION_FILE_NAME, NutritionType)
        elem = file.get_elem(self.get_values()[0])
        return elem.get_values()