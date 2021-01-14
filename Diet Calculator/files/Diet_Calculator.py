from Main import Main as MainType
import os

if not os.access(os.getcwd() + "\store", os.F_OK):
        os.mkdir(os.getcwd() + "\store")

os.chdir(os.getcwd() + "\store")

#run program
m = MainType()