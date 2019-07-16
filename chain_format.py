#*************************************************************************
#
#   Program:    Formating chains
#   File:       chain_format.py
#   
#   Version:    V1.0
#   Date:       16.07.19
#   Function:   Splitting pdb models based on how many residues they have.
# 				Then replacing all atom numbers, atom residues and chain labels to 	
#				same name between all models.
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

#source = "/Volumes/ALINASD/PhD_Rotations/Comp/VMD_vis/results_for_VMD_replaced.pdb"#sys.argv[1]
source = sys.argv[1]
my_file = open(source)
file_contents = my_file.readlines()


text_file_31 = open("results_for_VMD_31_lines.pdb", "w")
text_file_35 = open("results_for_VMD_35_lines.pdb", "w")


def get_last_character(string):
	return string[len(string) - 1:]

# replacing string with replacementString in the array
def replaceStringInArray(array, string, replacementString):
	new_array = []
	for element in array:
		if element == string:
			new_array.append(replacementString)
		else:
			new_array.append(element)
	return new_array

# array's element at given index
def replace_element_in_array(in_ar, repl, i):
	if len(in_ar) > (i):
		new_array = in_ar
		new_array[i] = repl
		return new_array
	else:
		return in_ar

# append 'to_array' with value at given index in 'from_array'
def append_element_to_array(from_array, to_array, at_index):
	if len(from_array) > at_index - 1:
		label = from_array[at_index]
		new_ar = to_array
		new_ar.append(label)
		return new_ar
	else:
		return to_array

# formats array elements into string respecting pdb file format spacing
def array_to_pdb_line(array):
	combined = ""	
	spacing = ["<6", ">5", "<4", ">3", "<1", "<6", ">8", ">8", ">8", ">6", ">1"]
	for index, u in enumerate(array, start=0):
		combined = combined + ("{:" + str(spacing[index]) + "}").format(u.strip())
		if index == 1:
			combined = combined + "  " 
		if index == 3 or index == 4 or index == 9:
			combined = combined + " "
	return combined + "\n"
	
				
grouped_models = {}
single_model_lines = []
current_model_number = ""
# creates hash table from file containing all models
for index, line in enumerate(file_contents, start=0):
	stripped_line = line.strip()
	single_model_lines.append(line)
	if stripped_line.startswith("MODEL"):
		model_number = (stripped_line[stripped_line.find("MODEL") + len("MODEL"):]).replace(" ", "")
		current_model_number = str(model_number)
	elif stripped_line.startswith("ENDMDL"):
		# copy that array into grouped models hash table at given model number
		grouped_models[current_model_number] = single_model_lines
		single_model_lines = []

chain_numbers_31 = []
chain_numbers_35 = []
chain_labels_31 = []
chain_labels_35 = []

# modifies each model - changing chain labels, atom number
for model_key in grouped_models:
	model_line_no = len(grouped_models[model_key])

	for index, model_line in enumerate(grouped_models[model_key], start=0):
		line_into_array = list(filter(lambda a: a != '', model_line.split(" ")))
		last = line_into_array[len(line_into_array)-1]
		if last.startswith("1.00"):
			line_into_array = line_into_array[:len(line_into_array) - 1]
			line_into_array.append("1.00")
			line_into_array.append(last[4:])
		if line_into_array[0] == "ATOM":
			line_into_array[1] = str(index - 1)
			
		line_into_array = replaceStringInArray(line_into_array, "A", "L")
		line_into_array = replaceStringInArray(line_into_array, "B", "H")


		if model_line_no == 31:
			if len(chain_numbers_31) < 29:
				# creates chain label array that is used for all models that consists of 31 lines
				# from that array, chain number and label is replaced
				chain_numbers_31 = append_element_to_array(line_into_array, chain_numbers_31, 5)
				chain_labels_31 = append_element_to_array(line_into_array, chain_labels_31, 3)
		
			if index > 1 and index < 30:
				line_into_array = replace_element_in_array(line_into_array, chain_numbers_31[index - 2], 5)
				line_into_array = replace_element_in_array(line_into_array, chain_labels_31[index - 2], 3)
				text_file_31.write(array_to_pdb_line(line_into_array))
			else:
				text_file_31.write(array_to_pdb_line(line_into_array))
		if model_line_no == 35:
			if len(chain_numbers_35) < 33:
				chain_numbers_35 = append_element_to_array(line_into_array, chain_numbers_35, 5)
				chain_labels_35 = append_element_to_array(line_into_array, chain_labels_35, 3)
				
			if index > 1 and index < 34:
				line_into_array = replace_element_in_array(line_into_array, chain_numbers_35[index - 2], 5)
				line_into_array = replace_element_in_array(line_into_array, chain_labels_35[index - 2], 3)
				text_file_35.write(array_to_pdb_line(line_into_array))
			else:
				text_file_35.write(array_to_pdb_line(line_into_array))
		
text_file_31.close()
text_file_35.close()


