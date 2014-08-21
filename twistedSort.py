#! /usr/bin/env python

'''
Sort an array such that a1 >= a2 <= a3 >= a4 ...
'''

class Solution:
    def twistedSort(self,A):
        stack = []
        stack.append(A[0])

        for i in range(1,len(A)):
            num = stack[-1]
            if i%2 == 1:
                if num <= A[i]:
                    stack.append(A[i])
                else:
                    stack.pop()
                    stack.append(A[i])
                    stack.append(num)
            else:
                if num >= A[i]:
                    stack.append(A[i])
                else:
                    stack.pop()
                    stack.append(A[i])
                    stack.append(num)

        return stack

if __name__ == "__main__":
    s = Solution()
    print s.twistedSort([3,1,2,1,4,5,6,8,10])
                
