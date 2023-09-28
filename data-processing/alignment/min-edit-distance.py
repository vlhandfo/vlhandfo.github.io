"""J&M, CH2, Task # 2.6 Implement a minimum edit distance algorithm"""

import numpy as np

def min_edit_dist(source: str, target: str, sub_cost:int=2, 
                  del_cost:int=1, ins_cost:int=1) -> int:
    """Calculate the minimum edit distance between a source string and a target 
    string.
    
    Parameters:
		source (str): The source string.
        target (str): The target string.
        sub_cost (int): The cost of substitution; default is 2
        del_cost (int): The cost of deletion; default is 1
        ins_cost (int): The cost of insertion; default is 1
        
    Returns:
		med (int): the minimum edit distance between the source and target 
        	strings
    
    Detailed Explanation:
	The minimum edit distance between two strings is the minimum number of 
    operations (insertions, deletions, or substitutions) required to transform 
    the source string into the target string. This function utilizes the dynamic
    programming approach to	solve the problem efficiently.
    """
    operations = ["delete", "insert", "substitute"]
    n = len(source)
    m = len(target)

	# Create a distance matrix
    d = np.zeros((m+1, n+1), dtype=int) 

    # Create backpointer
    backpointers = [{op:None for op in operations}
                            for i in range(m + 1)]
    
	# Initialization: first row and column is coming from an empty string
    for row in range(m + 1):
        d[row,0] = row
        
    for col in range(n + 1):
        d[0, col] = col
        

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            sub_cost_tmp = sub_cost
            if source[i-1] == target[j-1]:
                sub_cost_tmp = 0
       
            # min_edit = min(costs)
            # d[i, j] = min_edit
            # backpointers[i][costs[min_edit]] = costs[min_edit]
   
    med = d[m,n]
    
    return med, d

min_edit_dist("duck", "dock")