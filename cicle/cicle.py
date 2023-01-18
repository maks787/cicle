from math import *
from random import *
##1
#n = int(input("sisestage arv vahemikus 1 kuni 9: "))

#if n < 1 or n > 9:
#    raise ValueError("Value Error")

#for i in range(n):
#    print("  ^---^  ", end="")
#print()
#for i in range(n):
#    print(" ( o o ) ", end="")
#print()
#for i in range(n):
#    print("  ! = !/", end="")
#print()
#for i in range(n):
#    print("  ^---^  ", end="")
#print()

###2
#kraadi = int(input("Enter the exponent: "))
#n = int(input("Enter the number: "))

#for i in range(1, n+1):
#    print(i ** kraadi)

###3
#import random
#num_opilane = random.randint(10, 30)
#print ("õpilaste arv:", num_opilane)
#hinnangud = [random.randint(1, 10) for _ in range(num_opilane)]
#min_hinne = min(hinnangud)
#max_hinne = max(hinnangud)
#print("Minimum hinne:", min_hinne)
#print("maximum hinne:", max_hinne)

##4
#amööbide_arv = 1
#for tundi in range(3, 25, 3):
#    amööbide_arv = 2**(tundi/3)
#    print(tundi, ":", amööbide_arv)
###5
import random
pannide_arv = 0
M=random.randint(1,10)
print("pannide arv", M)
K=random.randint(1,10)
print("kotlettide arv", K)
if M>K:
    M,K = K,M
while K > 0:
    K -= M
    pannide_arv +=1
    print("Number of pans:", pannide_arv)
    print("M:",M)
    print("K:",K)