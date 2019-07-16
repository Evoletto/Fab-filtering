#*************************************************************************
#
#   Program:    Finding specified ZONES
#   File:       Step_through_PDB.py
#   
#   Version:    V1.0
#   Date:       16.07.19
#   Function:   Specifying reference and mobile file, then finding ZONE of intrest
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


def get_last_character(string):
	return string[len(string) - 1:]

def line_contains_the_same_conditions(line, conditions):
	for condition in conditions:
		if line.count(condition) > 1:
			return True
	return False	
	
	
#directory_path = "/Volumes/ALINASD/PhD_Rotations/Comp/Compatible_SSBOND/"
#directory_path = sys.argv[1]
#file1 = "1A3R_1.pdb"
file1 = input("Please provide directory path to your reference file\n")
#file1 = sys.argv[2]
#file2 = "1AQK_1.pdb"
file2 = input("Please provide directory path to your mobile file\n")
#file2 = sys.argv[3]

conditions = ["CYS L", "CYS H", "CYS A", "CYS B", "CYS G", "CYS E", "CYS C"]

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
					chain_name = get_last_character(condition)
					res1.append(chain_name + str(last) + "-" + chain_name + number) 		
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
					chain_name = get_last_character(condition)
					res2.append(chain_name + str(last) + "-" + chain_name + number)		
		else:
 			print("Contains the same conditions, file igonred")
 	

if len(res1) < 2 or len(res2) < 2:
	print("conditions not found")
else:
	print("ZONE " + res1[0] + ":" + res2[0])
	print("ZONE " + res1[1] + ":" + res2[1])




# if not then ignore the file
















