from itertools import combinations

n=input()

s=list(input().split(' '))

k=int(input())

count=0

for i in combinations(s,k):
    if 'a' in i:
        count+=1
    
    
probability = count/len(list(combinations(s,k)))
print(probability)
