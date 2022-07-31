from random import randint, random
from KiwiSorting import Bubble
from KiwiSorting import Selection
from KiwiSorting import Insertion
from time import time

averagecase = [randint(1,1000000) for _ in range(5000)]
bestcase = sorted(averagecase)
worstcase = sorted(averagecase, reverse = True)

def Start():
    while True:
        sortby = input("Which sorting algorithm do you want to test?\n1 - Bubble\n2 - Selection\n3 - Insertion\n")
        
        if sortby == "1":
            bubbleTest()
            break
        elif sortby == "2":
            SelectionTest()
            break
        elif sortby == "3":
            InsertionTest()
            break
        else: 
            print("Incorrect input!")


def bubbleTest():

    print("Bubble test:\n")

    def test_BubbleWorst():
        start = time()
        assert Bubble(worstcase) == bestcase
        print("Worst case:")
        print(time() - start)

        test_BubbleBest()

    def test_BubbleBest():
        start = time()
        Bubble(bestcase)
        print("Best case:")
        print(time() - start)

        test_BubbleAvg()

    def test_BubbleAvg():
        start = time()
        assert Bubble(averagecase) == bestcase
        print("Average case:")
        print(time() - start)

    test_BubbleWorst()

def SelectionTest():

    print("Selection test:\n")

    def test_SelectionWorst():
        start = time()
        assert Selection(worstcase) == bestcase
        print("Worst case:")
        print(time() - start)

        test_SelectionBest()

    def test_SelectionBest():
        start = time()
        Selection(bestcase)
        print("Best case:")
        print(time() - start)

        test_SelectionAvg()

    def test_SelectionAvg():
        start = time()
        assert Selection(averagecase) == bestcase
        print("Average case:")
        print(time() - start)
        
    test_SelectionWorst()

def InsertionTest():
    
    print("Insertion test:\n")

    def test_InsertionWorst():
        start = time()
        assert Insertion(worstcase) == bestcase
        print("Worst case:")
        print(time() - start)

        test_InsertionBest()

    def test_InsertionBest():
        start = time()
        Insertion(bestcase)
        print("Best case:")
        print(time() - start)

        test_InsertionAvg()

    def test_InsertionAvg():
        start = time()
        assert Insertion(averagecase) == bestcase
        print("Average case:")
        print(time() - start)
        
    test_InsertionWorst()

#Start()