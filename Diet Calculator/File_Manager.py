import os
from Element_Base import Element_Base as Base

#NAME of element should NOT be able to have _

class File:

    nameExtension = "_names"
    fileExtension = ".txt"

    #name is file name
    #elementType is in Base family of classes
    def __init__(self, name, elementType):
        
        self._type = elementType
        self.fileName = name + self.fileExtension
        self.namesFileName = name + self.nameExtension + self.fileExtension

        if not os.path.isfile(self.fileName):
            file = open(self.fileName, "w+")
            file.close()
        
        if not os.path.isfile(self.namesFileName):
            fileNames = open(self.namesFileName, "w+")
            fileNames.close()

    #add an element of the given type to teh file
    def add_elem(self, element):

        #cast to a base element
        baseElement = self.cast_to_base(element)

        #write to names file
        namesFile = open(self.namesFileName, "r+")
        if not self.check_name(baseElement.get_name(), namesFile):
            print(baseElement.get_name(), "name is taken")
            exit()

        while namesFile.readline():
            pass

        namesFile.write(str(baseElement.get_name()) + "\n")
        namesFile.close()
        #write to names file

        #write to values file
        valuesFile = open(self.fileName, "r+")
        while valuesFile.readline():
            pass
        
        valuesFile.write(str(baseElement.get_name()) + self.nameExtension + "\n")
        for item in baseElement.get_values():
            valuesFile.write(str(item) + "\n")

        valuesFile.close()
        #write to values file

    #get element as the set type using the given name
    def get_elem(self, name):

        #check to see if there exists an element with the specified name
        namesFile = open(self.namesFileName, "r")
        if self.check_name(name, namesFile):
            print(name, "not found")
            exit()
        namesFile.close()

        #open the values file
        file = open(self.fileName, "r")

        #look for the specified name
        #stop at the line where the specified name is found
        line = file.readline()
        while line != "":
            if self.nameExtension in line:
                if line.strip().split("_")[0] == name:
                    break
            line = file.readline()

        #go to the line after the name
        line = file.readline()

        #read the element information
        info = []
        while self.nameExtension not in line:
            info.append(line.strip())
            line = file.readline()

        return self._type(name, info)

    #file is opened for reading
    #checks if name is already exists, return True if not taken
    def check_name(self, name, file):
        
        lines = file.readlines()
        for line in lines:
            if line.strip() == name:
                return False
        return True
            
    def cast_to_base(self, elem):

        return Base(elem.get_name(), elem.get_values())

