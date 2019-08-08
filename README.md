# Project Title

Proximity of lysine to light chain terminal of the disulfide bridge in Fab region of antibody

## Flow of the project:

### Preparation of the files for analysis

Initial antibody .pdb files were first downloaded from the AbDB (Antibody Structure Database) (http://www.bioinf.org.uk/abs/abdb/). Downloaded dataset included Non-Redundant (NR) Kabat Antibody (Light + Heavy Fragment variable (Fv)) Datasets included total of 1483 files.

Files were first screened based on the cysteine residue being found on the C-terminus of the light chain (LC):
```
  1. FAB_Two_filters_final_whole_folder_automated.py
```
This information was extracted from the SEQRES region of the LC, once the condition was met the chain labels and the file name were identified followed by download of the full FAB antibody file from the https://www.rcsb.org.

Acquired files were screened again for the presence of cysteine residue on the C-terminus of the LC, this time it was checked in two separate positions; one in SEQRES region and one in ATOM list of the LC. This was performed using: 


```
  2. FAB_second_screen.py
```

### ProFit analysis

The protein fitting program called “ProFit” was downloaded (http://www.bioinf.org.uk/software/profit/). Followed by installation of BiopTools and BiopLib tools for handing of protein structures  (http://www.bioinf.org.uk/software/bioptools/index.html, http://www.bioinf.org.uk/software/bioplib/index.html).

The compatible files were then fitted against each other by selecting the first file to act as a reference followed by fitting the remaining files against that reference and generating an RMS value. Then the next file on the list was set as a reference, this was performed until all files were analysed against each other. The conditions by which the files were fitted together was set up as a ZONE. The ZONE was defined as a cysteine residue on the LC plus two amino acids prior that against cysteine residue on the HC plus the two amino acids prior that. The ZONES were listed as per ProFit requirements as well as selected atom by which the fitting should take place, here ATOM CA and then later CB, and SG.

The next script used was:
```
  3. Step_through_pdb_automated.py
```
that checked the SSBOND region in the pdb file for the presence of complete Fab disulfide bond. 

The script is being called out from the terminal:
```
  3.1 run_script 
```
The outcome of this were files which generated RMS score that were automatically saved as:
```
RMSDs.txt
```
The RMSDs.txt file contained names of the two files (reference_file.pdb -mobile_file.pdb RMS: XXX) and the RMS value. 

All the fitting results from the ATOM region were saved as 
```
reference_file-mobile_file.fit.
```
That included the fitting coordinates.
 
            
From here, a script was written;
```              
  4. Matrix.py
```
that analysed the comparison between files generated in the RMSDs.txt file based on the matrix. The sum of each row was added, and the lowest representation was selected, the results were printed into
```
  Matrix_sum.txt 
```
Based on the matrix_sum results, a file with the lowest representation as well as all the files that were fitted to it were selected and moved to new folder for easier access. 

### Visualisation of the results

In order to represent and visualise the whole fitting, the results had to be categorised
The three separate codes were run through BASH script from terminal
```
  5. call_out_new_zones.sh
```

Firstly, the ZONEs of interests from the mobile files were identified again by using:
```
  5.1 get_new_zones.py
```

The nearest lysine residue to the specified ZONE residue (CYS) had to be identified by using pdbfindnearres tool with the cut of distance of 8A by using:
```
  5.2 get_min_max_from_zones.py
```
Once these seven residues from LC and seven from HC were identified, they were printed into a new .pdb file. The ZONEs and files were separated from each other by adding MODEL to the top and ENDMDL to the bottom of each file alongside the name of the file within REMARK section by using:
```
  5.3 cut_zones_from_fit_file.py
```
This generated a pdb file called
```
     results_for_VMD.pdb
```
that contained just the extracted residues from all the fitting performed earlier.


The residues which were not LYS or CYS had to be mutated into a GLY, alongside the ATOM numbers, residue numbers and chain labels as these needed to be identical between all files. 

First, the residues that were not CYS or LYS were from the results_for_VMD file were mutated to GLY using:
 
```
  6.1 res_mutation.py
```
followed by generation of new output file:
```
results_for_VMD_replaced.pdb
```

Due to the LYS being found at different location towards the CYS based on the previous analysis (get_min_max_from_zones.py), this presented an issue of splitting the files. For the VMD analysis all files must be in the same order, have the same ATOM numbers, residue numbers and chain labels as mentioned above. It was decided that the combined fit residues will be split based on the LYS location, resulting in ten different conformation:
``` 
	1. GLY GLY CYS LYS GLY CYS		= 45 files
	2. LYS GLY GLY CYS GLY GLY CYS		= 9 files
	3. LYS GLY GLY CYS LYS GLY CYS		= 5 files	
	4. LYS GLY CYS GLY GLY CYS LYS		= 1 file
	5. LYS GLY CYS GLY GLY CYS 		= 24 files
	6. GLY GLY CYS LYS GLY CYS LYS		= 5 files	
	7. LYS GLY GLY CYS LYS GLY GLY CYS	= 1 file
	8. LYS GLY CYS LYS GLY GLY CYS		= 3 files
	9. GLY GLY CYS GLY GLY CYS LYS		= 1 file
	10.LYS LYS CYS GLY GLY CYS LYS		= 1 file
``` 

This was performed by another script 
```        
  6.2 new_chain_mutation.py
```
where the files were separated to their appropriate bins and chain labels were changed to either L or H where appropriate. This generated new output files:
```
      results_for_VMD_replaced_vX.pdb
```

Lastly, the chain residue number were changed in each bin for the same number throughout by using:
```
  6.3 chain_format.py
```
The result was 10 separate pdb files, each containing GLY, LYS and CYS residues with x, y, and z coordinates from the ProFit fitting.



A new script was generated to calculate a distance of an atom of a specified residue. This was performed using :
```
  7. cal_distance_automatic.py
```
Here a user can select a specific residue from the bins generated above and find the distance between two atoms.



### Germline analysis

Germline analysis of the FAB’ antibody sequences used was performed by using XXXXX tool. This resulted in two files containing each V domains and C domains. To analyse the difference in gene segments that the files contained the distance calculation was performed using cal_distance_automatic.py. Then a new script was developed that used the distance information and the gene segment for each light and heavy chain of the Fab fragment: 
```
Germline_analysis.py
```

### Graphs
```
  8. histogram_final.py
```
and
```
  9 new_matrix_dendrogram.py
```








