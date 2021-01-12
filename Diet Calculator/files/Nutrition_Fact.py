import Element_Base as E_Base

class Nutrition_Fact(E_Base.Element_Base):

    #name - name of nutrition fact
    #values - length of 10 numbers for the nutritional info

    #checks if the nutrition fact has valid values
    #returns true if all values are valid
    def is_valid(self):

        for item in self.values:
            if not item.replace('.', "", 1).isnumeric():
                return False
        return True

    #adds two nutrition facts
    #returns list of values containing 8 info facts
    def __add__(self, other):

        toRet = []
        for i in range(0, len(self.values)):
            toRet.append(self.values[i] + other.values[i])
        return toRet

    #n1 - n2
    #subtracts n2 FROM n1
    #returns list of values containing 8 info facts
    #return [] if one of values is negative
    def __sub__(self, other):

        toRet = []
        for i in range(0, len(self.values)):
            val = self.values[i] - other.values[i]
            if val < 0:
                return []
            toRet.append(val)
        return toRet

    #nurition_Fact * number
    #multiplies all the 8 values by number
    #return list of values containing 8 info facts
    def __mul__(self, number):

        values = [int(float(item) * float(number)) for item in self.values]

        return values
