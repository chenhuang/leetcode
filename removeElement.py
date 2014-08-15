#!/usr/bin/env python

'''
Remove Element 

Given an array and a value, remove all instances of that value in place and return the new length.

The order of elements can be changed. It doesn't matter what you leave beyond the new length.

https://oj.leetcode.com/problems/remove-element/

'''

class Solution:
    # @param    A       a list of integers
    # @param    elem    an integer, value need to be removed
    # @return an integer
    # Idea:
    # two pointer: i = 0 and j = len(A)-1, i travel from 0 to j-1
    # if A[i] == elem, swap A[i] with A[j], j -= 1
    def removeElement(self, A, elem):
        if len(A) == 0: return 0
        i = 0
        j = len(A)-1
        while i != j:
            if A[i] == elem:
                A[i] = A[j]
                A[j] = elem
                j -= 1
            else:
                i += 1
        if A[j] == elem:
            j -= 1
        return j+1                

