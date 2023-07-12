lst = list(map(int,input().split()))
def count_lesserElements(lst):
    maxEle = min(lst)
    for ele in lst:
        if ele > maxEle:
            maxEle = ele
    c = 0
    for ele in lst:
        if ele == maxEle:
            c += 1
    return len(lst) - c

print(count_lesserElements([5, 5, 3]))
print(count_lesserElements([3, 1, 2]))
print(count_lesserElements(lst))
