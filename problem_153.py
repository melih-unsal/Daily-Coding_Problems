"""
PROBLEM 153 [HARD]
Find an efficient algorithm to find the smallest distance (measured in number of words) between any two given words in a string.
For example, given words "hello", and "world" and a text content of "dog cat hello cat dog dog hello cat world",
return 1 because there's only one word "cat" in between the two words.
""" 

word1="hello"
word2="world"
text="dog cat hello cat dog dog hello cat world"

def smallest_distance(text,s1,s2):
    words=text.split(" ")
    min_dist=len(words)
    target=""
    last_seen=-1
    for i in range(len(words)):
        word=words[i]
        if word==s1:
            if target==s1:
                dist=i-last_seen-1
                if dist <min_dist:
                    min_dist=dist
            last_seen=i
            target=s2
        elif word==s2:
            if target==s2:
                dist=i-last_seen-1
                if dist <min_dist:
                    min_dist=dist
            last_seen=i
            target=s1
    if min_dist<len(words):
        print(min_dist)
    else:
        print("Either of the words does not exist")
        
smallest_distance(text,word1,word2)
                
                
                
        
                    
                    
                    
    