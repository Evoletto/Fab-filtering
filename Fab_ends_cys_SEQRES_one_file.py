import re
import os, shutil
import os.path


directory_path = "/Users/Alina/Dropbox/Comp/NR_LH_Combined_Kabat/"
file = "1A3R_1.pdb"

my_file = open(directory_path + file)
# read the content
file_contents = my_file.readlines()

light_chain = ""
heavy_chain = ""

for line in file_contents:
	if line.startswith("REMARK 950 CHAIN L    L"):
		striped = line.strip()
		light_chain = striped[len(striped) - 1]
	
	if line.startswith("REMARK 950 CHAIN H    H"):
		striped = line.strip()
		heavy_chain = striped[len(striped) - 1]
		
	if line.strip().endswith("CYS"):
		print ("LC ends on " + line.strip()[-3:])

print(file.rsplit('.', 1)[0], light_chain, heavy_chain)	



# this code works