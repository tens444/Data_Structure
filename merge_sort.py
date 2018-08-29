L = [4,2,5,3,1,8,20,31,24,35,6]

def merge_sort(L):
    if len(L) <= 1:
        return L
    else:
        mid = int(len(L)/2)
        left = merge_sort(L[:mid])
        right = merge_sort(L[mid:])
        return merge(left, right)
    
def merge(left, right):
    length_a = len(left)
    length_b = len(right)
    a = b = 0
    merged_list = list()
    while a < length_a and b < length_b:
        if left[a] < right[b]:
            merged_list.append(left[a])
            a += 1
        else:
            merged_list.append(right[b])
            b += 1
    while a < length_a:
        merged_list.append(left[a])
        a += 1
    while b < length_b:
        merged_list.append(right[b])
        b += 1
    return merged_list

print(merge_sort(L))

