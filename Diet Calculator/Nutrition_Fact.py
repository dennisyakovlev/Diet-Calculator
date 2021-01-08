import Element_Base as E_Base

class Nutrition_Fact(E_Base.Element_Base):

    #name - name of nutrition fact
    #values - length of 8 numbers for the nutritional info
    #total fat and total carbohydrates are not entered SHOULD BE CHANGED to accept total fat and carbs

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

    def get_calories(self):

        return self.values[0]

    def get_saturdated(self):

        return self.values[1]

    def get_trans(self):

        return self.values[2]

    def get_fiber(self):

        return self.values[3]
    
    def get_sugar(self):

        return self.values[4]
    
    def get_protien(self):

        return self.values[5]
    
    def get_chol(self):

        return self.values[6]

    def get_sodium(self):

        return self.values[7]

    def get_fat(self):

        return self.get_trans() + self.get_saturdated()

    def get_carbs(self):

        return self.get_fiber() + self.get_sugar()
