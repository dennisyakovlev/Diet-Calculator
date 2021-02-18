import os
import warnings

#methods return true on success and false on fail
class File:

    nameExtension = "_names"
    temporaryExtension = "_temp"
    fileExtension = ".txt"
    infoFolder = "store"

    #name is file name
    #elementType is in Base family of classes
    def __init__(self, name, elementType):

        #the type of the element to be added
        self._type = elementType
        #the name of the file containing the information of the elements
        self.fileName = name + self.fileExtension
        #the name of the file containing the names of the elements
        self.namesFileName = name + self.nameExtension + self.fileExtension
        #the name of the temporary file
        self.tempFileName = name + self.temporaryExtension + self.fileExtension

        if not self.fileName in os.listdir():
            file = open(self.fileName, "w+")
            file.close()
        
        if not self.namesFileName in os.listdir():
            fileNames = open(self.namesFileName, "w+")
            fileNames.close()

    #get all the names of the elements in the file
    def get_all(self):
        
        toReturn = []
        namesFile = open(self.namesFileName)
        line = namesFile.readline()
        while line != "":
            toReturn.append(line.strip())
            line = namesFile.readline()
        return toReturn

    #to check if a name exists
    #return true if the name already exists
    def elem_exists(self, name):
        
        file = open(self.namesFileName)
        return not self.__check_name(name, file)        

    #add an element of the given type to teh file
    def add_elem(self, element):

        #write to names file
        namesFile = open(self.namesFileName, "r+")
        if not self.__check_name(element.get_name(), namesFile):
            return False

        while namesFile.readline():
            pass

        namesFile.write(str(element.get_name()) + "\n")
        namesFile.close()
        #write to names file

        #write to values file
        valuesFile = open(self.fileName, "r+")
        while valuesFile.readline():
            pass
        
        valuesFile.write(str(element.get_name()) + self.nameExtension + "\n")
        for item in element.get_values():
            valuesFile.write(str(item) + "\n")

        valuesFile.close()
        #write to values file
    
        return True

    #get element as the set type using the given name
    def get_elem(self, name):

        #check to see if there exists an element with the specified name
        namesFile = open(self.namesFileName, "r")
        if self.__check_name(name, namesFile):
            raise Exception(f'GET_ELEM - cannot get element of name: {name}')
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
        while (self.nameExtension not in line) and (line != ""):
            info.append(line.strip())
            line = file.readline()

        return self._type(name, info)

    #need to remove name from names file aswell
    #remove element from file as the set type using the given name
    def remove_elem(self, name):
        
        namesFile = open(self.namesFileName, "r")
        if self.__check_name(name, namesFile):
            raise Exception(f'REMOVE_ELEM - cannot get element of name: {name}')
        namesFile.close()

        self.__remoe_elem_name(name)
        self.__remove_elem_values(name)       

    #delete name from names file
    def __remoe_elem_name(self, name):
        
        newFile = []
        file = open(self.namesFileName, "r")
        #read all line except the element
        line = file.readline()
        while line != "":
            if name == line.strip():
                line = file.readline()
            newFile.append(line)
            line = file.readline()
        #when last element in file is requested there is blank item in list
        file.close()

        #write to temporary file
        tempFile = open(self.tempFileName, "w")
        for item in newFile:
            tempFile.write(item)
        tempFile.close()

        #swap temporary and new file
        os.remove(self.namesFileName)
        os.rename(self.tempFileName, self.namesFileName)

    #delete element from file containing values 
    def __remove_elem_values(self, name):
        
        newFile = []
        file = open(self.fileName, "r")
        #read all line except the element
        line = file.readline()
        while line != "":
            if self.nameExtension in line:
                if line.strip() == (name + self.nameExtension):
                    line = file.readline()
                    while (self.nameExtension not in line) and (line != ""):
                        line = file.readline()
            newFile.append(line)
            line = file.readline()
        #when last element in file is requested there is blank item in list
        if newFile[-1] == "":
            newFile.pop()
        file.close()

        #write to temporary file
        tempFile = open(self.tempFileName, "w")
        for item in newFile:
            tempFile.write(item)
        tempFile.close()

        #swap temporary and new file
        os.remove(self.fileName)
        os.rename(self.tempFileName, self.fileName)

    #file is opened for reading
    #checks if name is already exists, return True if name doesnt exist
    def __check_name(self, name, file):
        
        lines = file.readlines()
        for line in lines:
            if line.strip() == name:
                return False
        return True

