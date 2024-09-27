def InsertionSort(X):
    for i in range(1, len(X)):
        key=X[i]
        j=i-1
        while j >= 0 and key > X[j]:
            X[j+1] = X[j]
            j-=1
        X[j+1]=key


def SelectionSort(X):
    for i in range(len(X)):
        min_index = i
        for j in range(i+1, len(X)):
            if X[min_index] > X[j]:
                min_index = j
        X[i], X[min_index] = X[min_index], X[i]


X = [1, 2, 21, 33, 45, 65, 12]
TempList = [1, 2, 21, 33, 45, 65, 12]
InsertionSort(X)
print(X)
X.clear()
for i in range(0, len(TempList)):
    X.append(TempList.pop(0))
SelectionSort(X)
print(X)

