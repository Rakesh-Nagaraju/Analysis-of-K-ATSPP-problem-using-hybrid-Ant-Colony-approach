import numpy as np
import time

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

def OPT_3_Optimization(path, distance_matrix):
    while True:
        k_time = time.time()
        alpha = 0
        for i in range(1,len(path)-1):
         for j in range(i + 2, len(path)-1):
          for k in range(j + 2, len(path)-1 + (i > 0)):
            alpha += reverse_edges(distance_matrix, path, i, j, k)
        k_n_time = time.time()
        z_time = k_n_time - k_time
        if alpha >= 0 or z_time > 150:
            break
        return path

# Function reverse_edge
def reverse_edges(distance_matrix, path, l, m, n):
    dist_1 = distance_matrix[path[l-1]][path[l]] + distance_matrix[path[m-1]][path[m]] + distance_matrix[path[n-1]][path[n % len(path)]]
    dist_2 = distance_matrix[path[l-1]][path[m-1]] + distance_matrix[path[l]][path[m]] + distance_matrix[path[n-1]][path[n % len(path)]]
    dist_3 = distance_matrix[path[l-1]][path[l]] + distance_matrix[path[m-1]][path[n-1]] + distance_matrix[path[m]][path[n % len(path)]]
    dist_4 = distance_matrix[path[l-1]][path[m]] + distance_matrix[path[n-1]][path[l]] + distance_matrix[path[m-1]][path[n % len(path)]]
    dist_5 = distance_matrix[path[n % len(path)]][path[l]] + distance_matrix[path[m-1]][path[m]] + distance_matrix[path[n-1]][path[l-1]]
    if dist_1 > dist_2:
            path[l:m] = reversed(path[l:m])
            res = dist_2 - dist_1
            return res
    elif dist_1 > dist_2:
            path[m:n] = reversed(path[m:n])
            res = dist_2 - dist_1
            return res
    elif dist_1 > dist_5:
            path[l:n] = reversed(path[l:n])
            res = dist_5 - dist_1
            return res
    elif dist_1 > dist_4:
            tmp = path[m:n] + path[l:m]
            path[l:n] = tmp
            res = dist_4 - dist_1 
            return res
    return 0
#END#



