def LinearSearch(n, arr, ele):
    flag = 0
    for i in range(len(arr)):
        if (arr[i] == ele):
            return i+1
    return -1

n = int(input())
arr = list(map(int,input().split()))
ele = int(input())
print("Element Found at : ", LinearSearch(n, arr,ele))
# I/O Format
# -1 means element was not found
"""
5
4 5 3 6 7
6
Element Found at :  4
"""
