import random
import math

class cluster():
    def __init__(self):
        self.clusterObservations = []

    import random
import math

class Cluster():
    def __init__(self):
        self.cluster_obs = []

    def get_observation(self):
        return self.cluster_obs

    def add_observation(self, observation):
        self.cluster_obs.append(observation)

    def remove_observation(self, observation_location):
        self.cluster_obs.remove(observation_location)

    def calculate_centroid(self, k):
        centroid = []
        centroid_counter = 0
        counter = 0
        max_value = 0
        while counter < len(self.cluster_obs):
            if ((counter + 1 == len(self.cluster_obs)) and (centroid_counter < k)):
                max_value = float(max_value + self.cluster_obs[counter][centroid_counter])
                counter += 1
                centroid.append(round(float(max_value / counter), 4))
                counter = 0
                centroid_counter += 1
                max_value = 0
            elif ((counter + 1 == len(self.cluster_obs) and (centroid_counter == k))):
                max_value = float(max_value + self.cluster_obs[counter][centroid_counter])
                counter += 1
                centroid.append(round(float(max_value / counter), 4))
                break
            else:
                max_value = float(max_value + self.cluster_obs[counter][centroid_counter])
                counter += 1

        return centroid

    def print_cluster(self):
        return self.cluster_obs

    def get_dimensions(self):
        return len(self.cluster_obs)

class ClusterManager():
    def __init__(self, observations, k):
        self.observations = observations
        self.k = k
        self.clusters = []
        self.centroids = []

    def random_kmeans_initialization(self):
        for counter in range(self.k):
            self.clusters.append(Cluster())

        for counter in range(len(self.observations)):
            self.clusters[random.randrange(self.k)].add_observation(self.observations[counter])

    def get_clusters(self):
        return self.clusters

    def assignment_kmeans(self):
        done = True
        for counter in range(len(self.clusters)):
            current_obs = self.clusters[counter].get_observation()
            dynamic_counter = 0
            dynamic_length = len(current_obs)
            while dynamic_counter < dynamic_length:
                for x in range(len(self.clusters)):
                    euclidean_distance = self.calculate_euclidean_observation_to_cluster(current_obs[dynamic_counter], self.clusters[x].calculate_centroid(self.k))
                    if (x == 0):
                        closest = euclidean_distance
                        closest_cluster_index = x
                        observation_index = dynamic_counter
                    else:
                        if (closest > euclidean_distance):
                            closest = euclidean_distance
                            closest_cluster_index = x
                            observation_index = dynamic_counter
                if (closest_cluster_index != counter):
                    self.clusters[closest_cluster_index].add_observation(current_obs[observation_index])
                    self.clusters[counter].remove_observation(current_obs[observation_index])
                    done = False
                    current_obs = self.clusters[counter].get_observation()
                    dynamic_length = len(current_obs)
                    dynamic_counter -= 1

                dynamic_counter += 1

        return done

    def find_nearest_cluster(self, observation, cluster_index):
        closest_cluster_index = 0
        current_closest_cluster = 0
        clustering_map = []
        for counter in range(len(observation)):
            current_closest_cluster = 0
            for j in range(len(self.clusters)):
                if (current_closest_cluster == 0):
                    current_closest_cluster = (self.calculate_euclidean_observation_to_cluster(observation[counter], self.clusters[j].calculate_centroid(self.k)))
                    observation_index = counter
                else:
                    temp = (self.calculate_euclidean_observation_to_cluster(observation[counter], self.clusters[j].calculate_centroid(self.k)))
                    if (current_closest_cluster > temp):
                        closest_cluster_index = j
                        observation_index = counter

            if (closest_cluster_index != cluster_index):
                self.clusters[closest_cluster_index].add_observation(observation[observation_index])
                self.clusters[cluster_index].remove_observation(observation[observation_index])
                clustering_map.append(observation_index)

        cluster_remover = len(clustering_map) - 1
        while cluster_remover > 0:
            self.clusters[cluster_index].remove_observation(observation[clustering_map[cluster_remover]])
            cluster_remover 

import random
import math

