"""
PROBLEM 331 MEDIUM
This problem was asked by LinkedIn.
You are given a string consisting of the letters x and y, such as xyxxxyxyy.
In addition, you have an operation called flip, which changes a single x to y or vice versa.
Determine how many times you would need to apply this operation to ensure that all x's come before all y's.
In the preceding example, it suffices to flip the second and sixth characters, so you should return 2.

"""

word="xyxxxyxyy"

def getNumOfNeededFlips(word):
    #count the number of xs first
    x=0
    for char in word:
        if char=='x':
            x+=1
            
    """
    initially result equals to x1+...xn when we put y1 it turns out to be y1+x2+x3+...xn when we put y2 it becomes y1+y2+x4+x5+...+xn
    so if we decrease it by x1 when we put yi we actually adding yi-x(i+1)
    """
    min_total=x
    index=0
    
    while index<len(word) and word[index]=='x':
            min_total-=1
            index+=1
    
    running_sum=min_total
    while index<len(word):
        while index<len(word) and word[index]=='y':
            running_sum+=1
            index+=1
            
        while index<len(word) and word[index]=='x':
            running_sum-=1
            index+=1
        if running_sum < min_total:
            min_total=running_sum
    return min_total

print(getNumOfNeededFlips(word))        
        
        