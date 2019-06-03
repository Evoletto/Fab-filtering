import re
import os, shutil
import os.path
import urllib.request

# First get the file names with correct labels of chains and if the LC ends on CYS
directory_path = "/Users/Alina/Google_Drive_BBK/Comp/NR_LH_Combined_Kabat/"
all_files = sorted(os.listdir(directory_path))
files_to_download = []

for index, file in enumerate(all_files, start=1):
	if not file.endswith(".pdb"):
		# prevents reading hidden files like .DS_Sore
		continue
	my_file = open(directory_path + file)
	# read the content
	file_contents = my_file.readlines()

	light_chain = ""
	heavy_chain = ""

	for line in file_contents:
		if line.startswith("REMARK 950 CHAIN L    L"):
			light_chain = line[len(line) - 2]
	
		if line.startswith("REMARK 950 CHAIN H    H"):
			heavy_chain = line[len(line) - 2]
			
		if line.strip().startswith("SEQRES  17 L") and line.strip().find("CYS") > 0: 
			#print("LC ends on " + line.strip()[-3:])
			files_to_download.append(file)
			break
						
	#print(file.rsplit('.', 1)[0], light_chain, heavy_chain)
	
print(files_to_download)
for file in files_to_download:
	striped_filename = file.rsplit('_', 1)[0]
	url = 'https://files.rcsb.org/download/' + striped_filename + ".pdb"
	print("will download file at: ",url) 
	urllib.request.urlretrieve(url, '/Users/Alina/Google_Drive_BBK/Comp/Fab_filtered_RCSB/' + file)


# First get the file names with correct labels of chains and if the LC ends on CYS
directory_path = "/Users/Alina/Google_Drive_BBK/Comp/Fab_filtered_RCSB/"
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
			shutil.copy(directory_path + file, "/Users/Alina/Google_Drive_BBK/Comp/Fab_filtered_CYS_on_LC/")
			break
# 						
	#print(file.rsplit('.', 1)[0])


	
	

