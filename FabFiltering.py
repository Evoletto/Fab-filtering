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
	filename = (directory_path + file)
	lines = [line.rstrip('\n') for line in open(filename)]

	conditions = ["L    L    A", 
				  "L    L    L",
				  "H    H    B",
				  "H    H    H",
				  "L    L    C",
				  "H    H    D"]


	for index, line in enumerate(lines, start=1):
		if index >= 7 and index < 10:
			found = False	
			for condition in conditions:
				if line.find(condition) > 0:
					print(line)
					print(filename)
					found = True
					break
				if found == True:
					break
			if found == True:
				break		
					
					
					
					
					
					