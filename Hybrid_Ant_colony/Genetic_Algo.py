import random

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

#Function to check the validity of the chromosomes in a tour
def check_validity(tour):
  for i in range(len(tour)):
    tour[i] = list(dict.fromkeys(tour[i]))
  return tour

#Inverse/Flip mutation
def inverse(tour):
  for i in range(len(tour)):
     if i == 0:
       if len(tour[i]) > 2:
        f1, f2 = random.sample(range(1,len(tour[i])),2)  
        tour[i][tour[i][f1]:tour[i][f2]] = tour[i][tour[i][f1]:tour[i][f2]][::-1]
       else:
         break
     elif i == len(tour)-1:
       if len(tour[i]) > 2:
        f1, f2 = random.sample(range(0,len(tour[i])-1),2)
        tour[i][tour[i][f1]:tour[i][f2]] = tour[i][tour[i][f1]:tour[i][f2]][::-1]  
       else:
         break
     else:
        if len(tour[i])> 2:
         f1, f2 = random.sample(range(len(tour[i])),2)
         tour[i][tour[i][f1]:tour[i][f2]] = tour[i][tour[i][f1]:tour[i][f2]][::-1]  
        else:
           break
  return(check_validity(tour))

#Swap mutation
def swap(tour):
  for i in range(len(tour)):
     if i == 0:
       if len(tour[i]) > 2:
        f1, f2 = random.sample(range(1,len(tour[i])),2) 
        tour[i][f1], tour[i][f2] = tour[i][f2], tour[i][f1] 
       else:
         break
     elif i == len(tour)-1:
       if len(tour[i]) > 2:
        f1, f2 = random.sample(range(0,len(tour[i])-1),2) 
        tour[i][f1], tour[i][f2] = tour[i][f2], tour[i][f1] 
       else:
         break
     else:
        if len(tour[i]) > 2:
         f1, f2 = random.sample(range(len(tour[i])),2) 
         tour[i][f1], tour[i][f2] = tour[i][f2], tour[i][f1] 
        else:
          break
  return(check_validity(tour))

#Slide mutation
def slide(tour):
  for i in range(len(tour)):
     if i == 0:
       if len(tour[i]) > 2:
        f1, f2 = random.sample(range(1,len(tour[i])),2) 
        tour[i].insert(f2, tour[i].pop(f1)) 
       else:
         break
     elif i == len(tour)-1:
       if len(tour[i]) > 2:
        f1, f2 = random.sample(range(0,len(tour[i])-1),2) 
        tour[i].insert(f2, tour[i].pop(f1)) 
       else:
         break
     else:
        if len(tour[i]) > 2:
         f1, f2 = random.sample(range(len(tour[i])),2) 
         tour[i].insert(f2, tour[i].pop(f1))
        else: 
          break
  return(check_validity(tour))

#One-point Crossover
def cross_over(tour):
  for i in range(0,len(tour)-1,2):
    if i == 0:
     if len(tour[i]) > 2:
      f1 = random.randrange(1,len(tour[i]))
      if i+1 != len(tour)-1:
       if len(tour[i+1]) > 0:
        f2 = random.randrange(len(tour[i+1])) 
        tour[i][f1], tour[i+1][f2] = tour[i+1][f2], tour[i][f1]
       else:
         break
      else:
        if len(tour[i+1]) > 2:
         f2 = random.randrange(len(tour[i+1])-1)
         tour[i][f1], tour[i+1][f2] = tour[i+1][f2], tour[i][f1]
        else:
          break   
     else:
        break
    elif i == len(tour)-2:
      if len(tour[i]) > 0:
       f1 = random.randrange(len(tour[i]))
      else:
        break
      if len(tour[i+1]) > 2:
         f2 = random.randrange(len(tour[i+1])-1)
         tour[i][f1], tour[i+1][f2] = tour[i+1][f2], tour[i][f1]
      else:
        break
    else:
      if len(tour[i]) > 0:
       f1 = random.randrange(len(tour[i]))  
      else: 
        break
      if len(tour[i+1])> 0:
       f2 = random.randrange(len(tour[i+1]))
       tour[i][f1], tour[i+1][f2] = tour[i+1][f2], tour[i][f1]
      else:
        break  
  return(check_validity(tour))

#Inverse and Crossover
def inverse_cross_over(tour):
  for i in range(0,len(tour)-1,2):
      if i == 0:
       if len(tour[i]) > 2:
        f1, f2 = random.sample(range(1,len(tour[i])),2)
        k = tour[i][tour[i][f1]:tour[i][f2]][::-1]
       else:
        break
       if i+1 == len(tour)-2:
        if len(tour[i+1]) > 2: 
         f3, f4 = random.sample(range(len(tour[i+1])-1),2)
         k1 = tour[i+1][tour[i+1][f3]:tour[i+1][f4]][::-1]
         del tour[i][tour[i][f1]:tour[i][f2]]
         del tour[i+1][tour[i+1][f3]:tour[i+1][f4]]
         tour[i].extend(k1)
         tour[i+1].extend(k)
        else:
           break 
      elif i == len(tour)-2:
         if len(tour[i]) > 2:
          f1, f2 = random.sample(range(len(tour[i])),2)  
          k = tour[i][tour[i][f1]:tour[i][f2]][::-1]
         else:
          break
         if len(tour[i+1]) > 2:
          f3, f4 = random.sample(range(len(tour[i+1])-1),2)  
          k1 = tour[i+1][tour[i+1][f3]:tour[i+1][f4]][::-1]
          del tour[i][tour[i][f1]:tour[i][f2]]
          del tour[i+1][tour[i+1][f3]:tour[i+1][f4]]
          tour[i].extend(k1)
          tour[i+1].extend(k)
         else:
          break 
      else:
         if len(tour[i]) > 2:
          f1, f2 = random.sample(range(len(tour[i])),2) 
          k = tour[i][tour[i][f1]:tour[i][f2]][::-1] 
         else:
           break
         if len(tour[i+1]) > 2:
          f3, f4 = random.sample(range(len(tour[i+1])),2)  
          k1 = tour[i+1][tour[i+1][f3]:tour[i+1][f4]][::-1]
          del tour[i][tour[i][f1]:tour[i][f2]]
          del tour[i+1][tour[i+1][f3]:tour[i+1][f4]]
          tour[i].extend(k1)
          tour[i+1].extend(k)
         else:
           break 
  return(check_validity(tour))

