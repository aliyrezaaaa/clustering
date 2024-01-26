import numpy as np
import csv
from scipy.cluster.vq import kmeans2
from Clustering import Cluster
from CsvController import CsvController
from Clustering import ClusterManager

file_name = "iris.csv"
k = 3

csv_file = CsvController(file_name)
csv_titles, csv_data = csv_file.read_csv()
extracted_column = csv_file.extract_column(csv_data, 4)
csv_data = csv_file.delete_column(csv_data, 4)
csv_data = csv_file.convert_to_float(csv_data)

clustering = ClusterManager(csv_data, k)
clustering.random_kmeans_initialization()
done = False

while not done:
    clustering.random_kmeans_update()
    done = clustering.assignment_kmeans()

clusters = clustering.get_clusters()
print(clusters[1].get_observation())

# res, idx = kmeans2(np.array(csv_data), k)
#
# for cluster in range(0, k):
#     print("Cluster number", str(cluster + 1))
#     for i in range(0, len(idx)):
#         if idx[i] == cluster:
#             print(str(csv_data[i]), ",", extracted_column[cluster])