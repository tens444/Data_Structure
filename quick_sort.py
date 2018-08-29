def quick_sort(L, begin, end):
    if begin < end:
        pivot = partition(L, begin, end)
        quick_sort(L, begin, pivot)
        quick_sort(L, pivot+1, end)
    return L

def partition(L, begin, end):
    pivot = begin
    value = L[pivot]
    left = pivot + 1
    right = end - 1

    while True:
        while left <= right and L[left] < value:
            left += 1
        while left <= right and value < L[right]:
            right -= 1
        if left > right:
            break
        else:
            L[left], L[right] = L[right], L[left]
    
    L[pivot], L[right] = L[right], L[pivot]
    return right

if __name__ == "__main__":
    L = [4,2,5,3,1,8,20,31,24,35,6]
    print(quick_sort(L, 0, len(L)))