#*************************************************************************
#
#   Program:    Second FAB screen
#   File:       FAB_second_screen.py
#   
#   Version:    V1.0
#   Date:       16.07.19
#   Function:   Second screening after full files were downloaded from the pdb website.
# 				Once screened, it copies them to a new location.
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
from subprocess import call


# First get the file names with correct labels of chains and if the LC ends on CYS
# select location where the folder with downloaded files is
directory_path = sys.argv[1]
# select location where to copy correct files
mobile_file = sys.argv[2]
#directory_path = "/Volumes/ALINASD/PhD_Rotations/Comp/Fab_filtered_RCSB/"
all_files = sorted(os.listdir(directory_path))
files_to_download = []

for index, file in enumerate(all_files, start=1):
	if not file.endswith(".pdb"):
		continue
	my_file = open(directory_path + file)
	# read the content
	file_contents = my_file.readlines()
	
	for line in file_contents:	
		if line.strip().startswith("SEQRES  17 L" and "TER") and line.strip().find("CYS") > 0:
			#print("LC ends on " + line.strip()[-9:-6])
			#files_to_download.append(file)
			#shutil.copy(directory_path + file, "/Volumes/ALINASD/PhD_Rotations/Comp/Fab_filtered_CYS_on_LC/")
			shutil.copy(directory_path + file, mobile_file)
			break
# 						
	#print(file.rsplit('.', 1)[0])