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
       self.commands = ["DAY", "DISH", "FOOD", "EXIT"]
       self.dict = {self.commands[0]: self.__DAY, \
                    self.commands[1]: self.__DISH, \
                    self.commands[2]: self.__FOOD, \
                    self.commands[3]: self.__EXIT}
       #set commands

       #set printing params
       self.commandValues = ["Access day commands: ", \
                             "Access dish commands", \
                             "Access food commands: ", \
                             "Exit the program: "]
       self.commandSpaces = self.__get_spaces(self.commandValues)

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
       #set printing params

       #create printing list
       temp = []
       #replace first item with later with command
       self.printItems = []
       for i in range(0, len(self.commands)):
           self.printItems.append(self.commandValues[i] + self.commandSpaces[i] + self.commands[i])
           temp.append(self.commandValues[i] + self.commandSpaces[i])
       
       spacing = self._get_longest_val(temp)
       self.command = "\n" + (" " * spacing) + "COMMANDS\n"
       #create printing list

       #create files
       self.nuritionFile = FileType(CONST.NUTRITION_FILE_NAME, NutritionType)
       self.foodFile = FileType(CONST.FOOD_FILE_NAME, FoodType)
       self.dishesFile = FileType(CONST.DISH_FILE_NAME, DishType)
       self.daysFile = FileType(CONST.DAY_FILE_NAME, DayType)
       #create files

       #first print
       print("Instructions:")
       
       print()

       print("All commands are in capital letters. They are case sensitive.\n" + \
             "Commands to access an item are under \"COMMANDS\"\n" + \
             "Entering a command brings up that items actions\n" + \
             "which are ADD, GET, and REMOVE.\n" + \
             "Some items have special actions, they will explititly state this.")
       
       print()

       print("ALL is a special word that can be used with the GET and REMOVE actions.\n" + \
             "With get it print the names of all of the type of item.\n" + \
             "With remove it removes all of the type of item.")
       
       print()

       print("The following are the items.")
       print("Nutrition Fact:\n")
       print("     - This is the first information to be entered\n" + \
             "     - Enter information per 100g")
       print("Food:\n")
       print("     - Uses a nutritional information to hold its value")
       print("Dish:\n")
       print("     - Consists of any number of foods of any weight")
       print("Day:\n")
       print("     - Consists of any number of dishes")

       print()
       print("-" * 20 + "SCROLL TO TOP FOR COMPLETE INSTRUCTIONS" + "-" * 20)
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
               comm = ""
               for item in self.commands[:-1]:
                   comm = comm + item + " or "
               comm = comm + self.commands[-1]
               print("Enter valid command of: " + comm)
           else:
               #run function call
               self.dict[inp]()

           print()

    def __print_commands(self):

        maxLen = 0
        for item in self.printItems:
            maxLen = max(maxLen, len(item))
        
        print("-" * maxLen)

        #print(self.command)
        print(self.command)
        for item in self.printItems:
            print(item)

    def __EXIT(self):

        sys.exit()

    def __DAY(self):
        
        self.__options("day", [self.__DELETE_DAY, self.__ADD_DAY, self.__GET_DAY, self.__CHANGE_DAY])
    def __GET_DAY(self, name):

        if name == "ALL":
            self.__print_all(self.daysFile)
        else:
            if not self.daysFile.elem_exists(name):
                self.__print_name_error("Day with this name does not exist")
            else:
               
                inp = input("\nGet nutritional information total(T) or for each dish(E): ")

                if inp == "T":
                    day = self.daysFile.get_elem(name)

                    nutritionalInfo = day.get_nutritional_info()
                    self.__print_nutrition(name, nutritionalInfo, "Nutritional information for the day ")
                elif inp ==  "E":
                    dishes = self.daysFile.get_elem(name).get_values()

                    #list of list of values
                    #[[calories, ..., protien], [calories, ..., protien], ...]
                    nutritionalInfos = []
                    for dish in dishes:
                        nutritionalInfos.append(self.dishesFile.get_elem(dish).get_nutritional_info())
                    
                    # {       element        }                                     
                    #[[calories, ..., protien], [calories, ..., protien], ...]
                    printValuesTemp = []
                    #for each nutrition fact
                    for fact in nutritionalInfos:
                        toPrint = self.__get_print_nutrition_info(fact)
                        longest = self.__get_longest(toPrint)
                        lengthLongest = len(toPrint[longest]) + 1

                        for i in range(len(toPrint)):
                            toPrint[i] = toPrint[i] + ((lengthLongest - len(toPrint[i])) * " ") + "| "

                        printValuesTemp.append(toPrint)

                    #[calories from all dishes, ..., protien from all dishes]
                    printValues = ["" for item in range(len(printValuesTemp[0]))]
                    #index from calories ... protien
                    for i in range(len(printValuesTemp[0])):
                        #index each element in printValuesTemp
                        for j in range(len(printValuesTemp)):
                            #if it is the first nutrition fact to be printed, add a | on the left
                            if j == 0:
                                printValues[i] = "| " + printValues[i] + printValuesTemp[j][i]
                            else:
                                printValues[i] = printValues[i] + printValuesTemp[j][i]

                    #print result
                    print("\n" + ("-" * (len(printValues[0]) - 1)))
                    for line in printValues:
                        print(line[:-1])
                    print("-" * (len(printValues[0]) - 1))

                else:
                    self.__print_name_error("Input should be \"T\" or \"E\"")
    def __DELETE_DAY(self, name):

        if name == "ALL":
            self.__remove_all(self.daysFile)
        else:
            if not self.daysFile.elem_exists(name):
                self.__print_name_error("Day with this name does not exist")
            else:
                self.daysFile.remove_elem(name)
    def __ADD_DAY(self, name):

        if self.daysFile.elem_exists(name):
            self.__print_name_error("Day with this name already exists")
        else:
            print("\nEnter dishes which make up day")
            print()
            
            values = []
            dishName = " "
            hadError = False
            while True:

                dishName = input("Name of dish (hit enter to exit): ")

                if dishName == "":
                    break

                if not self.dishesFile.elem_exists(dishName):
                    hadError = True
                    self.__print_name_error("\nDish with this name does not exist." + \
                                            "\nMust create this dish using DISH command." + \
                                            "\nPress enter to exit this command.\n")
                else:
                    values.append(dishName)
            
            if not hadError:
                self.daysFile.add_elem(DayType(name, values))
    def __CHANGE_DAY(self, name):
        pass

    def __DISH(self):

        self.__options("dish", [self.__DELETE_DISH, self.__ADD_DISH, self.__GET_DISH, self.__CHANGE_DISH])
    def __GET_DISH(self, name):

        if name == "ALL":
            self.__print_all(self.dishesFile)
        else:
            if not self.dishesFile.elem_exists(name):
                self.__print_name_error("Dish with this name does not exist")
            else:
                dish = self.dishesFile.get_elem(name)

                nutritionalInfo = dish.get_nutritional_info()
                self.__print_nutrition(name, nutritionalInfo, "Nutritional information for one ")      
    def __DELETE_DISH(self, name):

        if name == "ALL":
            self.__remove_all(self.dishesFile)
        else:
            if not self.dishesFile.elem_exists(name):
                self.__print_name_error("Dish with this name does not exist")
            else:
                self.dishesFile.remove_elem(name)
    def __ADD_DISH(self, name):
                
        if self.dishesFile.elem_exists(name):
            self.__print_name_error("Dish with this name already exists")
        else:
            
            print("\nEnter food name(s) and weight(s).")
            print()

            values = []
            foodName = " "
            hadError = False
            #get values to create dish
            while True:

                foodName = input("Name of food (hit enter to exit): ")

                if foodName == "":
                    break

                if not self.foodFile.elem_exists(foodName):
                    hadError = True
                    self.__print_name_error("\nFood with this name does not exist." + \
                                            "\nMust create this dish using FOOD command." + \
                                            "\nPress enter to exit this command.\n")
                else:
                    foodWeight = input("Weight of food to be added to dish: ")

                    values.append(foodName)
                    values.append(foodWeight)

            if not hadError:
                self.dishesFile.add_elem(DishType(name, values))     
    def __CHANGE_DISH(self, name) :
        
        if not self.dishesFile.elem_exists(name):
            self.__print_name_error("Dish with this name does not exist")
        else:
            dish = self.dishesFile.get_elem(name)

            values = dish.get_values()

            foods = []
            weights = []
            for i in range(0, len(values), 2):
                foods.append(values[i])
                weights.append(values[i + 1])

            longest = self._get_longest_val(foods)

            print("\nFoods that make up dish \"" + name + "\":\n")
            for i in range(len(foods)):
                print( "Food: " + ((longest - len(foods[i])) * " ") + foods[i] + " | Weight: " + str(weights[i]) + " g" )

            print()
            print("To remove food: enter R, then food name (R name)\n" + \
                  "To add food: enter A, then food name, then weight (A name number)\n" + \
                  "To change weight of food already in dish: enter C, then food name, then weight (C name number)")
            while True:
                inp = input("Enter: ")
                food, comm = inp.split(" ")
                if comm == "ADD":
                    pass
                if comm != "ADD" and comm != "REMOVE":
                    print("Enter valid command of ADD or REMOVE")
                    break
                if not self.foodFile.elem_exists(food):
                    self.__print_name_error("Food with this name does not exist")
                    break





    def __FOOD(self):

        self.__options("food", [self.__DELETE_FOOD, self.__ADD_FOOD, self.__GET_FOOD, self.__CHANGE_FOOD])
    def __GET_FOOD(self, name):

        if name == "ALL":
            self.__print_all(self.foodFile)
        else:
            if not self.foodFile.elem_exists(name):
                self.__print_name_error("Food with this name does not exist")
            else:
                food = self.foodFile.get_elem(name)
                nutritionalInfo = food.get_nutritional_info()

                self.__print_nutrition(name, nutritionalInfo)
    def __DELETE_FOOD(self, name):

        if name == "ALL":
            self.__remove_all(self.foodFile)
        else:
            if not self.foodFile.elem_exists(name):
                self.__print_name_error("Food with this name does not exist")
            else:
                self.foodFile.remove_elem(name)
    def __ADD_FOOD(self, name):

        if self.foodFile.elem_exists(name):
            self.__print_name_error("Food with this name already exists")
        else:
            self.__ADD_NUTRITION(name)

            food = FoodType(name, [name, 100])
            self.foodFile.add_elem(food)
    def __CHANGE_FOOD(self, name):
        
        pass


    def __NUTRITION(self):
                
        self.__options("nutrition fact", [self.__DELETE_NUTRITION, self.__ADD_NUTRITION, self.__GET_NUTRITION])   
    def __GET_NUTRITION(self, name):
        
        if name == "ALL":
            self.__print_all(self.nuritionFile)
        else:
            if not self.nuritionFile.elem_exists(name):
                self.__print_name_error("Nurition fact with this name does not exist")
            else:
                fact = self.nuritionFile.get_elem(name)

                self.__print_nutrition(name, fact.get_values())
    def __DELETE_NUTRITION(self, name):
        
        if name == "ALL":
            self.__remove_all(self.nuritionFile)
        else:
            if not self.nuritionFile.elem_exists(name):
                self.__print_name_error("Nurition fact with this name does not exist")
            else:
                self.nuritionFile.remove_elem(name)
    def __ADD_NUTRITION(self, name):

        if self.nuritionFile.elem_exists(name):
            self.__print_name_error("Nurition fact with this name already exists")
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
         
    #print when a name error occurs 
    def __print_name_error(self, toPrint):

        print("\n***" + toPrint + "***\n")

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

        print("Remove " + toPrint + ": REMOVE\n" + \
              "Add  " + toPrint + ": ADD\n" + \
              "Get " + toPrint + ": GET\n" + \
              "Change " + toPrint + ": CHANGE\n")

        inp = input("Enter action: ")

        if inp != "REMOVE" and inp != "ADD" and inp != "GET" and inp != "CHANGE":
            print("\nEnter valid action of: REMOVE or ADD or GET or CHANGE")
        else:
            print()

            name = input("Enter " + toPrint + " name: ")

            if inp == "REMOVE":
                functions[0](name)
            elif inp == "ADD":
                functions[1](name)
            elif inp == "GET":
                functions[2](name)
            elif inp == "CHANGE":
                functions[3](name)

    #name - name to be printed
    #fact - list of values from nutrition fact to be printed
    def __print_nutrition(self, name, values, text = "Nutritional information per 100g for "):

        print()

        longestLine = text + "\"" + name + "\":"

        print("-" * len(longestLine))
        
        print(longestLine + "\n")
        
        printValues = self.__get_print_nutrition_info(values)

        print(printValues[0])
        print(printValues[1])
        print(printValues[2])
        print(printValues[3])
        print(printValues[4])
        print(printValues[5])
        print(printValues[6])
        print(printValues[7])
        print(printValues[8])
        print(printValues[9])

        print("-" * len(longestLine))

    #returns list of values where each line is the output for a nutrition fact
    #list of length 10
    def __get_print_nutrition_info(self, values):

        toRet = [self.nutritionItems[0] + self.nutritionSpaces[0] + " " + str(values[0]) + " cal",
                 self.nutritionItems[1] + self.nutritionSpaces[1] + " " + str(values[1]) + " g",
                 self.nutritionItems[2] + self.nutritionSpaces[2] + " " + str(values[2]) + " g", 
                 self.nutritionItems[3] + self.nutritionSpaces[3] + " " + str(values[3]) + " g",
                 self.nutritionItems[4] + self.nutritionSpaces[4] + " " + str(values[4]) + " mg",
                 self.nutritionItems[5] + self.nutritionSpaces[5] + " " + str(values[5]) + " mg",
                 self.nutritionItems[6] + self.nutritionSpaces[6] + " " + str(values[6]) + " g",
                 self.nutritionItems[7] + self.nutritionSpaces[7] + " " + str(values[7]) + " g",
                 self.nutritionItems[8] + self.nutritionSpaces[8] + " " + str(values[8]) + " g",
                 self.nutritionItems[9] + self.nutritionSpaces[9] + " " + str(values[9]) + " g"]
    
        return toRet

    #returns indicie of longest element in list
    def __get_longest(self, values):

        longest = 0
        for i in range(len(values)):
            longest = i if len(values[i]) > len(values[longest]) else longest
        return longest

    #return size of longest element in list
    def _get_longest_val(self, values):

        longest = 0
        for item in values:
            longest = len(item) if len(item) > longest else longest
        return longest