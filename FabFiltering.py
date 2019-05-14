# open file
# my_file = open("1A2Y_1.pdb")
# read the content
# file_contents = my_file.read()
# print(file_contents)

import re
import os
directory_path = "/Users/Alina/Dropbox/Comp/NR_LH_Combined_Kabat/"
all_files = sorted(os.listdir(directory_path))


for file in all_files:
#tmp = "/Users/Alina/Dropbox/Comp/NR_LH_Combined_Kabat/1A3R_1.pdb"
	filename = (directory_path + file)
	lines = [line.rstrip('\n') for line in open(filename)]

	conditions = ["L    L    A", 
				  "L    L    L",
				  "H    H    B",
				  "H    H    H",
				  "L    L    C",
				  "H    H    D"]


	found = False	

	for index, line in enumerate(lines, start=1):
		# if index >= 7 and index < 10:

		if index >= 7:
			for condition in conditions:
				if line.find(condition) > 0:
					found = True
					break
				if found == True:
					break
			if found == True:
				# TODO: if found
				if line.strip().endswith("CYS"):
					print(filename)
					break		
					
					