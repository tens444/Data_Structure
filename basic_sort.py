L = [4,2,5,3,1,8,20,31,24,35,6]

def bubble_sort(L):
    for i in range(len(L)):
        for j in range(len(L) - i - 1):
            if L[j] > L[j+1]:
                L[j], L[j+1] = L[j+1], L[j]
    return L

def select_sort(L):
    for i in range(len(L)):
        min = i
        for j in range(i, len(L)):
            if L[min] > L[j]:
                min = j
        if i != min:
            L[min], L[i] = L[i], L[min]
    return L

def insert_sort(L):
    for i in range(1, len(L)):
        temp = L[i]
        pos = i
        while pos > 0 Lnd temp < L[pos - 1]:
            L[pos] = L[pos - 1]
            pos -= 1
        L[pos] = temp
    return L