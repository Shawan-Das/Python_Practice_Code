import statistics
n=int(input())

x=list(map(int,input().strip().split()))[:n]

print(statistics.mean(x))
print(statistics.median(x))
list= sorted(x)
print(statistics.mode(list))