import CONSTANTS as CONST
from File_Manager import File as FileType
from Nutrition_Fact import Nutrition_Fact as NutritionType
from Food import Food as FoodType
from Food import get_food_info as get_food
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

        self.__options("food", [self.__DELETE_FOOD, self.__ADD_FOOD, self.__GET_FOOD])
    def __GET_FOOD(self, name):
        print("mhm")
        if not self.foodFile.elem_exists(name):
            print("Food with this name does not exist")
        else:
            food = self.foodFile.get_elem(name)
            info = get_food(food)

            self.__print_nutrition(name, info)
    def __DELETE_FOOD(self, name):
        print("fuck")
        if not self.foodFile.elem_exists(name):
            print("Food with this name does not exist")
        else:
            food = self.foodFile.remove_elem(name)
    def __ADD_FOOD(self, name):

        if self.nuritionFile.elem_exists(name):
            print("Food with this name already exists")
        else:
            nutritionName = input("Name of nutrition fact that makes up food: ")

            #check that the nutrition fact actually exists
            if not self.nuritionFile.elem_exists(name):
                print("Nurition fact with this name does not exist")
            else:
                food = FoodType(name, [nutritionName, 100])

                self.foodFile.add_elem(food)

    def __NUTRITION(self):
                
        self.__options("nutrition fact", [self.__DELETE_NUTRITION, self.__ADD_NUTRITION, self.__GET_NUTRITION])   
    def __GET_NUTRITION(self, name):

        if not self.nuritionFile.elem_exists(name):
            print("Nurition fact with this name does not exist")
        else:
            fact = self.nuritionFile.get_elem(name)

            self.__print_nutrition(name, fact.get_values())
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
    def __print_nutrition(self, name, values):

        #change to values and indicies
        print("Name:", name)
        print("Calories:", values[0])
        print("Fat:", values[1])
        print("     Saturated Fat:", values[1])
        print("     Trans Fat:", values[2])
        print("Cholesterol:", values[3])
        print("Sodium:", values[4])
        print("Carbohydrates:", values[6])
        print("     Fiber", values[5])
        print("     Sugar", values[6])
        print("Protien", values[7])

