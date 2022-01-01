import statistics


def qur(arr):
    n=len(arr)
    arr=sorted(arr)
    data=[]

    if n%2==0:
        list1=arr[0:n//2]
        list2=arr[n//2:n+1]
        data.append(int(statistics.median(list1)))
        data.append(int(statistics.median(arr)))
        data.append(int(statistics.median(list2)))
    else:
        list1=arr[0:n//2]
        data.append(int(statistics.median(list1)))
        data.append(arr[n//2])
        list2=arr[(n//2)+1: n+1]
        data.append(int(statistics.median(list2)))

    return data


if __name__ =='__main__':
    x=[3,7,8,5,12,14,21,13,18]
    data= qur(x)
    print(data)

