import sys
NOT_ALLOWED = ["_", "_names", ".txt"]

#base class for an element that wants to work with File class
class Element_Base:
    
    #SHOULD NOT BE OVERWRITTEN

    #name - name of element to be added to file
    #values - list of values to be added to element file
    def __init__(self, name, values):

        can_create = True
        for item in NOT_ALLOWED:
            if item in name:
                can_create = False
                break

        if can_create:
            self.name = name

            self.values = []
            for item in values:
                self.values.append(item)
        else:
            self.name = ''
            self.values = []

    #return whether element was successfully created
    def is_created(self):

        return (self.name != '') and (self.values != [])

    def get_values(self):

        return self.values

    def get_name(self):

        return self.name

    def get_length(self):

        return len(self.get_values())
    
    #SHOULD NOT BE OVERWRITTEN

