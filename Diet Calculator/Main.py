import CONSTANTS as CONST
from File_Manager import File as FileType
from Nutrition_Fact import Nutrition_Fact as NutritionType
from Food import Food as FoodType
import sys

class Main:

    def __init__(self):

       self.dict = {"EXIT": self.__EXIT, "N": self.__ADD_NUTRITION}

       self.nuritionFile = FileType(CONST.NUTRITION_FILE_NAME, NutritionType)
       self.foodFile = FileType(CONST.FOOD_FILE_NAME, FoodType)

       while True:

           self.__print_commands()

           #get function call
           inp = input()

           print()

           #run function call
           self.dict.get(inp)()

           print()

    def __print_commands(self):
        
        print("Commands:\n" + 
              "Add a nutritional information: N\n" + 
              "Exit the program: EXIT")

    def __EXIT(self):

        sys.exit()

    def __ADD_NUTRITION(self):

        #get name on nutrition fact
        name = input("Enter nutrition fact name: ")
        print()

        if self.nuritionFile.elem_exists(name):
            print("Nurition fact with this name already exists")
        else:
            #get info
            values = []
            values.append(input("Enter number of calories: "))
            values.append(input("Enter grams of saturated fat: "))
            values.append(input("Enter grams of trans fat: "))
            values.append(input("Enter milligrams of cholesterol: "))
            values.append(input("Enter milligrams of sodium: "))
            values.append(input("Enter grams of fiber: "))
            values.append(input("Enter grams of sugar: "))
            values.append(input("Enter grams of protien: "))

            self.nuritionFile.add_elem(NutritionType(name, values))