import random 

n = 5

numTails = 0
numHeads = 0
for i in range(n):
  value = random.randint(0,1)
  if(value ==0):
    numTails +=1
else:
    numHeads +=1
  

print("Number of Heads:", numHeads)
print("Number of Tails", numTails)
print("Number of Trials:" numHeads + numTails)
