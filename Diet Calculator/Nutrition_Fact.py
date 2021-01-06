import Element_Base as E_Base

class Nutrition_Fact(E_Base.Element_Base):

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
