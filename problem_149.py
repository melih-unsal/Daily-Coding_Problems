"""
PROBLEM 149 HARD
This problem was asked by Goldman Sachs.

Given a list of numbers L, implement a method sum(i, j) which returns the sum from the sublist L[i:j] (including i, excluding j).

For example, given L = [1, 2, 3, 4, 5], sum(1, 3) should return sum([2, 3]), which is 5.

You can assume that you can do some pre-processing. sum() should be optimized over the pre-processing step.
"""
def preprocess(arr):
    total=0
    modified=[0]*len(arr)
    total=0
    for i in range(len(arr)):
        modified[i] = arr[i]+total
        total=modified[i]
    return modified
    
def sum(i,j):
    assert i<j and i>0 and j>0 and i<len(arr) and j<len(arr),"invalid interval "
    print(preprocessed_arr[j-1]-preprocessed_arr[i-1])
    
arr=[1,2,3,4,5]
preprocessed_arr=preprocess(arr)
sum(1,3)
    
    
