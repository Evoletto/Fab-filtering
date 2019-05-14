import re
import os, shutil
directory_path = "/Users/Alina/Dropbox/Comp/NR_LH_Combined_Kabat/"
 # get all the files in the listed directory
 # all_files = sorted(os.listdir(directory_path))
all_files = sorted(os.listdir(directory_path))

# create a loop, go through file one line at a time
for file in all_files:
# tmp = "/Users/Alina/Dropbox/Comp/NR_LH_Combined_Kabat/1A3R_1.pdb"
	filename = (directory_path + file)
	# read line by line in the filename
	lines = [line.rstrip('\n') for line in open(filename)]

	conditions = ["L    L    A", 
				  "L    L    L",
				  "H    H    B",
				  "H    H    H",
				  "L    L    C",
				  "H    H    D"]
	conditions2 = ["A    N    N",
				   "A    A    A",
				   "A    P    P",
				   "A    F    F"]

	found = False	

    # if it meets the conditions in line lines 7 to 10
	for index, line in enumerate(lines, start=1):
		# if index >= 7 and index < 10:
		# if statement, conditions
		if index >= 7 and index < 10:
			# checks for positive conditions
			for condition in conditions:
				if line.find(condition) > 0:
					found = True
					break		
			# checks for negative conditions
			for condition in conditions2:
				if line.find(condition) > 0:
					found = False
					break

		if found == True:
			# TODO: if found
			if line.strip().endswith("CYS"):
				shutil.copy(filename, "/Users/Alina/Dropbox/Comp/Fab filtered/")
				print(filename)
				break	






