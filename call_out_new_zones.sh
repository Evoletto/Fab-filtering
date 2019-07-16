#*************************************************************************
#
#   Program:    call_out_new_zones
#   File:       call_out_new_zones.sh
#   
#   Version:    V1.0
#   Date:       27.06.19
#   Function:   BASH command that runs the get_new_zones.py, get_min_max_from_zones.py,
#				cut_zones_from_fit.py
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

#!/bin/bash

ref=3L5X_1.pdb
mobile_dir="$1"
index=1

for mobile in "$mobile_dir"/*.pdb 
do
	zones=$(python3 get_new_zones.py $ref $mobile)
	a=${ref%.*}   # remove suffix starting with "_"
	b=${mobile:$((${#mobile} - 10)):6}
	fitName="$a-$b.fit"

 	area_res=$(pdbfindnearres -l $zones LYS $fitName)

	chains=$(python3 get_min_max_from_zones.py "$area_res" "$zones")

	# cut zones from fit file
#  	umc=$(python3 cut_zones_from_fit_file.py $fitName $chains "$index")
#  	echo "$umc"
	python3 cut_zones_from_fit_file.py $fitName $chains "$index" >> results_for_VMD.pdb

	index=$(( $index + 1 ))

done