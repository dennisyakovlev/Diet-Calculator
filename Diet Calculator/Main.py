import CONSTANTS as CONST
from File_Manager import File as FileType
from Nutrition_Fact import Nutrition_Fact as NutritionType
from Food import Food as FoodType
import sys

class Main:

    def __init__(self):
        
       self.commands = ["EXIT", "NUTRITION", "FOOD"]
       self.dict = {self.commands[0]: self.__EXIT, self.commands[1]: self.__NUTRITION, self.commands[2]: self.__FOOD}

       self.nuritionFile = FileType(CONST.NUTRITION_FILE_NAME, NutritionType)
       self.foodFile = FileType(CONST.FOOD_FILE_NAME, FoodType)

       while True:

           self.__print_commands()

           #get function call
           inp = input()

           print()

           if inp not in self.dict:
               print("Enter valid command")
           else:
               #run function call
               self.dict[inp]()

           print()

    def __print_commands(self):
        
        print("Commands:\n" + 
              "Add a food: " + self.commands[2] + "\n" +
              "Add a nutritional information: " + self.commands[1] + "\n" + 
              "Exit the program: " + self.commands[0])

    def __EXIT(self):

        sys.exit()

    def __FOOD(self):

        self.__options("food", [self.__GET_FOOD, self.__DELETE_FOOD, self.__ADD_FOOD])
    def __GET_FOOD(self, name):
        print("mhm")
        if not self.foodFile.elem_exists(name):
            print("Food with this name does not exist")
        else:
            food = self.foodFile.get_elem(name)
            info = food.get_values()

            self.__print_nutrition(name, info)
    def __DELETE_FOOD(self, name):

        if not self.foodFile.elem_exists(name):
            print("Food with this name does not exist")
        else:
            food = self.foodFile.remove_elem(name)
    def __ADD_FOOD(self, name):

        if self.nuritionFile.elem_exists(name):
            print("Food with this name already exists")
        else:
            nutritionName = input("Name of nutrition fact that makes up food: ")

            self.foodFile.add_elem(FoodType(name, nutritionName))

    def __NUTRITION(self):
                
        self.__options("nutrition fact", [self.__DELETE_NUTRITION, self.__ADD_NUTRITION, self.__GET_NUTRITION])   
    def __GET_NUTRITION(self, name):

        if not self.nuritionFile.elem_exists(name):
            print("Nurition fact with this name does not exist")
        else:
            fact = self.nuritionFile.get_elem(name)

            self.__print_nutrition(name, fact)
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

    #toPrint - what should be printed 
    #functions - list of functions to be called with input as item name
    def __options(self, toPrint, functions):

        inp = input("Remove " + toPrint + ": REMOVE\n" +
                    "Add  " + toPrint + ": ADD\n" +
                    "Get " + toPrint + ": GET\n")

        print()

        name = input("Enter " + toPrint + " name: ")

        if inp == "REMOVE":
            functions[0](name)
        elif inp == "ADD":
            functions[1](name)
        elif inp == "GET":
            functions[2](name)

    #name - name to be printed
    #fact - nutrition fact to be printed
    def __print_nutrition(self, name, fact):

        print("Name:", name)
        print("Calories:", fact.get_calories())
        print("Fat:", fact.get_fat())
        print("     Saturated Fat:", fact.get_saturdated())
        print("     Trans Fat:", fact.get_trans())
        print("Cholesterol:", fact.get_chol())
        print("Sodium:", fact.get_sodium())
        print("Carbohydrates:", fact.get_carbs())
        print("     Fiber", fact.get_fiber())
        print("     Sugar", fact.get_sugar())
        print("Protien", fact.get_protien())

