# Analysis-of-K-ATSPP-problem-using-hybrid-Ant-Colony-approach
Also uses 3-OPT and Genetic Algorithm
Contains : 3 folders: Dataset, Acutal implementation and Testing code.



Folder: Hybrid_Ant_Colony
1.) main.py
'''
       Python program to implement an hybrid algorithm that combines
       ACO, 3-OPT and Genetic Algorithm.
       This algorithm is designed to solve the k-ATSPP problem also generalized as
       Asymmetric Multiple Travelling Salesman Problem

       
       Contains methods: 
            - To find the total distance of a single tour .
            - Fitness Evaluation to evaluate the total distance within the full tour among k-paths.    
            - Main function that contains the complete logic for the algorithm.
       
       Note: 
        - No Arguments to be provided. Directly run the code and perform actions as directed
          by the Menu in the Code.     
        - Incase of crash or failure or any abrupt scenario, kindly run the code from beginning.
        - Incase of futher queries, please contact the author Rakesh Nagaraju at : rakesh.nagaraju@sjsu.edu or rakenju@gmail.com
''' 
2.) Ant_Colony_Opt.py
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
3.) Genetic_Algo.py
'''
       Implementation of Multi-Chromosome Genetic Algorithm (GA).
       Returns 8 different tours after performing 7 different Mutation and Crossover operations. 
       Mutation includes : Swap, Inverse/Flip, Slide
       Crossover includes: One-point crossover, Swap crossover, Inverse/Flip crossover, Slide crossover.
       
       Contains methods: 
            - To generate paths, initialize ants.
            - Pick the next city to visit based on the pheromone level.    
            - Calculate total distances between the paths.
            - Spread pheromone on selected edges.
            - Evaporate pheromones on all edges.
       
       Arguments to be provided:
            tour: the tour on which GA operations are to be performed.      
'''

4.) OPT_3.py
'''
       Implementation of 3-OPT Optimization.
       Randomly chooses 3, 3 edges and interchanges them. 
       If total tour is better, then keep the tour else disregard. 
       
       Contains methods: 
            - Three_OPT which is the main function in this program.
            - reverse_edge which interchanges the edges and checks 
              if the to new tour is optimal or not. 
       
       Arguments to be provided:
            distance_matrix: distance matrix    
            path: the tour or path that is to be optimized.     
'''

4.)File_Parse_TSP.py
'''
Contains code to parser a TSPLIB file before applying the Optimization techniques.
'''

Folder: Testing 
We have an algorithm to compare with our implementation
Dynamic_Programming.py
'''
Dynamic progrmming Implementation by Carl Ekerot

Currently modified to suit the Asymmetric graph and also handle Multiple salesman
while randomly choosing the points (s,t) for the testing purpose of 
"Analysis of k-ATSPP using modified ACO approach" project
'''
