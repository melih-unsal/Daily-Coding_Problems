"""
PROBLEM 333 MEDIUM
This problem was asked by Pinterest.
At a party, there is a single person who everyone knows, but who does not know anyone in return (the "celebrity").
To help figure out who this is, you have access to an O(1) method called knows(a, b), which returns True if person a knows person b, else False.
Given a list of N people and the above operation, find a way to identify the celebrity in O(N) time.
"""
import numpy as np
n=4
relationships=np.array([[1,1,0,0,],[0,1,0,0],[0,1,1,1],[1,1,1,0]])
def knows(a,b):
    assert a<n and b<n,"Undefined person id"
    return relationships[a,b]    
    
def find_celebrity():
    candidate_celebrity=0
    while candidate_celebrity < n:
        index=candidate_celebrity+1
        while index <n and not knows(candidate_celebrity,index):
            index +=1
        if index <n:
            candidate_celebrity =index
        else:
            break
    for i in range(n):
        if knows(candidate_celebrity,i) and i!=candidate_celebrity:
            return -1
        if not knows(i,candidate_celebrity):
            return -1
    return candidate_celebrity
print(find_celebrity())
    
        