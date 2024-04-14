def find_max(a, n):
    if n == 1:
        return a[0]
    return max(a[n-1], find_max(a, n-1))
n = int(input())
a = [int(input()) for i in range(n)]
print("Maximum element in the array is", find_max(a, n))
