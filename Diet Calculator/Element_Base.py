#base class for an element that wants to work with File class
class Element_Base:
    
    def __init__(self, name, values):

        self.name = name

        self.values = []
        self.types = []
        for item in values:
            self.types.append(type(item))
            self.values.append(item)

    def get_types(self):

        return self.types

    def get_values(self):

        return self.values

    def get_name(self):

        return self.name

    def get_length(self):

        return len(self.get_values())

