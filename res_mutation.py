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


#file_path = "/Volumes/ALINASD/PhD_Rotations/Comp/VMD_vis/results_for_VMD.pdb" 
file_path = sys.argv[1]

conditions = ["CYS", "LYS"]
mutation = "GLY"
unwanted_res = ["ASN", "GLU", "PRO", "VAL", "ALA", "SER", "ARG", "ASP", "VAL", "THR", "LEU"]

my_file = open(file_path)
file_contents = my_file.readlines()
text_file = open("results_for_VMD_replaced.pdb", "w")

lines_to_process = []
for index, line in enumerate(file_contents, start=0):
	if line.strip().startswith("ATOM"):
		if line.strip().find("CA") > 0:
			lines_to_process.append(file_contents[index - 1])
			lines_to_process.append(file_contents[index])
			lines_to_process.append(file_contents[index + 1])
			lines_to_process.append(file_contents[index + 2])
	else:
		lines_to_process.append(line)
		
for process_line in lines_to_process:
	if process_line.strip().startswith("ATOM"):
		copied_line = process_line
		for un_res in unwanted_res:	
			if process_line.strip().find(un_res) > 0:
# 					print("Replacing line", line, " with: ", mutation)
				copied_line = copied_line.replace(un_res, mutation)
# 					print("Replaced line:", copied_line)
		text_file.write(copied_line)
	else:
		text_file.write(process_line)
text_file.close()
