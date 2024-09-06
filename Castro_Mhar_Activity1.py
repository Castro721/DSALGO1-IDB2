
def InsertionSortAscend(arr1):
    for i in range(1, len(arr1)):
        key = arr1[i]
        j = i - 1
        while j >= 0 and key < arr1[j]:
            arr1[j + 1] = arr1[j]
            j -= 1
        arr1[j + 1] = key


def InsertionSortDescend(arr1):
    for i in range(1, len(arr1)):
        key = arr1[i]
        j = i - 1
        while j >= 0 and key > arr1[j]:
            arr1[j + 1] = arr1[j]
            j -= 1
        arr1[j + 1] = key


def SelectionSortAscend(arr2):
    for i in range(len(arr2)):
        min_idx = i
        for j in range(i + 1, len(arr2)):
            if arr2[min_idx] > arr2[j]:
                min_idx = j
        arr2[i], arr2[min_idx] = arr2[min_idx], arr2[i]


def SelectionSortDescend(arr2):
    for i in range(len(arr2)):
        min_idx = i
        for j in range(i + 1, len(arr2)):
            if arr2[min_idx] < arr2[j]:
                min_idx = j
        arr2[i], arr2[min_idx] = arr2[min_idx], arr2[i]


def BubbleSortAscend(arr3):
    for i in range(len(arr3)):
        for j in range(0, len(arr3) - i - 1):
            if arr3[j] > arr3[j + 1]:
                arr3[j], arr3[j + 1] = arr3[j + 1], arr3[j]


def BubbleSortDescend(arr3):
    for i in range(len(arr3)):
        for j in range(0, len(arr3) - i - 1):
            if arr3[j] < arr3[j + 1]:
                arr3[j], arr3[j + 1] = arr3[j + 1], arr3[j]


def OddNumbers(my_list):
    listOdd = []
    for num in my_list:
        if num % 2 != 0:
            listOdd.append(num)
    return listOdd



def EvenNumbers(my_list):
    listEven = []
    for num in my_list:
        if num % 2 == 0:
            listEven.append(num)
    return listEven

'''
arr1 = [10, 2, 3, 1, 1, 4, 89, 21]
print("Array 1 before Insertion sort")
print(arr1)
InsertionSort(arr1)
print("This is after the insertion sort")
print(arr1)


#Selection sort
arr2 = [10, 2, 3, 1, 1, 4, 89, 21]
print("Array 2 before Selection sort")
print(arr2)
SelectionSort(arr2)
print("Array 2 after Selection sort")
print(arr2)


#Bubble sort
arr3 = [10, 2, 3, 1, 1, 4, 89, 21]
print("Array 3 before Bubble sort sort")
print(arr3)
BubbleSort(arr3)
print("Array 3 after Bubble sort")
print(arr3)
'''

#1.
list1 = [23, 89, 7, 56, 44]
print("This is List 1 Before Bubble Sort")
print(list1)
BubbleSortAscend(list1)
print("This is List 1 in Ascending Order After Bubble Sort")
print(list1)
print()

#2.
list2 = [12, 78, 91, 34, 62]
print("This is List 2 Before Insertion Sort")
print(list2)
InsertionSortAscend(list2)
print("This is List 2 in Ascending Order After Insertion Sort")
print(list2)
print()

#3.
list3 = [5, 99, 48, 15, 67]
print("This is List 3 Before Selection Sort")
print(list3)
SelectionSortDescend(list3)
print("This is List 3 in Descending Order After Selection Sort")
print(list3)
print()

#4.
list4 = [38, 82, 25, 74, 13]
print("This is List 4 Before Insertion Sort")
print(list4)
InsertionSortDescend(list4)
print("This is List 4 in Descending Order After Insertion Sort")
print(list4)
print()

#5.
list5 = [44, 56, 62, 78, 48, 15, 38, 25]
print("This is List 5 Before Insertion Sort")
print(list5)
InsertionSortDescend(list5)
list6 = list5
print("This is List 6 in Descending Order After Insertion Sort")
print(list6)
InsertionSortAscend(list5)
list7 = list5
print("This is List 7 in Ascending Order After Insertion Sort")
print(list7)
print()

#6.
list8 = [23, 89, 7, 56, 44, 12, 78, 91, 34, 62, 5, 99, 48, 15, 67, 38, 82, 25, 74, 13]
print("This is List 8 Before Selection Sort")
print(list8)
SelectionSortAscend(list8)
print("This is List 8 in Ascending Order After Selection Sort")
print(list8)
print()

#7.
list1Odd = OddNumbers(list8)
print("This is odd values in List 8")
print(list1Odd)
list2Even = EvenNumbers(list8)
print("This is Even values in list 8")
print(list2Even)