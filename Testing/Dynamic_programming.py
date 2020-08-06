import itertools
import random
import time
import sys
from File_Parse_TSP import *


'''
Dynamic progrmming Implementation by Carl Ekerot

Currently modified to suit the Asymmetric graph and also handle Multiple salesman
while randomly choosing the points (s,t) for the testing purpose of 
"Analysis of k-ATSPP using modified ACO approach" project

Reference : https://github.com/CarlEkerot/held-karp/blob/master/held-karp.py
'''

#Calculate the total cost of the paths.
def path_dist(tour,st,distances):
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
        return fitness

#Dynamic programming solution (Held-Karp algorithm)
def DP_Solution(distances,k_val):
    n = len(distances)
    C = {}
    for k in range(1, n):
        C[(1 << k, k)] = (distances[0][k], 0)

    for size in range(2, n):
        for sub in itertools.combinations(range(1, n), size):
            num_bits = 0
            for bit in sub:
                num_bits |= 1 << bit
            for k in sub:
                prev = num_bits & ~(1 << k)
                res = []
                for m in sub:
                    if m == 0 or m == k:
                        continue
                    res.append((C[(prev, m)][0] + distances[m][k], m))
                C[(num_bits, k)] = min(res)

    
    num_bits = (2**n - 1) - 1
    res = []
    for k in range(1, n):
        res.append((C[(num_bits, k)][0] + distances[k][0], k))
    opt, prev = min(res)

    # Find the full path by backtracking
    path = []
    for i in range(n - 1):
        path.append(prev)
        new_bits = num_bits & ~(1 << prev)
        _, prev = C[(num_bits, prev)]
        num_bits = new_bits

    # Add starting and end points
    path.append(0)
    total_path = list(reversed(path))
    ans = (np.array_split(total_path, k_val))
    ans1 = []
    for array in ans:
        ans1.append((array.tolist()))
    for arr in range(len(ans1)):
        if arr == 0:
            s = ans1[arr][0]
        if arr == len(ans1) -1:
            t = ans1[arr][len(ans1[arr])-1]
    S_T = (s,t)
    dist = path_dist(ans1, S_T, distances)
    return dist, ans1, S_T

if __name__ == '__main__':
    k_val = int(input("Enter the Number of salesman : "))
    #Start Timer
    k = time.time()
    #Parse file to generate distance Matrix
    distances = parse_file_before_exec("fasym7.txt")
    #Call the dp function to generate cost, k-paths and also the chosen (s,t) points
    cost, path, ST = DP_Solution(distances,k_val)
    #End Timer
    k1 = time.time()
    #Print out the results 
    print("Best Solution : ", (path, cost))
    print("Elapsed time : ",k1-k) 
    print("\nFor the values chosen (s,t) = ",ST," and k = ",k_val)
#END#