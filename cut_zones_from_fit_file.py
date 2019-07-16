#*************************************************************************
#
#   Program:    cut_zones_from_fit_file
#   File:       cut_zones_from_fit_file.py
#   
#   Version:    V1.0
#   Date:       02.07.19
#   Function:   Once the specified zones are identified from 'get_new_zones.py"
#				and nearby LYS is found from "get_min_max_from_zones.py" then these zones	
#				can be found in .fit files and copied to a new file. 
#				It is to be used with BASH code called "call_out_new_zones.sh"
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


if len(sys.argv) > 1:
	fit_filename = sys.argv[1]
	chains = sys.argv[2].split(",")
	current_index = sys.argv[3]
	if len(chains) > 0:
		copied_lines = []
	
		file = open(fit_filename)
		file_contents = file.readlines()
		copied_lines.append("MODEL        " + current_index)
		copied_lines.append("REMARK " + fit_filename)
		for line in file_contents:
			for chain_element in chains:
				chain = str(chain_element.replace("'", ""))
				
				chain_label = chain[0]
				chain_value = chain[1:]
				
				# take each file line and split it into array by space character
				# then remove empty elements (spaces)
				line_into_array = list(filter(lambda a: a != '', line.split(" ")))
				
				# loop through above array's items
				for index, element in enumerate(line_into_array, start=0):
					# check if current element is the same as chain label
					if element == chain_label:
						# if so, then check if the next element in the array matches its value
						if line_into_array[index + 1] == chain_value:
		 					# copy that line
							copied_lines.append(line.replace("\n", ""))
							break
		#print("ENDMDL_" + current_index)
		copied_lines.append("ENDMDL")	
		
		# check if first line starts with LYS
		if len(copied_lines) > 2:
			if copied_lines[2].find("LYS") > 0:
				for copied_line in copied_lines:
					print(copied_line)
		