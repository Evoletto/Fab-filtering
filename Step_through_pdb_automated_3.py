#*************************************************************************
#
#   Program:    Going through pdb files and identifying ZONEs for ProFit analysis
#   File:       step_through_pdb_automated_3.py
#   
#   Version:    V1.0
#   Date:       27.06.19
#   Function:   Analysis of the .pdb files. Check for specific ZONES and prints Zone range
#		 		and chain label and commands for ProFit. This script is to be used with
# 				run_script_3
#
#   
#   Copyright:  (c) Alina Chrzastek, UCL, 2019
#   Author:     Alina Chrzastek
#   Address:    Institute of Structural and Molecular Biology
#               Division of Biosciences
#               University College
#               Gower Street
#               London
#               WC1E 6BT
#   EMail:      a.chrzastek.18@ucl.ac.uk 
#*************************************************************************

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
						chain_name = get_last_character(condition)
						res.append(chain_name + str(last) + "-" + chain_name + number) 		
		else:
 			continue	
	return res


conditions = ["CYS L", "CYS H", "CYS A", "CYS B", "CYS G", "CYS E", "CYS C"]


# first file
file_contents = get_file_content(reference_file)
if file_contents is not None:
	zone_pdb1 = get_zones(file_contents)

	# second file
	file_contents = get_file_content(mobile_file)
	if file_contents is not None:
		zone_pdb2 = get_zones(file_contents)

		# checking if zones are valid
		if len(zone_pdb1) >= 2 and len(zone_pdb2) >= 2:
			print("ZONE " + zone_pdb1[0] + ":" + zone_pdb2[0])
			print("ZONE " + zone_pdb1[1] + ":" + zone_pdb2[1])
			print("ATOMS CA")
			print("FIT")
			print("WRITE " + reference_file.replace(".pdb","-") + mobile_file.replace("pdb", "fit"))



















