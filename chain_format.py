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

import os

for file_index in range(1, 11):
	# loop from 1 to 10, 11 not included
	source = "/Volumes/ALINASD/PhD_Rotations/Comp/VMD_vis/results_for_VMD_v" + str(file_index) + ".pdb" 
	#source = sys.argv[1]
	my_file = open(source)
	file_contents = my_file.readlines()


	# text_file_31 = open("results_for_VMD_31_lines.pdb", "w")

	def get_chain_numbers(model):
		numbers = []
		for line in model:
			if line.startswith("ATOM"):
				number = line[22:26]
				numbers.append(number)
		return numbers

	# modifies each model - changing chain labels, atom number
	replaced_model_lines = []
	grouped_models = {}
	single_model_lines = []


	# creates hash table from file containing all models
	model_line_count = 0
	for index, line in enumerate(file_contents, start=0):
		model_line_count += 1
		stripped_line = line.strip()
		single_model_lines.append(line)
		if stripped_line.startswith("MODEL"):
			model_number = (stripped_line[stripped_line.find("MODEL") + len("MODEL"):]).replace(" ", "")
			current_model_number = str(model_number)
		elif stripped_line.startswith("ENDMDL"):
			# copy that array into grouped models hash table at given model number
	# 		print(":", grouped_models[model_line_count])
			if grouped_models.get(model_line_count):
				grouped_models[model_line_count].append(single_model_lines)
			else:
				grouped_models[model_line_count] = [single_model_lines]		
			single_model_lines = []
			model_line_count = 0

	# for line_count in grouped_models:
	# 	print(line_count, ":")
	# 	for l in grouped_models[line_count]:
	# 		for i in l:
	# 			print(i)
		
	# modifies each model - changing chain labels, atom number
	mod = []
	for line_count in grouped_models:
		base_model = grouped_models[line_count][0]
	# 	print("base model for ", line_count, " : ", base_model)
		for models in grouped_models[line_count]:
			# models for this line len

	# 		k = list(grouped_models.keys())[0]
		
			base_chain_numbers = get_chain_numbers(base_model)
			new_model_lines = []
			for index, model_line in enumerate(models,start=0):
	# 			for index, model_line in enumerate(grouped_models[model_key], start=0):
				if model_line.startswith("ATOM"):
					# replace numbers
					# check if valid index - number of lines
					new_line = model_line[:22] + str(base_chain_numbers[index - 2]) + model_line[26:]
					new_model_lines.append(new_line)
				else:
					# copy current line without modifications
					new_model_lines.append(model_line)
			mod.append(new_model_lines)
		break

	os.remove(source) #this deletes the file
	# new file
	pdb_file = open(source, "w")
	for model in mod:
		for model_line in model:
			#print(ln)
			pdb_file.write(model_line)
	pdb_file.close()
	# 
	# for m in mod:
	# 	for n in mod[m]:
	# 		print(n)