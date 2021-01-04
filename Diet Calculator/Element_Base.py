NOT_ALLOWED = ["_", "_names", ".txt"]

#base class for an element that wants to work with File class
class Element_Base:
    
    def __init__(self, name, values):

        for item in NOT_ALLOWED:
            if item in name:
                print(name, "contains illegal character", item)

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