#Swap and Crossover
def swap_cross_over(tour):
  for i in range(0,len(tour)-1,2):
      if i == 0:
       if len(tour[i]) > 2:
        f1, f2 = random.sample(range(1,len(tour[i])),2)
       else:
        break
       if len(tour[i+1]) > 2: 
         f3, f4 = random.sample(range(len(tour[i+1])-1),2)
         tour[i][f1], tour[i][f2] = tour[i][f2], tour[i][f1]
         tour[i+1][f3], tour[i+1][f4] = tour[i+1][f3], tour[i+1][f4]
         tour[i][f1], tour[i+1][f3] = tour[i+1][f3], tour[i][f1]
         tour[i][f2], tour[i+1][f4] = tour[i+1][f4], tour[i][f2]
       else:
           break
      elif i == len(tour)-2:
         if len(tour[i]) > 2:
          f1, f2 = random.sample(range(len(tour[i])),2)  
         else:
           break
         if len(tour[i+1]) > 2:
          f3, f4 = random.sample(range(len(tour[i+1])-1),2)  
          tour[i][f1], tour[i][f2] = tour[i][f2], tour[i][f1]
          tour[i+1][f3], tour[i+1][f4] = tour[i+1][f3], tour[i+1][f4]
          tour[i][f1], tour[i+1][f3] = tour[i+1][f3], tour[i][f1]
          tour[i][f2], tour[i+1][f4] = tour[i+1][f4], tour[i][f2] 
         else:
          break 
      else:
         if len(tour[i]) > 2:
          f1, f2 = random.sample(range(len(tour[i])),2)  
          tour[i][f1], tour[i][f2] = tour[i][f2], tour[i][f1]
         else:
           break
         if len(tour[i+1]) > 2:
          f3, f4 = random.sample(range(len(tour[i+1])),2)  
          tour[i+1][f3], tour[i+1][f4] = tour[i+1][f3], tour[i+1][f4]
          tour[i][f1], tour[i+1][f3] = tour[i+1][f3], tour[i][f1]
          tour[i][f2], tour[i+1][f4] = tour[i+1][f4], tour[i][f2]
         else:
           break 
  return(check_validity(tour))

#Slide and Crossover
def slide_cross_over(tour):
  for i in range(0,len(tour)-1,2):
      if i == 0:
       if len(tour[i]) > 2:
        f1, f2 = random.sample(range(1,len(tour[i])),2)
        tour[i].insert(f2, tour[i].pop(f1))
        k = tour[i][tour[i][f1]:tour[i][f2]]
       else:
        break
       if i+1 == len(tour)-2:
        if len(tour[i+1]) > 2: 
         f3, f4 = random.sample(range(len(tour[i+1])-1),2)
         tour[i+1].insert(f4, tour[i+1].pop(f3))
         k1 = tour[i+1][tour[i+1][f3]:tour[i+1][f4]]     
         del tour[i][tour[i][f1]:tour[i][f2]]
         del tour[i+1][tour[i+1][f3]:tour[i+1][f4]]
         tour[i].extend(k1)
         tour[i+1].extend(k)
        else:
           break 
      elif i == len(tour)-2:
         if len(tour[i]) > 2:
           f1, f2 = random.sample(range(len(tour[i])-1),2)
           tour[i].insert(f2, tour[i].pop(f1))
           k = tour[i][tour[i][f1]:tour[i][f2]]
         else:
           break
         if len(tour[i+1]) > 2:
          f3, f4 = random.sample(range(len(tour[i+1])-1),2)  
          tour[i+1].insert(f4, tour[i+1].pop(f3))
          k1 = tour[i+1][tour[i+1][f3]:tour[i+1][f4]]     
          del tour[i][tour[i][f1]:tour[i][f2]]
          del tour[i+1][tour[i+1][f3]:tour[i+1][f4]]
          tour[i].extend(k1)
          tour[i+1].extend(k)
         else:
          break 
      else:
         if len(tour[i]) > 2:
          f1, f2 = random.sample(range(len(tour[i])),2)  
          tour[i].insert(f2, tour[i].pop(f1))
          k = tour[i][tour[i][f1]:tour[i][f2]]
         else: 
          break
         if len(tour[i+1]) > 2:
          f3, f4 = random.sample(range(len(tour[i+1])-1),2)  
          tour[i+1].insert(f4, tour[i+1].pop(f3))
          k1 = tour[i+1][tour[i+1][f3]:tour[i+1][f4]]      
          del tour[i][tour[i][f1]:tour[i][f2]]
          del tour[i+1][tour[i+1][f3]:tour[i+1][f4]]
          tour[i].extend(k1)
          tour[i+1].extend(k)
         else: 
           break 
  return(check_validity(tour))
#END#
