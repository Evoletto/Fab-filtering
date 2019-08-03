#*************************************************************************
#
#   Program:    Calculating distances between atoms of specific residues
#   File:       cal_distance_automatic.py
#   
#   Version:    V1.0
#   Date:       29.07.19
#   Function:   Calculates distances between specified atoms od residues.
#				Runs from terminal, ie 
#  				"cal_distance_automatic.py file.pdb CYS 226 O LYS 224 N"
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

import sys
import math

def calculate_distance(coords):
	if len(coords) == 6:
		x1 = float(coords["x1"])
		y1 = float(coords["y1"])
		z1 = float(coords["z1"])
		x2 = float(coords["x2"])
		y2 = float(coords["y2"])
		z2 = float(coords["z2"])		
		return math.sqrt(math.pow(x1-x2, 2) + math.pow(y1-y2, 2) + math.pow(z1-z2, 2))					
	else:
		return None
		
if len(sys.argv) > 6:
	fit_filename = sys.argv[1]
	first_res = sys.argv[2]
	first_res_seq_no = sys.argv[3]
	first_res_atm_id = sys.argv[4]
	
	second_res = sys.argv[5]
	second_res_seq_no = sys.argv[6]
	second_res_atm_id = sys.argv[7]
	
	print("First res: ", first_res, first_res_seq_no, first_res_atm_id)
	print("Second res: ", second_res, second_res_seq_no, second_res_atm_id)
	
	# group models
	grouped_models = {}
	single_model_lines = []
	current_fit_file = ""
	file_contents = open(fit_filename).readlines()
	# creates hash table from file containing all models

	for index, line in enumerate(file_contents, start=0):
		stripped_line = line.strip()
		single_model_lines.append(line)
		if stripped_line.startswith("REMARK"):
			current_fit_file = stripped_line[len("REMARK"):]
		elif stripped_line.startswith("ENDMDL"):
			grouped_models[current_fit_file] = single_model_lines
			single_model_lines = []

	for model_name in grouped_models:
		print("model name: ", model_name)
		coords = {}
		for line in grouped_models[model_name]:
			if line.strip().startswith("ATOM"):
				current_res = line[17:20].strip()
				current_res_seq_no = line[22:26].strip()
				current_atom = line[12:16].strip()
				if first_res == current_res and first_res_seq_no == current_res_seq_no and first_res_atm_id == current_atom:
					coords["x1"] = float(line[30:38])
					coords["y1"] = float(line[38:46])
					coords["z1"] = float(line[46:54])
				elif second_res == current_res and second_res_seq_no == current_res_seq_no and second_res_atm_id == current_atom:
					coords["x2"] = float(line[30:38])
					coords["y2"] = float(line[38:46])
					coords["z2"] = float(line[46:54])
		print("Result: ", calculate_distance(coords))
else:
	print("Incorrect format")	



