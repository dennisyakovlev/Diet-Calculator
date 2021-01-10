import CONSTANTS as CONST
from File_Manager import File as FileType
from Nutrition_Fact import Nutrition_Fact as NutritionType
from Food import Food as FoodType
from Dish import Dish as DishType
from Day import Day as DayType

import sys

class Main:

    def __init__(self):
        
       #set commands
       self.commands = ["DAY", "DISH", "FOOD", "NUTRITION", "EXIT"]
       self.dict = {self.commands[0]: self.__DAY, \
                    self.commands[1]: self.__DISH, \
                    self.commands[2]: self.__FOOD, \
                    self.commands[3]: self.__NUTRITION, \
                    self.commands[4]: self.__EXIT}
       #set commands

       #set printing params
       self.nutritionItems = ["Calories:", \
                              "Fat:", 
                              "     Saturated Fat:", \
                              "     Trans Fat:", \
                              "Cholesterol:", \
                              "Sodium:", \
                              "Carbohydrates:", \
                              "     Fiber", \
                              "     Sugar", \
                              "Protien"]
       self.nutritionSpaces = self.__get_spaces(self.nutritionItems)


       self.commandValues = ["Access day commands: ", \
                             "Access food commands: ", \
                             "Access nutritional information commands: ", \
                             "Exit the program: ", \
                             "Access dish commands"]
       self.commandSpaces = self.__get_spaces(self.commandValues)
       #set printing params

       #create printing list
       self.printItems = []
       for i in range(0, len(self.commands)):
           self.printItems.append(self.commandValues[i] + self.commandSpaces[i] + self.commands[i])
       #create printing list

       #create files
       self.nuritionFile = FileType(CONST.NUTRITION_FILE_NAME, NutritionType)
       self.foodFile = FileType(CONST.FOOD_FILE_NAME, FoodType)
       self.dishesFile = FileType(CONST.DISH_FILE_NAME, DishType)
       self.daysFile = FileType(CONST.DAY_FILE_NAME, DayType)
       #create files

       #first print
       print("Special words\n")
       print("ALL - Gets the names of all the requested items.\n" + \
             "    - Works with GET and REMOVE actions.")
       print()
       #first print

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

        maxLen = 0
        for item in self.printItems:
            maxLen = max(maxLen, len(item))
        
        print("-" * maxLen)

        print("Commands:\n")
        for item in self.printItems:
            print(item)

    def __EXIT(self):

        sys.exit()

    def __DAY(self):
        
        self.__options("day", [self.__DELETE_DAY, self.__ADD_DAY, self.__GET_DAY])
    def __GET_DAY(self, name):

        if name == "ALL":
            self.__print_all(self.daysFile)
        else:
            print("test")
    def __DELETE_DAY(self, name):

        if name == "ALL":
            self.__remove_all(self.daysFile)
        else:
            if not self.daysFile.elem_exists(name):
                print("Day with this name does not exist")
            else:
                self.daysFile.remove_elem(name)
    def __ADD_DAY(self, name):

        if self.daysFile.elem_exists(name):
            print("Day with this name already exists")
        else:
            print("\nEnter dishes which make up day")
            print()
            
            values = []
            dishName = " "
            while True:

                dishName = input("Name of dish: ")

                if dishName == "":
                    break

                if not self.dishesFile.elem_exists(dishName):
                    print("Dish with this name does not exist")
                else:
                    values.append(dishName)

            self.daysFile.add_elem(DayType(name, values))

    def __DISH(self):

        self.__options("dish", [self.__DELETE_DISH, self.__ADD_DISH, self.__GET_DISH])
    def __GET_DISH(self, name):

        if name == "ALL":
            self.__print_all(self.dishesFile)
        else:
            if not self.dishesFile.elem_exists(name):
                print("Dish with this name does not exist")
            else:
                dish = self.dishesFile.get_elem(name)

                nutritionalInfo = dish.get_nutritional_info()
                self.__print_nutrition(name, nutritionalInfo, "Nutritional information for one ")      
    def __DELETE_DISH(self, name):

        if name == "ALL":
            self.__remove_all(self.dishesFile)
        else:
            if not self.dishesFile.elem_exists(name):
                print("Dish with this name does not exist")
            else:
                self.dishesFile.remove_elem(name)
    def __ADD_DISH(self, name):
                
        if self.dishesFile.elem_exists(name):
            print("Dish with this name already exists")
        else:
            
            print("\nEnter food name(s) and weight(s).")
            print()

            values = []
            foodName = " "
            #get values to create dish
            while True:

                foodName = input("Name of food: ")

                if foodName == "":
                    break

                if not self.foodFile.elem_exists(foodName):
                    print("Food with this name does not exist")
                else:
                    foodWeight = input("Weight of food to be added to dish: ")

                    values.append(foodName)
                    values.append(foodWeight)

            self.dishesFile.add_elem(DishType(name, values))     

    def __FOOD(self):

        self.__options("food", [self.__DELETE_FOOD, self.__ADD_FOOD, self.__GET_FOOD])
    def __GET_FOOD(self, name):

        if name == "ALL":
            self.__print_all(self.foodFile)
        else:
            if not self.foodFile.elem_exists(name):
                print("Food with this name does not exist")
            else:
                food = self.foodFile.get_elem(name)
                nutritionalInfo = food.get_nutritional_info()

                self.__print_nutrition(name, nutritionalInfo)
    def __DELETE_FOOD(self, name):

        if name == "ALL":
            self.__remove_all(self.foodFile)
        else:
            if not self.foodFile.elem_exists(name):
                print("Food with this name does not exist")
            else:
                self.foodFile.remove_elem(name)
    def __ADD_FOOD(self, name):

        if self.foodFile.elem_exists(name):
            print("Food with this name already exists")
        else:
            nutritionName = input("\nName of nutrition fact that makes up food: ")

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
            self.__print_all(self.nuritionFile)
        else:
            if not self.nuritionFile.elem_exists(name):
                print("Nurition fact with this name does not exist")
            else:
                fact = self.nuritionFile.get_elem(name)

                self.__print_nutrition(name, fact.get_values())
    def __DELETE_NUTRITION(self, name):
        
        if name == "ALL":
            self.__remove_all(self.nuritionFile)
        else:
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
            values.append(input("Enter grams of total fat: "))
            values.append(input("Enter grams of saturated fat: "))
            values.append(input("Enter grams of trans fat: "))
            values.append(input("Enter milligrams of cholesterol: "))
            values.append(input("Enter milligrams of sodium: "))
            values.append(input("Enter grams of total carbs: "))
            values.append(input("Enter grams of fiber: "))
            values.append(input("Enter grams of sugar: "))
            values.append(input("Enter grams of protien: "))

            nutrition = NutritionType(name, values)

            if nutrition.is_valid():
                self.nuritionFile.add_elem(nutrition)
            else:
                print("\nEnter valid values")
         
    #print all the items from a file
    def __print_all(self, file):

        allNames = file.get_all()
        print()
        for item in allNames:
            print(item)

    #delete all the intems from a file
    def __remove_all(self, file):

        allNames = file.get_all()[::-1]
        for name in allNames:
            file.remove_elem(name)

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

        if inp != "REMOVE" and inp != "ADD" and inp != "GET":
            print("\nEnter valid action")
        else:
            print()

            name = input("Enter " + toPrint + " name: ")

            if inp == "REMOVE":
                functions[0](name)
            elif inp == "ADD":
                functions[1](name)
            elif inp == "GET":
                functions[2](name)

    #name - name to be printed
    #fact - list of values from nutrition fact to be printed
    def __print_nutrition(self, name, values, text = "Nutritional information per 100g for "):

        print()

        longestLine = text + "\"" + name + "\":"

        print("-" * len(longestLine))
        
        print(longestLine + "\n")
        
        print(self.nutritionItems[0] + self.nutritionSpaces[0], values[0], "cal")
        print(self.nutritionItems[1] + self.nutritionSpaces[1], str(values[1]), "g")
        print(self.nutritionItems[2] + self.nutritionSpaces[2], str(values[2]), "g")
        print(self.nutritionItems[3] + self.nutritionSpaces[3], str(values[3]), "g")
        print(self.nutritionItems[4] + self.nutritionSpaces[4], str(values[4]), "mg")
        print(self.nutritionItems[5] + self.nutritionSpaces[5], str(values[5]), "mg")
        print(self.nutritionItems[6] + self.nutritionSpaces[6], str(values[6]), "g")
        print(self.nutritionItems[7] + self.nutritionSpaces[7], str(values[7]), "g")
        print(self.nutritionItems[8] + self.nutritionSpaces[8], str(values[8]), "g")
        print(self.nutritionItems[9] + self.nutritionSpaces[9], str(values[9]), "g")
        
        print("-" * len(longestLine))