import math
import statistics


def stdDev(arr):
    mean=round((statistics.mean(arr)),1)
    #print(mean)
    new_list=[(i-mean)**2 for i in arr]

    #print(new_list)

    result=(statistics.mean(new_list))**0.5

    print(round(result,1))

if __name__ == '__main__':
    n = int(input().strip())

    vals = list(map(int, input().rstrip().split()))

    stdDev(vals)