class Cluster():
    def __init__(self):
        self.cluster_obs = []

    def get_observation(self):
        return self.cluster_obs

    def add_observation(self, observation):
        self.cluster_obs.append(observation)

    def remove_observation(self, observation_location):
        self.cluster_obs.remove(observation_location)

    def calculate_centroid(self, k):
        centroid = []
        centroid_counter = 0
        counter = 0
        max_value = 0
        while counter < len(self.cluster_obs):
            if ((counter + 1 == len(self.cluster_obs)) and (centroid_counter < k)):
                max_value = float(max_value + self.cluster_obs[counter][centroid_counter])
                counter += 1
                centroid.append(round(float(max_value / counter), 4))
                counter = 0
                centroid_counter += 1
                max_value = 0
            elif ((counter + 1 == len(self.cluster_obs) and (centroid_counter == k))):
                max_value = float(max_value + self.cluster_obs[counter][centroid_counter])
                counter += 1
                centroid.append(round(float(max_value / counter), 4))
                break
            else:
                max_value = float(max_value + self.cluster_obs[counter][centroid_counter])
                counter += 1

        return centroid

    def print_cluster(self):
        return self.cluster_obs

    def get_dimensions(self):
        return len(self.cluster_obs)

class ClusterManager():
    def __init__(self, observations, k):
        self.observations = observations
        self.k = k
        self.clusters = []
        self.centroids = []

    def random_kmeans_initialization(self):
        for counter in range(self.k):
            self.clusters.append(Cluster())

        for counter in range(len(self.observations)):
            self.clusters[random.randrange(self.k)].add_observation(self.observations[counter])

    def get_clusters(self):
        return self.clusters

    def assignment_kmeans(self):
        done = True
        for counter in range(len(self.clusters)):
            current_obs = self.clusters[counter].get_observation()
            dynamic_counter = 0
            dynamic_length = len(current_obs)
            while dynamic_counter < dynamic_length:
                for x in range(len(self.clusters)):
                    euclidean_distance = self.calculate_euclidean_observation_to_cluster(current_obs[dynamic_counter], self.clusters[x].calculate_centroid(self.k))
                    if (x == 0):
                        closest = euclidean_distance
                        closest_cluster_index = x
                        observation_index = dynamic_counter
                    else:
                        if (closest > euclidean_distance):
                            closest = euclidean_distance
                            closest_cluster_index = x
                            observation_index = dynamic_counter
                if (closest_cluster_index != counter):
                    self.clusters[closest_cluster_index].add_observation(current_obs[observation_index])
                    self.clusters[counter].remove_observation(current_obs[observation_index])
                    done = False
                    current_obs = self.clusters[counter].get_observation()
                    dynamic_length = len(current_obs)
                    dynamic_counter -= 1

                dynamic_counter += 1

        return done

    def find_nearest_cluster(self, observation, cluster_index):
        closest_cluster_index = 0
        current_closest_cluster = 0
        clustering_map = []
        for counter in range(len(observation)):
            current_closest_cluster = 0
            for j in range(len(self.clusters)):
                if (current_closest_cluster == 0):
                    current_closest_cluster = (self.calculate_euclidean_observation_to_cluster(observation[counter], self.clusters[j].calculate_centroid(self.k)))
                    observation_index = counter
                else:
                    temp = (self.calculate_euclidean_observation_to_cluster(observation[counter], self.clusters[j].calculate_centroid(self.k)))
                    if (current_closest_cluster > temp):
                        closest_cluster_index = j
                        observation_index = counter

            if (closest_cluster_index != cluster_index):
                self.clusters[closest_cluster_index].add_observation(observation[observation_index])
                self.clusters[cluster_index].remove_observation(observation[observation_index])
                clustering_map.append(observation_index)

        cluster_remover = len(clustering_map) - 1
        while cluster_remover > 0:
            self.clusters[cluster_index].remove_observation(observation[clustering_map[cluster_remover]])
            cluster_remover -= 1

    def print_clusters(self):
        files = open("testfile.txt", "w")
        for counter in range(len(self.clusters)):
            files.write("Cluster Number = " + str(counter) + "\n")
            files.write(str(self.clusters[counter].print_cluster()) + "\n")
        files.close()