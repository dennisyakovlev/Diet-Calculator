import CONSTANTS as CONST
from File_Manager import File as FileType
from Nutrition_Fact import Nutrition_Fact as NutritionType
from Food import Food as FoodType
import sys

class Main:

    def __init__(self):
        
       #set commands
       self.commands = ["EXIT", "NUTRITION", "FOOD"]
       self.dict = {self.commands[0]: self.__EXIT, self.commands[1]: self.__NUTRITION, self.commands[2]: self.__FOOD}
       #set commands

       #set printing params
       self.nutritionItems = ["Calories:", "Fat:", "     Saturated Fat:", "     Trans Fat:", "Cholesterol:", "Sodium:", \
           "Carbohydrates:", "     Fiber", "     Sugar", "Protien"]
       self.nutritionSpaces = self.__get_spaces(self.nutritionItems)


       self.commandValues = ["Access food commands: ", "Access nutritional information commands: ", "Exit the program: "]
       self.commandSpaces = self.__get_spaces(self.commandValues)
       #set printing params

       #create files
       self.nuritionFile = FileType(CONST.NUTRITION_FILE_NAME, NutritionType)
       self.foodFile = FileType(CONST.FOOD_FILE_NAME, FoodType)
       #create files

       #consle loop
       while True:

           self.__print_commands()

           print()

           #get function call
           inp = input("Enter Command: ")

           print()

           if inp not in self.dict:
               print("Enter valid command")
           else:
               #run function call
               self.dict[inp]()

           print()

    def __print_commands(self):
        
        printItems = [self.commandValues[0] + self.commandSpaces[0] + self.commands[2], \
                      self.commandValues[1] + self.commandSpaces[1] + self.commands[1], \
                      self.commandValues[2] + self.commandSpaces[2] + self.commands[0]]

        maxLen = 0
        for item in printItems:
            maxLen = max(maxLen, len(item))
        
        print("-" * maxLen)

        print("Commands:\n" + 
              printItems[0] + "\n" +
              printItems[1] + "\n" + 
              printItems[2])

    def __EXIT(self):

        sys.exit()

    def __FOOD(self):

        self.__options("food", [self.__DELETE_FOOD, self.__ADD_FOOD, self.__GET_FOOD])
    def __GET_FOOD(self, name):

        if name == "ALL":
            allNames = self.foodFile.get_all()
            print()
            for item in allNames:
                print(item)
        else:
            if not self.foodFile.elem_exists(name):
                print("Food with this name does not exist")
            else:
                food = self.foodFile.get_elem(name)
                info = food.get_nutritional_info()

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

            #check that the nutrition fact actually exists
            if not self.nuritionFile.elem_exists(nutritionName):
                print("Nurition fact with this name does not exist")
            else:
                food = FoodType(name, [nutritionName, 100])
                self.foodFile.add_elem(food)

    def __NUTRITION(self):
                
        self.__options("nutrition fact", [self.__DELETE_NUTRITION, self.__ADD_NUTRITION, self.__GET_NUTRITION])   
    def __GET_NUTRITION(self, name):
        
        if name == "ALL":
            allNames = self.nuritionFile.get_all()
            print()
            for item in allNames:
                print(item)
        else:
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
            print("\nEnter per 100g")
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
         
    #get list of string of spaces compareed to the
    #max length of a string in values
    def __get_spaces(self, values):
        
       toRet = []
       maxLen = 0
       for item in values:
           maxLen = max(maxLen, len(item))
       for item in values:
           toRet.append(" " * (maxLen - len(item)))

       return toRet

    #toPrint - what should be printed 
    #functions - list of functions to be called with input as item name
    def __options(self, toPrint, functions):

        print("Remove " + toPrint + ": REMOVE\n" +
                    "Add  " + toPrint + ": ADD\n" +
                    "Get " + toPrint + ": GET\n")

        inp = input("Enter action: ")

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

        print()

        longestLine = "Nutritional information per 100g for \"" + name + "\":"

        print("-" * len(longestLine))
        
        print(longestLine + "\n")
        
        print(self.nutritionItems[0] + self.nutritionSpaces[0], values[0], "cal")
        print(self.nutritionItems[1] + self.nutritionSpaces[1], str(values[1] + values[2]), "g")
        print(self.nutritionItems[2] + self.nutritionSpaces[2], str(values[1]), "g")
        print(self.nutritionItems[3] + self.nutritionSpaces[3], str(values[2]), "g")
        print(self.nutritionItems[4] + self.nutritionSpaces[4], str(values[3]), "mg")
        print(self.nutritionItems[5] + self.nutritionSpaces[5], str(values[4]), "mg")
        print(self.nutritionItems[6] + self.nutritionSpaces[6], str(values[5] + values[6]), "g")
        print(self.nutritionItems[7] + self.nutritionSpaces[7], str(values[5]), "g")
        print(self.nutritionItems[8] + self.nutritionSpaces[8], str(values[6]), "g")
        print(self.nutritionItems[9] + self.nutritionSpaces[9], str(values[7]), "g")
        
        print("-" * len(longestLine))