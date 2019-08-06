# Project Title

Proximity of lysine to light chain terminal of the disulfide bridge in Fab region of antibody

## Flow of the project:

Initial antibody .pdb files were first downloaded from the AbDB: Antibody Structure Database (http://www.bioinf.org.uk/abs/abdb/ downloaded on 13 May 2019). Downloaded dataset included Non-Redundant (NR) Kabat Antibody (Light + Heavy Fragment variable (Fv)) Datasets included total of 1483 files.

Files were first screened based on the cysteine residue being found on the C-terminus of the light chain (LC):
```
  1. FAB_Two_filters_final_whole_folder_automated.py
```
This information was extracted from the SEQRES region of the LC, once the condition was met the chain labels and the file name were identified followed by download of the full FAB antibody file from the https://www.rcsb.org.

Acquired files were screened again for the presence of cysteine residue on the C-terminus of the LC, this time it was checked in two separate positions; one in SEQRES region and one in ATOM list of the LC. This was performed using: 

```
  2. FAB_second_screen.py
```


Meanwhile, a protein fitting program called “ProFit” was downloaded (http://www.bioinf.org.uk/software/profit/). Followed by installation of BiopTools and BiopLib tools for handing of protein structures  (http://www.bioinf.org.uk/software/bioptools/index.html, http://www.bioinf.org.uk/software/bioplib/index.html.

The compatible files were then fitted against each other by selecting the first file to act as a reference followed by fitting the remaining files against that reference and generating an RMS value. Then the next file on the list was set as a reference, this was performed until all files were analysed against each other. The conditions by which the files were fitted together was set up as a ZONE. The ZONE was defined as a cysteine residue on the LC plus two amino acids prior that against cysteine residue on the HC plus the two amino acids prior that. The ZONES were listed as per ProFit requirements as well as selected atom by which the fitting should take place, here ATOM CA and then later CB, and SG.
```
  3. Step_through_pdb_automated.py
```
checked the SSBOND region in the pdb file for the presence of complete Fab disulfide bond. This resulted in 165 of compatible files

Furthermore, the script is being called out by a BASH script from the terminal:
```
  3.1 run_script 
```
Files which generated RMS score were automatically  saved as:
```
RMSDs.txt
```
which contained names of the two files (reference_file.pdb -mobile_file.pdb RMS: XXX) and the RMS value. 

Furthermore, all the fitting results from the ATOM region were saved as 
```
reference_file-mobile_file.fit.
```
Root Mean Square Deviation (RMSD) is a measure of a difference between two structures.
 
            
              
  4. Matrix.py
            -> matrix.txt
  5. call_out_new_zones.sh
  5.1 get_new_zones.py
  5.2 get_min_max_from_zones.py
  5.3 cut_zones_from_fit_file.py
            -> results_for_VMD.pdb
  6. Mutation
  6.1 res_mutation.py
            -> results_for_VMD_replaced.pdb
  6.2 new_chain_mutation.py
            -> results_for_VMD_replaced_vX.pdb
  6.3 chain_format.py
  7. val_distance_automatic.py
  8. histogram_final.py
  9 new_matrix_dendrogram.py