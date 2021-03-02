pos = -1
def search(list,n):
    l = 0
    u = len(list) - 1
    for i in range(l,u+1):
        mid = (l + u)//2
        if(list[mid]==n):
            globals()['pos'] = mid
            return True
        else:
            if(list[mid] < n):
                l = mid + 1
            else:
                u = mid - 1
    return False
lst= list(map(int,input().split(' ')))
n = int(input())
if (search(lst,n)):
    print(n," is found at",pos)
else:
    print(n," is not found")