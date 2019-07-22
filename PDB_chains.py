
import os


directory_path = "/Volumes/ALINASD/PhD_Rotations/Comp/Compatible_SSBOND/PDB_FAB_files/"
	#file = "1NGQ_1.pdb"
all_files = sorted(os.listdir(directory_path))
acceptable_ids = ["L", "H", "A", "B", "G", "E"]
for index, file in enumerate(all_files, start=1):
	if not file.endswith(".pdb"):
		# prevents reading hidden files like .DS_Sore
		continue
	if file.startswith("."):
		# prevents reading hidden files like .DS_Sore
		continue


	text_file = open(file.replace(".pdb", "_fab.pdb"), "w")
	my_file = open(directory_path + file)
	# read the content
	file_contents = my_file.readlines()
	for line in file_contents:
		if line.strip().startswith("ATOM"):
			id = line[21]
# 			print(id)
			for acceptable_id in acceptable_ids:
# 				print("is ", acceptable_id, " in ", id)
				if id.find(acceptable_id) >= 0:
# 					print(line)
					text_file.write(line)
	text_file.close()		



