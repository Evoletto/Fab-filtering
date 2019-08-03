#*************************************************************************
#
#   Program:    Uses pdbfindnearres to find residue of intrest 
#   File:       get_min_max_from_zones.py
#   
#   Version:    V1.0
#   Date:       02.07.19
#   Function:   It uses the specified zones for each zone to find the near residue, 
#				here lysine (LYS) from .pdb files. It is to be used with BASH code called	
#				"call_out_new_zones.sh"
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
from subprocess import call

def get_first_character(string):
	return str(string[:1])

def split_string_by(string, delimiter):
	delimiter_index = string.find(delimiter)
	if delimiter_index >= 0:
		first_part = string[:delimiter_index]
		second_part = string[delimiter_index + 1:]
		return [first_part, second_part]
	else:
		return [string]

def get_last_character(string):
	return string[len(string) - 1:]

def get_last_n_character(n, string):
	return string[len(string) - n:]

def get_zones_from_string(zone):
	split_zone = split_string_by(zone, "-")
	if len(split_zone) == 1:
		# short zones (single chain)
		first = split_zone[0]
		last_digit = int(get_last_n_character(2, first))
		second = first[:len(first) - 2] + (str(last_digit - 1))
		split_zone.insert(1, second)
		third = ""
		third_end = last_digit - 2
		if third_end < 10 :
			third = first[:len(first) - 2] + "0" + (str(third_end))
		else:
			third = first[:len(first) - 2] + (str(third_end))
		split_zone.insert(2, third)
		return split_zone
	else:
		# old way, zones
		#'L211-L213'
		if len(split_zone) > 0:
			first = split_zone[0]
			last_digit = int(get_last_character(first))
			copied = first[:len(first) - 1] + (str(last_digit + 1))
			split_zone.insert(1, copied)
			return split_zone

if len(sys.argv) > 1:
	find_area_array = sys.argv[1].split("\n")
	zones = sys.argv[2]
	if len(find_area_array) > 0:
	
		split_zones = split_string_by(zones, ",")
		if len(split_zones) > 1:		
			first_chain = get_first_character(split_zones[0]).strip()
			second_chain = get_first_character(split_zones[1]).strip()
		
			first_chain_max = -1
			second_chain_max = -1
			for area in find_area_array:
				if area.find(first_chain) >= 0:
					value = int(area[1:])
					first_chain_max = max(first_chain_max, value)
				if area.find(second_chain) >= 0:
					value = int(area[1:])
					second_chain_max = max(second_chain_max, value)	
			# print("Zones:", split_zones)
# 			print("Max for",first_chain, first_chain_max)
# 			print("Max for",second_chain, second_chain_max)
			res = []
			if first_chain_max > 0:
				chain = first_chain + str(first_chain_max)
				res.append(chain)
			if second_chain_max > 0:
				chain = second_chain + str(second_chain_max)
				res.append(chain)
			for zone in split_zones:
				
				res.extend(get_zones_from_string(zone))
			
			print(",".join(set(res)))

		