
import numpy as np
from numpy.random import choice 
import random 

'''
       Implementation of Ant Colony Algorithm.
       Returns Minimum path taken by ants to travel between 
       specified start and destination covering all intermediate nodes.
       
       Contains methods: 
            - To generate paths, initialize ants.
            - Pick the next city to visit based on the pheromone level.    
            - Calculate total distances between the paths.
            - Spread pheromone on selected edges.
            - Evaporate pheromones on all edges.
       
       Arguments to be provided:
            distance matrix : numpy.array conatining the distances between each edge.
            ants : Total number of ants to be run in every iteration
            best_ant : number of ants that should spread pheromone.
            decay_rate : rate at which the pheromone should decay.
            alpha : weights on the pheromones
            beta : weights on the distances       
'''
class ACO():
    #Initialization
    def __init__(self, distance_matrix, ants, best_ant, decay_rate, alpha, beta):
        self.distances  = distance_matrix
        self.pheromone = np.ones(self.distances.shape) / len(distance_matrix)
        self.all_nodes = range(len(distance_matrix))
        self.ants_count = ants
        self.best_ant = best_ant
        self.decay_rate = decay_rate
        self.alpha = alpha
        self.beta = beta

    #Main logic that runs the code
    def run(self,s = 0,t = 0):
        paths = self.generate_paths(s,t)           
        return paths

    #Generate Paths given (s,t).
    def generate_paths(self,s,t):
        total_paths = []
        for i in range(self.ants_count):
            path = self.generate_path(s,t)
            total_paths.append((path, self.total_path_dist(path)))
        return total_paths

    #Generate Individual Paths.
    def generate_path(self, start, end):
        path = []
        visited = set()
        visited.add(start)
        prev = start
        for i in range(len(self.distances) - 1):
            next_city = self.next_city(self.pheromone[prev], self.distances[prev], visited)
            path.append((prev, next_city))
            prev = next_city
            visited.add(next_city)
        path.append((prev, end)) # going to end point    
        return path

    #Method to spread pheromones among the given edges.
    def spread_pheronome(self, paths, best_ant):
        sorted_paths = sorted(paths, key=lambda x: x[1])
        for path, dist in sorted_paths[:best_ant]:
            for next_move in path:
                self.pheromone[next_move] += 1.0 / self.distances[next_move]
    
    #Evaporate pheromones by multiplying with the decay rate.
    def evaporate_phermone(self):
        self.pheromone * self.decay_rate

    #Calculates the total distance covered
    def total_path_dist(self, path):
        total_distance = 0
        for pth in path:
            total_distance += self.distances[pth]
        return total_distance
    
    #Picks the next city based on the probablity.
    def next_city(self, pheromone, dist, visited):
        pheromone = np.copy(pheromone)
        pheromone[list(visited)] = 0
        for i1 in range(len(dist)):
            if dist[i1] == int(0):
                dist[i1] = 1 
        row = pheromone ** self.alpha * ((1/ dist) ** self.beta)
        try:
         norm_row = row / row.sum() 
         next_city = choice(self.all_nodes, 1,p=norm_row)[0]
        except:
         next_city = choice(self.all_nodes, 1)[0]
        return next_city

#END#