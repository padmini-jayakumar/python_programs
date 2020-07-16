

n = int(input())
arr=map(int, input().split())
arr = list(arr)
arr.sort(reverse=True)
arr=list(dict.fromkeys(arr))
print(arr[1])
