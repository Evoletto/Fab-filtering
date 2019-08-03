#*************************************************************************
#
#   Program:    matrix
#   File:      	matrix.py
#   
#   Version:    V1.0
#   Date:       27.06.19
#   Function:   Runs through the RMSDs.txt file. Adds all files to all files
#				and generates sum of each. Prints the lowest sum.
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
import sys

#rmsd_file_path = "/Users/Alina/Google_Drive_BBK/Comp/Matrix/RMSDs_3.txt" 
rmsd_file_path = sys.argv[1]
#sys.stdout = open("/Users/Alina/Google_Drive_BBK/Comp/Matrix/Matrix_sum.txt", "w")
sys.stdout = open(sys.argv[2], "w")

rmsd_file = open(rmsd_file_path)
file_contents = rmsd_file.readlines()
matrix = {}
ref1 = {}
prev_key = ""
for line in file_contents:
	# get first file name
	delimiter = line.find("-")
	first_filename = line[:delimiter].replace(".pdb", "")
	# get second file name
	second_filename = line[delimiter + 1:line.find(".pdb:")]
	# get rms value
	rms_value = float(line[line.find("RMS:") + len("RMS:"):])
	# create array with those values
	if prev_key == "":
		prev_key = first_filename
		
	if prev_key == first_filename:
		# continue with current array row
		ref1[second_filename] = rms_value
	else: 
		#new row
		matrix[prev_key] = ref1
		ref1 = {}
		ref1[second_filename] = rms_value
		
		
		
	prev_key = first_filename
	
lowest = 9999999
column_name = ""
for i in matrix:
	row = matrix[i]
	sum = 0.0
	for key, value in row.items():
		sum += float(value)
	print("sum for row: ", i, "= ", round(sum, 3))
	if sum == 0.0:
		continue
	if sum < lowest:
		lowest = sum
		column_name = i
print("lowest:",column_name, round(lowest, 3))
sys.stdout.close()




