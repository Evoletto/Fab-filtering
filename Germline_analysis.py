#*************************************************************************
#
#   Program:    Extraction of germline data 
#   File:       Germline_analysisc.py
#   
#   Version:    V1.0
#   Date:       03.08.19
#   Function:   Analysis of germline data and distance obtained from
#				cal_distance_automatic.py. It separates the date based on the light
#		        and heavy chain gene segments. The data is the plotted in the GraphPad.
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


distance_cal = "/Volumes/ALINASD/PhD_Rotations/Comp/Germline/Distance_CYS_SG_LYS_CA.txt" 
#distance_cal = sys.argv[1]

v_domains_content = open("/Volumes/ALINASD/PhD_Rotations/Comp/Germline/Vdomains_human.txt").readlines()
#v_domains_content = sys.argv[2]

c_domains_content = open("/Volumes/ALINASD/PhD_Rotations/Comp/Germline/Cdomains_human.txt").readlines()
#c_domains_content = sys.argv[3]

text_file = open("graph_data.txt", "w")

distance_cal_file_content = open(distance_cal).readlines()

def index_of_character(line, character, alter_char):
	char = character
	if line.find(character) < 0:
		char = alter_char
	return line.find(char)
	
def get_gene_segment_for_filename(filename, domain_file_content):
	segments = []
	for index, line in enumerate(domain_file_content, start=0):
		if line.strip().startswith(filename):
			gene_light = line[index_of_character(line, ":", "*") + 1:index_of_character(line, "-", "*")]
			next_line = domain_file_content[index + 1]
			gene_heavy = next_line[index_of_character(next_line, ":", "*") + 1:index_of_character(next_line, "-", "*")]

			if gene_light is not None:
				segments.append(gene_light)	
			if gene_heavy is not None:
				segments.append(gene_heavy)
			return segments
	
results = {}		
for index, line in enumerate(distance_cal_file_content, start=0):
# 	print(line)
	if line.find("model") >= 0:
		filename = line[index_of_character(line, "-", "-") + 1: index_of_character(line, ".", ".")]
		# next line is the result line
		
		next_line = distance_cal_file_content[index + 1]
		result = next_line[index_of_character(next_line, ":", ":") + 1:].strip() #+ " - " + filename 
		genes = []
		gene_c = get_gene_segment_for_filename(filename, v_domains_content)
		if gene_c is not None:
			genes.extend(gene_c)
		gene_v = get_gene_segment_for_filename(filename, c_domains_content)
		if gene_v is not None:
 			genes.extend(gene_v)
 		
		if len(genes) > 0:
			for gene in genes:
				if results.get(gene) is None:
					results[gene] = [result]
				else:
					results[gene].append(result)
		index = index + 2
		
		
for gene_segment in results:
	print(gene_segment)
	text_file.write(gene_segment)
	text_file.write("\n")
	for res in results[gene_segment]:
		print(res)	
		text_file.write(res)
		text_file.write("\n")
	text_file.write("\n\n")
text_file.close()
		