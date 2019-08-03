#*************************************************************************
#
#   Program:    Extraction of FAB information
#   File:      	FAB_Two_filters_final_whole_folder_automated.py
#   
#   Version:    V1.0
#   Date:       27.06.19
#   Function:   Analysis of the FAB .pdb files. Looking for CYS on the C-terminus of 	
#				Light Chain. Downloads the correct pdb files from www.rcsb.org
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

# Get all .pdb file names from given directory
def get_file_content(directory_path, filename):
	if not filename.endswith(".pdb"):
		# prevents reading hidden files like .DS_Sore
		return None
	# read the content
	return open(directory_path + filename).readlines()
	
	
# Download file from web to set directory path
def download_file(file, to_directory):
	striped_filename = file.rsplit('_', 1)[0]
	url = 'https://files.rcsb.org/download/' + striped_filename + ".pdb"
	urllib.request.urlretrieve(url, to_directory + file)


# Download files from provided array of files to set directory path
def download_files(files, path):
	count = len(files)
	print("\n\nWill attempt to download ", count, " files")
	input("Press enter to continue")
	for index, file_to_download in enumerate(files, start=1):
		print("Downloading file ", index, "/", count)	
		download_file(file_to_download, path)
		#print(file.rsplit('.', 1)[0], light_chain, heavy_chain)

# Copy files that met given condition to a new directory
def check_downloaded_files_for_compatibility(directory_to_files):
	all_files = sorted(os.listdir(directory_to_files))
	path_to_compatible_files = directory_to_files + "Compatible"
	
	# create folder if does not exists and remove old version if already exists
	if os.path.exists(path_to_compatible_files):
		shutil.rmtree(path_to_compatible_files)
	
	os.makedirs(path_to_compatible_files)

	for index, file in enumerate(all_files, start=1):
		print("Checking file ", index, "/", len(all_files))
		file_contents = get_file_content(directory_to_files, file)
		if file_contents is None:
			continue
		for line in file_contents:
			if line.strip().startswith("SEQRES  17 L" and "TER") and line.strip().find("CYS") > 0:
				#print("LC ends on " + line.strip()[-9:-6])
				shutil.copy(directory_to_files + file, path_to_compatible_files)
				break
	
	call(["open", path_to_compatible_files])

# Finish program
def close():
	sys.exit()

files_to_download = []
directory_path = input("Please provide directory path to your original repository\n") 
if len(directory_path) > 0:
	directory_to_download_files = input("Please provide directory path where compatible files will be downloaded\n")
	if len(directory_to_download_files) > 0:
		all_files = sorted(os.listdir(directory_path))
		for index, file in enumerate(all_files, start=1):
			print("Checking file ", index, "/", len(all_files))
			file_contents = get_file_content(directory_path, file)
			if file_contents is None:
				continue
		
			light_chain = ""
			heavy_chain = ""

			for line in file_contents:
				striped_line = line.strip()
				if line.startswith("REMARK 950 CHAIN L    L"):
					light_chain = striped_line[-1]
				if line.startswith("REMARK 950 CHAIN H    H"):
					heavy_chain = striped_line[-1]
				if striped_line.startswith("SEQRES  17 L") and striped_line.find("CYS") > 0: 
					files_to_download.append(file)
					break
		file_count = len(files_to_download)
		files_in_download_directory = os.listdir(directory_to_download_files)
		if len(files_in_download_directory) > 1:
			print("Files in directory where you want to download new files already exists,\ndo you want to override them?")
			action = input("Download or Skip? (D/S): ")
			if action == "D":
				download_files(files_to_download, directory_to_download_files)
				check_downloaded_files_for_compatibility(directory_to_download_files)
			else:
				print("Skipping downloading files")
				check_downloaded_files_for_compatibility(directory_to_download_files)
		else:
			download_files(files_to_download, directory_to_download_files)
			check_downloaded_files_for_compatibility(directory_to_download_files)
		
		print("Done")
	else:
		print("Directory path provided is empty, closing\n")
		close()	
else:
	print("Directory path provided is empty, closing\n")
	close()





