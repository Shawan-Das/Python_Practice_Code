#Poison distribution
#Condition:
# 1. The outcome of each trial is either success or failure
# 2. The average number of successes (lemda) that occurs in a specified region is known.
# 3. The probability that a success will occur is ptoportional to the size of the region.
# 4. The probability that a success will occur in an extremely small region is virtually zero.

# EQN:  P(k,L) = L^k * e^-L  /k!
#Where:
#    e=2.71828
#    L is the average number of successes that occur in a specified region.
#    k is the actual number of successes that occur in a specified region
#    P(k,L) is the Poisson probability, which is the probability, which is the
#         probability of getting exactly K successes when the average number of successes is L


from math import factorial as fact

e= 2.71828
L= float(input())
k= int(input())

p= ((L**k)*(e**(-L)))/fact(k)

print(round(p,3))