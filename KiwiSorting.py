import matplotlib.pyplot as plt
from time import time 
from random import randint, random

def Start():
    arr = [randint(1,1000000) for _ in range(10)]

    while True:
        sortby = input("Which sorting algorithm do you want to use?\n1 - Bubble\n2 - Selection\n3 - Insertion\n")
        
        plt.plot(arr)
        plt.ylabel('Unsorted array')
        plt.show()

        if sortby == "1":
            Bubble(arr)
            break
        elif sortby == "2":
            Selection(arr)
            break
        elif sortby == "3":
            Insertion(arr)
            break
        else: 
            print("Incorrect input!")


#Bubble sort
def Bubble(arr):
    sort = "bubble"

    n = len(arr)
    swapped = False
    for i in range(n-1):
        for j in range(0, n-i-1):
            if arr[j] > arr[j + 1]:
                swapped = True
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
        if not swapped:
            return
    
    #return(arr)
    finish(arr,sort)

#Selection sort
def Selection(arr):
    sort = "selection"

    for i in range(len(arr)):
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[min_idx] > arr[j]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    
    #return(arr)
    finish(arr,sort)
    

#Insertion sort
def Insertion(arr):
    sort = "insertion"

    swapped = False
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >=0 and key < arr[j] :
                arr[j+1] = arr[j]
                j -= 1
        arr[j+1] = key
    
    #return(arr)
    finish(arr,sort)

def finish(arr,sort):

    print("List sorted using " + sort + " sort:\n")
    print(arr)

    plt.plot(arr)
    plt.ylabel('Sorted Array')
    plt.show()

Start()