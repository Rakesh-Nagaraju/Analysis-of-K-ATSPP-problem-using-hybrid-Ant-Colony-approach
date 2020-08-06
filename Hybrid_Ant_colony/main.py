import numpy as np
import time
import math
from Ant_Colony_Opt import ACO
from OPT_3 import *
from Genetic_Algo import *
from File_Parse_TSP import *

'''
       Main python program to implement an hybrid algorithm that combines
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

#Path distance
def path_dist(path,distances):
        total_dist = 0
        for ele in range(len(path)-1):
            total_dist += distances[path[ele]][path[ele+1]]
        return total_dist

#Fitness evaluation
def evaluate_fitness(tour,st,distances):
        fitness_scores = []
        total_distance = 0
        for gene in range(len(tour)):
            if gene == 0:
             for idx in range(len(tour[gene])):
                if idx == len(tour[gene])-1: 
                 total_distance += distances[tour[gene][idx]][st[1]]
                else:
                 total_distance += distances[tour[gene][idx]][tour[gene][idx+1]]
            elif gene == len(tour)-1:
             for idx in range(len(tour[gene])-1):
                if (idx == 0): 
                 total_distance += distances[st[0]][tour[gene][idx]]
                else:
                 total_distance += distances[tour[gene][idx]][tour[gene][idx+1]]
            else:
             for idx in range(len(tour[gene])):
                if idx == 0: 
                 total_distance += distances[st[0]][tour[gene][idx]]
                elif idx == len(tour[gene])-1: 
                 total_distance += distances[tour[gene][idx]][st[1]]
                else:
                 total_distance += distances[tour[gene][idx]][tour[gene][idx+1]]
            fitness = total_distance 
            fitness_scores.append(fitness)
        return fitness_scores

#Main Function that contains the algorithm.
def main(distances, k_val, st, Iteration = 1000, ants = 100, decay = 0.95,alpha = 1,beta = 1):
 Iter = 0
 #Start Timer
 seconds_start = time.time()
 #Sellect best ants as all the ants
 best_ants = ants
 #Initialize the ACO Class with parameters of distance, ants, best_ants, decay_rate, alpha and Beta values.
 ant_colony = ACO(distances, ants, best_ants, decay, alpha, beta)

 #Initialize Best solution to Infinity.
 Best_known_sol = (np.inf,np.inf)

 #Begin loop until Iterations is done and best solution has a value other than infinity. - Termination Condition.
 while((Iter <= Iteration and Best_known_sol == (np.inf,np.inf)) or (Best_known_sol == (np.inf,np.inf))):
    Population = ant_colony.run(st[0],st[1])
    Inter_path = []
    Inter_path_val = []

    #Add the shortest path from ACO to a nested array and also calculate corresponding cost of tour.
    for i1 in Population:
        x,y = i1
        a = []
        for j1 in range(len(x)):
            a.append(x[j1][0])
            Inter_path.append(a)
            Inter_path_val.append(path_dist(a,distances))
    
    opt_path = []
    opt_path_val = []
    for k in Inter_path:
     if k[0] == st[0] and k[len(k)-1] == st[1]: 
      dum = path_dist(k,distances)
      h = OPT_3_Optimization(k, distances) 
      if h != None:
        opt_path.append(h)
        opt_path_val.append(path_dist(h,distances))
      else:
          opt_path.append(k)
          opt_path_val.append(path_dist(k,distances))

    #Split the path among k Salesman.
    Multi_path_tour = []
    for l in opt_path:
       if l[0] == st[0] and l[len(k)-1] == st[1]: 
        ans = (np.array_split(l, k_val))
        ans_list = []
        for array in ans:
            ans_list.append((array.tolist()))
            Multi_path_tour.append(ans_list)

    #Evaluate Fitness and calculate Sa value.
    Sa_paths = []
    Sa_paths_val = []
    for m in range(len(Multi_path_tour)):
        k2 = evaluate_fitness(Multi_path_tour[m],st,distances)
        Multi_path_tour[m][0] = list(dict.fromkeys(Multi_path_tour[m][0]))
        Sa_paths.append(Multi_path_tour[m])
        Sa_paths_val.append(sum(k2))
    try:
     Sa = (Sa_paths[Sa_paths_val.index(min(Sa_paths_val))],Sa_paths_val[Sa_paths_val.index(min(Sa_paths_val))])
     del Sa_paths[Sa_paths.index(Sa[0])]
     del Sa_paths_val[Sa_paths_val.index(Sa[1])]
    except:
        pass

    #Perform Genetic Algorithm operations on Best path.
    New_Population = []
    for m2 in range(len(Sa_paths)):
        best = Sa_paths[Sa_paths_val.index(min(Sa_paths_val))]
        New_Population.append(inverse(best))
        New_Population.append(swap(best))
        New_Population.append(slide(best))
        New_Population.append(cross_over(best))
        New_Population.append(swap_cross_over(best))
        New_Population.append(inverse_cross_over(best))
        New_Population.append(slide_cross_over(best))
        New_Population.append(best)

    #Calculate Sb by finding the fitness scores among the new generated chromosomes.
    Sb_paths = []
    Sb_paths_val= []
    for i in range(len(New_Population)):
        k2 = evaluate_fitness(New_Population[i],st,distances)
        Sb_paths.append(New_Population[i])
        Sb_paths_val.append(sum(k2))
    try:
     Sb = (Sb_paths[Sb_paths_val.index(min(Sb_paths_val))],Sb_paths_val[Sb_paths_val.index(min(Sb_paths_val))]) 
    except:
        pass

    #Evaporate pheromones from all edges.
    ant_colony.evaporate_phermone()

    #Compare Sa and Sb to evaluate the best path and spread pheromones only on those paths.
    try:
     if Sa[1] < Sb[1]:
      if (Sa[0][0][0] == st[0]) and (Sa[0][len(Sa[0])-1][-1]) == st[1]:
        #Get only the best edges.
        d = []
        for i in Sa[0]:
            d.extend(i)
        d1 = []
        for i in range(0,len(d)-1,1):
            d1.append((d[i],d[i+1]))
        
        #Allocate the edges to Sa.
        Sa_best_edges = [(d1,Sa[1])]

        #Spread pheromones and assign the current best solution.
        ant_colony.spread_pheronome(Sa_best_edges,1)
        Curr_best_solution = Sa
     else:
      if (Sb[0][0][0] == st[0]) and (Sb[0][len(Sb[0])-1][-1]) == st[1]:
        #Get only the best edges.
        d = []
        for i in Sb[0]:
            d.extend(i)
        d1 = []
        for i in range(0,len(d)-1,1):
            d1.append((d[i],d[i+1]))

        #Allocate the edges to Sb.
        Sb_best_edges = [(d1,Sb[1])]

        #Spread pheromones and assign the current best solution.
        ant_colony.spread_pheronome(Sb_best_edges,1)
        Curr_best_solution = Sb

     #Check if the current solution is better than best known solution.
     if Curr_best_solution[1] < Best_known_sol[1]:
        Best_known_sol = Curr_best_solution
        #Get only the best edges.
        d = []
        for i in Best_known_sol[0]:
            d.extend(i)
        d1 = []
        for i in range(0,len(d)-1,1):
            d1.append((d[i],d[i+1]))

        #Allocate the edges to Best known solution edges.
        Best_known_sol_edges = [(d1,Best_known_sol[1])]
        #Spread pheromones
        ant_colony.spread_pheronome(Best_known_sol_edges,1)
    except:
        pass
    Iter += 1
 #Format and Print the Output. 
 seconds_end = time.time()
 time_elapsed = seconds_end - seconds_start
 print("Best_Solution :",Best_known_sol)
 print("Elapsed time : ",time_elapsed)

#Create a interative Menu for the User to select the input file and define the Parameters required
#and finally call the program.
if __name__ == '__main__':
 choice = True
 while(choice):
    Choice = int(input("Enter '0' to continue, '3' to Exit : ")) 
    if Choice == 0: 
     Filename = input("Enter filename : ")
     distances = parse_file_before_exec(Filename)
     k = int(input("Enter k (Salesman): "))
     ch = input("Want to specify end points? Y/N : ")
     if ch == 'Y':
      S = int(input("Enter the start-point : "))
      T = int(input("Enter the end-point : "))
      S_T = (S,T)
     else:
         #Generate Random start and end-points if not specified.
         S,T = random.sample(range(len(distances)),2)
         S_T = (S,T)
         print("Selected (s,t) is : ",S_T)
     num = int(input("Enter '1' to run with default parameters or '2' for setting the parameters : "))
     if num == 1:
         main(distances, k, S_T)
         print("For values given File :",Filename," k = ",k," start-end points = ",S_T,"\n")
     else:
        Iterations = int(input("Enter the number of Iterations : "))
        ants = int(input("Enter number of ants for ACO : "))
        decay = float(input("Enter decay rate : "))
        alpha = int(input("Enter alpha value : "))
        beta = int(input("Enter beta value : "))
        print("\n")
        main(distances, k, S_T, Iterations, ants, decay, alpha, beta)
        print("[For values given File :",Filename," k = ",k," start-end points = ",S_T,",")
        print("Iterations :",Iterations," Ants count = ",ants," Decay = ",decay,"Alpha",alpha,"Beta",beta,"]\n")
    else:
        #If choice = 3 exit the Menu.
        choice = False
#END#