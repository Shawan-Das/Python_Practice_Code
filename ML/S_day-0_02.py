# def weightedMean(X, W):
#     n = len(X)
#     list = [X[i] * W[i] for i in range(n)]
#     print(round((sum(list)/sum(W)),1))
#
#
#
# if __name__ == '__main__':
#     n = int(input().strip())
#
#     vals = list(map(int, input().rstrip().split()))
#
#     weights = list(map(int, input().rstrip().split()))
#
#     weightedMean(vals, weights)
import statistics

list=[3,5,7,8]
print(statistics.median(list))