#*************************************************************************
#
#   Program:    Splitting files
#   File:       new_chain_mutation.py
#   
#   Version:    V1.0
#   Date:       22.07.19
#   Function:   Splitting pdb models based on where the LYS is in the distance of CYS.
#				Replacing unusal chain labels to have common one amongst all files.
# 				
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



import os.path
import urllib.request
import sys

source = "/Volumes/ALINASD/PhD_Rotations/Comp/VMD_vis/results_for_VMD_replaced.pdb" 
#source = sys.argv[1]
my_file = open(source)
file_contents = my_file.readlines()


grouped_models = {}
single_model_lines = []
current_model_number = ""

# list all residue labels from each model in an array
def get_model_labels(model):
	current_label = ""
	current_seq_no = ""
	residues = []
	for line in model:
		if line.strip().startswith("ATOM"):
			seq_no = line[23:26]
			label = line[17:20]
			if current_seq_no != seq_no or current_label.strip() != label.strip():
				current_seq_no = seq_no
				current_label = label
				# another chain, get id
				residue_name = label
				residues.append(residue_name)
	return residues
		
residue_classificators = [
	["GLY", "GLY", "CYS", "LYS", "GLY", "CYS"], #1
	["LYS", "GLY", "GLY", "CYS", "GLY", "GLY", "CYS"], #2
	["LYS", "GLY", "GLY", "CYS", "LYS", "GLY", "CYS"], #3
	["LYS", "GLY", "CYS", "GLY", "GLY", "CYS", "LYS"], #4
	["LYS", "GLY", "CYS", "GLY", "GLY", "CYS"],			#5
	["GLY", "GLY", "CYS", "LYS", "GLY", "CYS", "LYS"], #6
	["LYS", "GLY", "GLY", "CYS", "LYS", "GLY", "GLY", "CYS"], #7
	["LYS", "GLY", "CYS", "LYS", "GLY", "GLY", "CYS"], #8
	["GLY", "GLY", "CYS", "GLY", "GLY", "CYS", "LYS"], #9
	["LYS", "LYS", "CYS", "GLY", "GLY", "CYS", "LYS"] # 10
]
def copy_model_to_file(model, class_id):
	text_file = open("results_for_VMD_v" + str(class_id) + ".pdb", "a+")
	for line in model:
		text_file.write(line)
	text_file.close()
	
def is_model_compatible_with_classificator(classificator, model_class):
	if len(classificator) == len(model_class):
		for index, item in enumerate(classificator, start=0):
			if item != model_class[index]:	
				return False
		# matching
		return True
	# different lengths, doesn't qualify 
	return False
		
# get model classification
def get_model_classification(model_class):
	class_i = ""
	for index, classificator in enumerate(residue_classificators, start=1):
		if is_model_compatible_with_classificator(classificator, model_class):
			return str(index)
	return str(-1)
			
	
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

# modifies each model - changing chain labels, atom number
mod = {}
for model_key in grouped_models:
	model_line_no = len(grouped_models[model_key])
	new_mod_group = []
	for index, model_line in enumerate(grouped_models[model_key], start=0):
		if model_line.startswith("ATOM"):
			# replace atom number
			atom_number = model_line[6:11]
			repla = "{:>5}".format(str(index - 1))
			mod_line = model_line.replace(atom_number, repla)
			
			# replace chain label
			chain_id = str(mod_line[21])
			repla1 = ""
			if chain_id == "A":
				repla1 = "L"
			elif chain_id == "B":
				repla1 = "H"
			elif chain_id == "E":
				repla1 = "L"
			elif chain_id == "G":
				repla1 = "L"
			elif chain_id == "L":
				repla1 = "L"
			elif chain_id == "H":
				repla1 = "H"
					
			mod_line_c = mod_line[:21] + repla1 + mod_line[22:]
			new_mod_group.append(mod_line_c)
		else:
			new_mod_group.append(model_line)
	mod[model_key] = new_mod_group

for m in mod:
	# check model clasification
	model_ids = get_model_labels(mod[m])
	class_id = get_model_classification(model_ids)
	print(model_ids, " :-> ", class_id)
	copy_model_to_file(mod[m], class_id)

		