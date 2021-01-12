import Element_Base as E_Base
from Nutrition_Fact import Nutrition_Fact as Fact
import CONSTANTS as CONST
from File_Manager import File as FileType

class Food(E_Base.Element_Base):

    #name - name of food
    #values - [nutrition fact name, weight]

    #return list of values from nutrition info
    def get_nutritional_info(self):
        file = FileType(CONST.NUTRITION_FILE_NAME, Fact)
        elem = file.get_elem(self.get_values()[0])
        return elem.get_values()