def sum_of_min_max(array):
    maxi=-float('inf')
    mini=float('inf')
    for i in array:
        if maxi<i:
            maxi=i
        elif mini>i:
            mini=i
    
    return maxi+mini

array=list(map(int,input().split()))
print(sum_of_min_max(array))