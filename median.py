#! /usr/bin/env python
# Find a median from a list of numbers, using two heaps
# There are two parts:
# 1. maintain a balanced heap tree
# Here we assume that the right tree is equal with the left tree, or is 1 element larger than that of left tree.
# 2. extract k numbers from the tree

import os
import sys
import re
import heapq

class solution: 
    def __init__(self):
        self.minHeap = []
        self.maxHeap = []

    def addElement(self, num):
        if len(self.minHeap) == 0:
            heapq.heappush(self.minHeap, num)
        else:
            minHeapTop = heapq.nsmallest(1,self.minHeap)[0]
            if len(heapq.nlargest(1,self.maxHeap)) == 0:
                heapq.heappush(self.maxHeap, min(num,minHeapTop))
                heapq.heappushpop(self.minHeap, max(num,minHeapTop))
            else:
                maxHeapTop = heapq.nlargest(1,self.maxHeap)[0]

                if num > minHeapTop:
                    tmp = minHeapTop
                    minHeapTop = num
                    num = tmp
                elif num < maxHeapTop:
                    tmp = maxHeapTop
                    maxHeapTop = num
                    num = tmp
                
                heapq.heappushpop(self.minHeap, minHeapTop)
                heapq._heappushpop_max(self.maxHeap, maxHeapTop)
                
                if len(self.minHeap) - len(self.maxHeap) > 0:
                    heapq.heappush(self.maxHeap,num)
                else:
                    heapq.heappush(self.minHeap,num)

    def getElement(self, k):
        result = []

        left = heapq.nlargest(k/2, self.maxHeap)
        right = []

        if k%2 == 0:
            right = heapq.nsmallest(k/2, self.minHeap)
        else:
            right = heapq.nsmallest(k/2+1, self.minHeap)

        if left is not None:
            result.extend(left)
        if right is not None:
            result.extend(right)

        print self.maxHeap, self.minHeap, result

        return result


    def findMedian(self, array, k):
        for i in array:
            self.addElement(i)
            print self.getElement(k)

import heapq
class medianWithHeap:
    class minHeap:
        def __init__(self):
            self.vals = []
        def put(self, n):
            heapq.heappush(self.vals, n)
        def get(self):
            if self.vals > 0:
                return heapq.heappop(self.vals)
            else:
                return None
        def size(self):
            return len(self.vals)

    class maxHeap:
        def __init__(self):
            self.vals = []
        def put(self, n):
            heapq.heappush(self.vals, -n)
        def get(self):
            if self.vals > 0:
                return -heapq.heappop(self.vals)
            else:
                return None
        def size(self):
            return len(self.vals)


    def __init__(self):
        self.minHeap = medianWithHeap.minHeap()
        self.maxHeap = medianWithHeap.maxHeap()

    def add(self, n):
        # Initialize the heaps
        if self.minHeap.size() == 0:
            self.minHeap.put(n)
            return 
        if self.maxHeap.size() == 0:
            self.maxHeap.put(n)
            return 

        # get lower half max
        left_max = self.maxHeap.get()
        right_min = self.minHeap.get()
        
        # swap if necessary
        if n < left_max:
            tmp = left_max
            left_max = n
            n = tmp
        elif n > right_min:
            tmp = right_min
            right_min = n
            n = tmp
            
        # update heap
        self.maxHeap.put(left_max)
        self.minHeap.put(right_min)

        if self.minHeap.size() > self.maxHeap.size():
            self.maxHeap.put(n)
        else:
            self.minHeap.put(n)

    def getMedian(self):
        if self.minHeap.size() == self.maxHeap.size():
            left_max = self.maxHeap.get()
            right_min = self.minHeap.get()

            return float((left_max+right_min)/2)
        else:
            return self.minHeap.get()

if __name__ == "__main__":
    s = medianWithHeap()
    for i in [10, 9 ,7, 3, 1]:
        s.add(i)
    
    print s.getMedian()

