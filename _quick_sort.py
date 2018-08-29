L = [4,2,5,3,1,8,20,31,24,35,6]

def quick_sort(L):
    if len(L) < 2:
        return L
    else:
        pivot = L[0]
        less = [i for i in L[1:] if i <= pivot]
        great = [i for i in L[1:] if i > pivot]
        return quick_sort(less) + [pivot] + quick_sort(great)

print(quick_sort(L))