import os.path
import sys
from subprocess import call

reference_file = sys.argv[1]
mobile_file = sys.argv[2]

# Get all .pdb file names from given directory
def get_file_content(file):
	if not file.endswith(".pdb"):
		# prevents reading hidden files like .DS_Sore
		return None
	# read the content
	return open(file).readlines()

# checking for the same conditions
def line_contains_the_same_conditions(line, conditions):
	for condition in conditions:
		if line.count(condition) > 1:
			return True
	return False	

# 	
def get_last_character(string):
	return string[len(string) - 1:]

# get the zone and list the two aa residues before that zone
def get_zones(file_content):
	res = []
	for line in file_content:
		if line.strip().startswith("SSBOND   3 "):
			if line_contains_the_same_conditions(line, conditions) == False:
				for condition in conditions:
					starts_at = line.find(condition)
					if starts_at > 0:
						stri = line[starts_at + len(condition):].strip()
						number = stri[:3]
						last = int(number) - 2
						res.append(get_last_character(condition) + str(last) + "-" + number) 		
		else:
 			continue	
	return res


conditions = ["CYS L", "CYS H", "CYS A", "CYS B"]


# first file
file_contents = get_file_content(reference_file)
if file_contents is not None:
	res1 = get_zones(file_contents)

	# second file
	file_contents = get_file_content(mobile_file)
	if file_contents is not None:
		res2 = get_zones(file_contents)

		# checking if zones are valid
		if len(res1) >= 2 and len(res2) >= 2:
			print("ZONE " + res1[0] + ":" + res2[0])
			print("ZONE " + res1[1] + ":" + res2[1])
			print("ATOMS CA")
			print("FIT")
			print("WRITE " + mobile_file.replace("pdb", "fit"))



















