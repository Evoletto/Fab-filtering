#*************************************************************************
#
#   Program:    new_matrix
#   File:      	new_matrix.py
#   
#   Version:    V1.0
#   Date:       27.06.19
#   Function:   Runs through the RMSDs.txt result file. 
#		 		Generates matrix and based on that produces figures.
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
import numpy as np
import matplotlib.pyplot as plt
import plotly
from scipy.cluster.hierarchy import dendrogram, linkage  
from matplotlib import pyplot as plt

rmsd_file_path = "/Volumes/ALINASD/PhD_Rotations/Comp/Graphs_Figures/RMSDs_4.txt" 
#rmsd_file_path = "/Volumes/ALINASD/PhD_Rotations/Comp/Graphs/RMSDs_3L5X_1_against_all.txt"
#rmsd_file_path = sys.argv[1]
#sys.stdout = open("/Volumes/ALINASD/PhD_Rotations/Comp/Graphs/Matrix_sum.txt", "w")
#sys.stdout = open(sys.argv[2], "w")

rmsd_file = open(rmsd_file_path)
file_contents = rmsd_file.readlines()
matrix = []
current_file = ""
for line in file_contents:
	# get first file name
	delimiter = line.find("-")
	first_filename = line[:delimiter].replace(".pdb", "")
	# get rms value
	rms_value = float(line[line.find("RMS:") + len("RMS:"):])
	# create array with those values
	if current_file == "":
		current_file = first_filename
		matrix.append([rms_value])
		
	elif current_file == first_filename:
		matrix[-1].append(rms_value)
	else: 
		#new row
		matrix.append([rms_value])
		
	current_file = first_filename
	
X = np.array(matrix)
print(X)

 #Hierarchal Clustering plot
labels = range(1, 165)  
plt.figure(figsize=(10, 7))  
plt.subplots_adjust(bottom=0.1)  
plt.scatter(X[:,0],X[:,1], label='True Position')
#plt.title('Hierarchical Clustering Dendrogram (truncated)')
plt.xlabel('sample index')
plt.ylabel('distance')

for label, x, y in zip(labels, X[:, 0], X[:, 1]):  
    plt.annotate(
        label,
        xy=(x, y), xytext=(-3, 3),
        textcoords='offset points', ha='right', va='bottom')
plt.show()

Z = linkage(X, 'ward')


# Dendrogram plot
# #calculate full dendrogram
# plt.figure(figsize=(25, 10))
# plt.title('Hierarchical Clustering Dendrogram')
# plt.xlabel('sample index')
# plt.ylabel('distance')
# dendrogram(
#     Z,
#     leaf_rotation=90.,  # rotates the x axis labels
#     leaf_font_size=8.,  # font size for the x axis labels
# )
# plt.show()

# 
# # Dendrogram Truncation plot
# plt.title('Hierarchical Clustering Dendrogram (truncated)')
# plt.xlabel('sample index')
# plt.ylabel('distance')
# dendrogram(
#     Z,
#     truncate_mode='lastp',  # show only the last p merged clusters
#     p=12,  # show only the last p merged clusters
#     #show_leaf_counts=False,  # otherwise numbers in brackets are counts
#     leaf_rotation=90.,
#     leaf_font_size=12.,
#     show_contracted=True,  # to get a distribution impression in truncated branches
# )
# plt.show()


# Fancy Dendrogram
# def fancy_dendrogram(*args, **kwargs):
#     max_d = kwargs.pop('max_d', None)
#     if max_d and 'color_threshold' not in kwargs:
#         kwargs['color_threshold'] = max_d
#     annotate_above = kwargs.pop('annotate_above', 0)
# 
#     ddata = dendrogram(*args, **kwargs)
# 
#     if not kwargs.get('no_plot', False):
#         plt.title('Hierarchical Clustering Dendrogram (truncated)')
#         plt.xlabel('sample index or (cluster size)')
#         plt.ylabel('distance')
#         for i, d, c in zip(ddata['icoord'], ddata['dcoord'], ddata['color_list']):
#             x = 0.5 * sum(i[1:3])
#             y = d[1]
#             if y > annotate_above:
#                 plt.plot(x, y, 'o', c=c)
#                 plt.annotate("%.3g" % y, (x, y), xytext=(0, -5),
#                              textcoords='offset points',
#                              va='top', ha='center')
#         if max_d:
#             plt.axhline(y=max_d, c='k')
#     return ddata
#     
# fancy_dendrogram(
#     Z,
#     truncate_mode='lastp',
#     p=12,
#     leaf_rotation=90.,
#     leaf_font_size=12.,
#     show_contracted=True,
#     annotate_above=10,  # useful in small plots so annotations don't overlap
# )
# plt.show()
# 


# Cut off Dendrogram

# set cut-off to 50
# max_d = 50  # max_d as in max_distance
# fancy_dendrogram(
#     Z,
#     truncate_mode='lastp',
#     p=12,
#     leaf_rotation=90.,
#     leaf_font_size=12.,
#     show_contracted=True,
#     annotate_above=10,
#     max_d=max_d,  # plot a horizontal cut-off line
# )
# plt.show()
