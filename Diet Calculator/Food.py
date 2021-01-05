import Element_Base as E_Base
from Nutrition_Fact import Nutrition_Fact as Fact
import CONSTANTS as CONST
from File_Manager import File as FileType

#name of food
def get_food_info(name):
    file = FileType(CONST.NUTRITION_FILE_NAME, Fact)
    elem = file.get_elem(self.name)
    return elem.get_values()

class Food(E_Base.Element_Base):

    #name - name of food
    #values - [(nutrition fact name, weight), ...]

    def get_values(self):

        file = FileType(CONST.NUTRITION_FILE_NAME, Fact)
        elem = file.get_elem(self.name)
        return elem.get_values()
