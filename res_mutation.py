#*************************************************************************
#
#   Program:    Mutation of residues
#   File:       res_mutation.py
#   
#   Version:    V1.0
#   Date:       16.07.19
#   Function:   Program mutates residues that are not CYS or LYS to GLY
#				
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

import re
import os, shutil
import os.path
import urllib.request
import sys


file_path = "/Volumes/ALINASD/PhD_Rotations/Comp/VMD_vis/results_for_VMD.pdb" 
# file_path = sys.argv[1]

conditions = ["CYS", "LYS"]
mutation = "GLY"
unwanted_res = ["ASN", "GLU", "PRO", "VAL", "ALA", "SER", "ARG", "ASP", "VAL", "THR", "LEU"]

my_file = open(file_path)
file_contents = my_file.readlines()
text_file = open("results_for_VMD_replaced.pdb", "w")

lines_to_process = []

# replace chains labels
def replace_chain_label(line, unwanted_labels, replacement_label):
	new_line = line
	for un_res in unwanted_labels:	
		if line.strip().find(un_res) > 0:
# 			Replacing with mutation
			new_line = line.replace(un_res, mutation)
			return new_line
	return new_line

# get lines from file content at given indexes
def get_lines_from_file(file_lines, from_index, to_index):
	lines_to_copy = []
	for i in range(from_index, to_index + 1):
		line_to_cpy = file_lines[i]
		if line_to_cpy not in lines_to_copy:
# 			print(line_to_cpy, " not in ",lines_to_copy)
			lines_to_copy.append(line_to_cpy)
	return lines_to_copy
	
# replace all unwanted chain labels to gly		
for process_line in file_contents:
	if process_line.strip().startswith("ATOM"):
		copied_line = replace_chain_label(process_line, unwanted_res, mutation)
		lines_to_process.append(copied_line)
	else:
		lines_to_process.append(process_line)

# for l in lines_to_process:
# 	text_file_write(l)
# text_file.close()
lines_filtered = []		
for index, line in enumerate(lines_to_process, start=0):
	if line.strip().startswith("ATOM"):
		# if line strip contains GLY:	
		if line.strip().find("CA") > 0:
			if line.strip().find("GLY") > 0:
				lines_filtered.extend(get_lines_from_file(lines_to_process, index - 1, index + 2))
				# index - 1 #N
				# index     #CA
				# index + 1 #C
				# index + 2 #O

			# if line strip contains LYS:
			if line.strip().find("LYS") > 0:
				lines_filtered.extend(get_lines_from_file(lines_to_process, index - 1, index + 7))
				# index - 1 #N
				# index     #CA
				# index + 1 #C
				# index + 2 #O
				# index + 3 #CB
				# index + 4 #CG
				# index + 5 #CD
				# index + 6 #CE
				# index + 7 #NZ
 			
 			# if line strip contains CYS:
			if line.strip().find("CYS") > 0:
				if file_contents[index + 5].find("OXT") > 0:
					lines_filtered.extend(get_lines_from_file(lines_to_process, index - 1, index + 5))
				else:
					lines_filtered.extend(get_lines_from_file(lines_to_process, index - 1, index + 4))
				# index - 1 #N
				# index	  #CA
				# index + 1 #C
				# index + 2 #O
				# index + 3 #CB
				# index + 4 #SG
				# index + 5 #OXT not needed
			
	else:
		lines_filtered.append(line)

for ln in lines_filtered:
	text_file.write(ln)
text_file.close()
