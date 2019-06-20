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
file1 = "1A3R_1.pdb"
file2 = "1AD9_1.pdb"

conditions = ["CYS L", "CYS H", "CYS A", "CYS B"]

my_file = open(directory_path + file1)
file_contents = my_file.readlines()

res1 = []
res2 = []

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
		else:
 			print("Contains the same conditions, file igonred")
 			
other_file = open(directory_path + file2)
file_contents = other_file.readlines()


for line in file_contents:
	if line.strip().startswith("SSBOND   3 "):
		if line_contains_the_same_conditions(line, conditions) == False:
			for condition in conditions:
				starts_at = line.find(condition)
				if starts_at > 0:
					stri = line[starts_at + len(condition):].strip()
					number = stri[:3]
					last = int(number) - 2
					res2.append(get_last_character(condition) + str(last) + "-" + number)		
		else:
 			print("Contains the same conditions, file igonred")
 	

if len(res1) < 2 or len(res2) < 2:
	print("conditions not found")
else:
	print("ZONE " + res1[0] + ":" + res2[0])
	print("ZONE " + res1[1] + ":" + res2[1])




# if not then ignore the file
















