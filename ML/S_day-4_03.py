



a,b = list(map(int,input().split(" ")))
n= int(input())
p=a/b
print(round(p* (1-p)**(n-1), 3))


#Bob is a high school basketball player. He is a 70%
#free throw shooter, meaning his probability of making a free
#throw is 0.70 . What is the probability that Bob makes his first free
# throw on his fifth shot?

# n=5, p=0.7, q= 0.3, so g(n,p) = p*q^(n-1)