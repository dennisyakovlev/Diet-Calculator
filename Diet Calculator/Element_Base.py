#base class for an element that wants to work with File class
class Element_Base:
    
    #types = [type, ...]
    #the types of the 
    def __init__(self, name, types):

        self.types = types
        self.values = []

    def to_elem(self, attributes):  

        if not len(self.types) == len(attributes):
            print("length of attributes does not equal length of types")
            exit()

        for i in range(0, len(self.types)):
            self.values.append(self.types[i](attributes[i]))

    def get_types(self):
        return self.types

    def get_values(self):
        return self.values

