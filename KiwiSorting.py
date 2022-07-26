from re import I


def Start():

    a = [6,10,7,9,1,0,11,13,100,67,34,56,12,76,45]
    n = len(a)

    print("Which sorting algorithm would you like to use?\n1 - Bubble\n2 - Selection")
    selection = input("")

    if selection == "1":
        Bubble(a,n)
    elif selection == "2":
        Selection(a,n)

def Bubble(a,n):
    x = 0
    while x < n - 1:
        i = 0
        while i < n - 1:
            if (a[i]>a[i+1]):

                temp = a[i]
                a[i] = a[i+1]
                a[i+1] = temp
        
            i = i + 1
        x = x + 1

    print(a)
    input("")

def Selection(a,n):
    i = 0

    while i < n-1:
        print("A")
        min_index = i
        j = i + 1
        
        while j < n:
            if a[j] < a[min_index]:
                min_index = j
                j = j + 1
                print("B")
        temp = a[min_index]
        a[min_index] = a[i]
        a[i] = temp
        print("C")
        i = i + 1
            
    print(a)
    input("")


Start()