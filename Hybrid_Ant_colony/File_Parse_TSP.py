import numpy as np
import pandas as pd
import re
res = []
res1 = []

def parse_file_before_exec(filename):
    inputFile = open(filename, "r") 
    res_final = []

    for line in inputFile:
     if line[0] == 'D':
        val = int(line.split(":")[1])
     if not re.match('^[a-zA-Z]',line[0]):
        line = line.lstrip()
        new_line = re.sub(' +', ' ',line)
        d = new_line.split(" ")
        for i in range(0,len(d)):     
            k = 0
            res1.append(int(d[i]))
    #print(len(res1))
    inputFile.close()
    ans = np.array_split(res1, val)
    return(np.array(ans))
#parse_file_before_exec("fasym7.txt")