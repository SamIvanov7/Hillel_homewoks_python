from random import randint

myLst = []
for i in range(1, 15):
    myLst.append(randint(0, 20))

print(myLst)


def puzirSorter(a):
    k = 0
    while k < len(a) - 1:
        m = 0
        while m < len(a) - 1 - k:
            if a[m] > a[m+1]:
                a[m], a[m+1] = a[m+1], a[m]
            m += 1
        k += 1
    return a


def shakerSorter(a):
    start = 0
    end = len(a) - 1
    isChanged = True
    while isChanged:
        isChanged = False
        for i in range(start, end):
            if a[i] > a[i + 1]:
                a[i], a[i + 1] = a[i + 1], a[i]
                isChanged = True
        if not isChanged:
            break

        isChanged = False
        end = end - 1
        for i in range(start, end)[::-1]:
            if a[i] > a[i + 1]:
                a[i], a[i + 1] = a[i + 1], a[i]
                isChanged = True
        start = start + 1
    return a


print(puzirSorter(myLst))
print(shakerSorter(myLst))
