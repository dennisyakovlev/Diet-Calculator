import CONSTANTS as CONST
from File_Manager import File as FileType
from Nutrition_Fact import Nutrition_Fact as NutritionType
from Food import Food as FoodType
import sys

class Main:

    def __init__(self):
        
       self.commands = ["EXIT", "NUTRITION", "FOOD"]
       self.dict = {self.commands[0]: self.__EXIT, self.commands[1]: self.__NUTRITION}

       self.nuritionFile = FileType(CONST.NUTRITION_FILE_NAME, NutritionType)
       self.foodFile = FileType(CONST.FOOD_FILE_NAME, FoodType)

       while True:

           self.__print_commands()

           #get function call
           inp = input()

           print()

           #run function call
           self.dict[inp]()

           print()

    def __print_commands(self):
        
        print("Commands:\n" + 
              "Add a nutritional information: " + self.commands[1] + "\n" + 
              "Exit the program: " + self.commands[0])

    def __EXIT(self):

        sys.exit()

    def __NUTRITION(self):
        
        inp = input("Remove nutrition fact: REMOVE\n" +
                     "Add nutrition fact: ADD\n" +
                     "Get nutrition fact info: GET\n")

        print()

        name = input("Enter nutrition fact name: ")

        if inp == "REMOVE":
            self.__DELETE_NUTRITION(name)
        elif inp == "ADD":
            self.__ADD_NUTRITION(name)
        elif inp == "GET":
            self.__GET_NUTRITION(name)
            
    def __GET_NUTRITION(self, name):

        if not self.nuritionFile.elem_exists(name):
            print("Nurition fact with this name does not exist")
        else:
            self.nuritionFile.get_elem(name)

    def __DELETE_NUTRITION(self, name):
        
        if not self.nuritionFile.elem_exists(name):
            print("Nurition fact with this name does not exist")
        else:
            self.nuritionFile.remove_elem(name)

    def __ADD_NUTRITION(self, name):

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