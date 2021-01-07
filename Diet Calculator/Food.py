import Element_Base as E_Base
from Nutrition_Fact import Nutrition_Fact as Fact
import CONSTANTS as CONST
from File_Manager import File as FileType

#food - type of food
def get_food_info(food):
    file = FileType(CONST.NUTRITION_FILE_NAME, Fact)
    elem = file.get_elem(food.get_values()[0])
    return elem.get_values()

class Food(E_Base.Element_Base):

    #name - name of food
    #values - [(nutrition fact name, weight), ...]

    pass
