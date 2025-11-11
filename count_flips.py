import random 

n = 1_000_000

numTails = 0
numHeads = 0
for i in range(n):
  value = random.randint(0,1)
  if(value ==0):
    numTails +=1
else:
    numHeads +=1
  

print("Number of Heads:", numHeads,"({0:f})".format(numHeads/n) )
print("Number of Tails", numTails, "({0:f})".format(numTails/n))
print("Number of Trials:" numHeads + numTails)
