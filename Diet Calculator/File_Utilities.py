import pytesseract as tess
import File_Utilities as f
import os
from PIL import Image

tess.pytesseract.tesseract_cmd = r"C:\Users\jboob\AppData\Local\Programs\Tesseract-OCR\tesseract.exe"

class Write:

	def imgNutritionFact(self, name, fileName):
		img = Image.open(fileName)
		text = tess.image_to_string(img)

	#write a N_Fact into the nutrition facts file
	def nmbrNutritionFact(self, name, cal, sat, trans, fiber, sugar, protien, chol, sod):
		
		if not os.path.isfile("ntr.txt"):
			file = open("ntr.txt", "w+")
			file.write("END")
			file.close()
			
		file = open("ntr.txt", "a")
		file.write("mhm\n")
		file.write("mhm2")
		
		file.close()


