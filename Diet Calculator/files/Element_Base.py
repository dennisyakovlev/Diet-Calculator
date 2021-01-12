import sys
NOT_ALLOWED = ["_", "_names", ".txt"]

#base class for an element that wants to work with File class
class Element_Base:
    
    #SHOULD NOT BE OVERWRITTEN

    #name - name of element to be added to file
    #values - list of values to be added to element file
    def __init__(self, name, values):

        for item in NOT_ALLOWED:
            if item in name:
                print(name, "contains illegal character", item)
                sys.exit()

        self.name = name

        self.values = []
        for item in values:
            self.values.append(item)

    def get_values(self):

        return self.values

    def get_name(self):

        return self.name

    def get_length(self):

        return len(self.get_values())
    s
    #SHOULD NOT BE OVERWRITTEN

