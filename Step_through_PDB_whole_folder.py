import re
import os, shutil
import os.path
import urllib.request

def get_last_character(string):
	return string[len(string) - 1:]
	
def line_contains_the_same_conditions(line, conditions):
	for condition in conditions:
		if line.count(condition) > 1:
			return True
	return False

directory_path = "/Users/Alina/Google_Drive_BBK/Comp/Compatible/"
all_files = sorted(os.listdir(directory_path))


conditions = ["CYS L", "CYS H", "CYS A", "CYS B"]

res1 = []

for index, file in enumerate(all_files, start=1):
	if not file.endswith(".pdb"):
		continue
	my_file = open(directory_path + file)
	# read the content
	file_contents = my_file.readlines()

	for line in file_contents:
		if line.strip().startswith("SSBOND   3 "):
			if line_contains_the_same_conditions(line, conditions) == False:
				for condition in conditions:
					starts_at = line.find(condition)
					if starts_at > 0:
						stri = line[starts_at + len(condition):].strip()
						number = stri[:3]
						last = int(number) - 2
						res1.append(get_last_character(condition) + str(last) + "-" + number) 
						shutil.copy(directory_path + file, "/Users/Alina/Google_Drive_BBK/Comp/Compatible_SSBOND/")		
			else:
				print("Contains the same conditions, file igonred")
				
					
					
					















