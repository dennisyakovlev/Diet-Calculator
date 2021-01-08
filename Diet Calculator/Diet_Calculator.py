from Main import Main as MainType
from Nutrition_Fact import Nutrition_Fact as N

#m = MainType()

arr = [1,2,3,4,5,6,7,8]

a = N("a", arr)
b = N("b", [item * 3 for item in arr])

c = b - a

for item in c:
    print(item)