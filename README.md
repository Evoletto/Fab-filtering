Flow of the project
  1. FAB_Two_filters_final_whole_folder_automated.py
  2. FAB_second_screen.py
  3. Step_through_pdb_automated.py
  3.1 run_script 
              -> .fit files
              -> RMSDs.txt
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