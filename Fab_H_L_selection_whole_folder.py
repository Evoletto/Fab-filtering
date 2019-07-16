import re
import os, shutil
import os.path

# open file
directory_path = "/Users/Alina/Dropbox/Comp/NR_LH_Combined_Kabat/"
all_files = sorted(os.listdir(directory_path))

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


	print(file.rsplit('.', 1)[0], light_chain, heavy_chain)
	
	
# code works