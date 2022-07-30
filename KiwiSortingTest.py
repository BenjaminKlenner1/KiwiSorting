from random import randint, random
from KiwiSorting import Bubble
from time import time

averagecase = [randint(1,10000) for _ in range(1000)]
bestcase = sorted(averagecase)
worstcase = sorted(averagecase, reverse = True)

def test_BubbleWorst():
    start = time()
    assert Bubble(worstcase) == bestcase
    print(time() - start)

def test_BubbleBest():
    start = time()
    assert Bubble(bestcase) == bestcase
    print(time() - start)

def test_BubbleAvg():
    start = time()
    assert Bubble(averagecase) == bestcase
    print(time() - start)