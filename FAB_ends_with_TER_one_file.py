import re
import os, shutil
import os.path


directory_path = "/Users/Alina/Dropbox/Comp/NR_LH_Combined_Kabat/"
file = "4DGV_1.pdb"
# all_files = sorted(os.listdir(directory_path))

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
		
	if line.strip().endswith("L 107"):
		print ("LC ends on " + line.strip()[17:21])
		
	if line.strip().endswith("L 108"):
		print ("LC ends on " + line.strip()[17:21])
		
	if line.strip().endswith("L 109"):
		print ("LC ends on " + line.strip()[17:21])
		
	if line.strip().endswith("L 110"):
		print ("LC ends on " + line.strip()[17:21])
		
		
print(file.rsplit('.', 1)[0], light_chain, heavy_chain)	



# this code works

