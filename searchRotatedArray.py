class Solution:
    # @param A, a list of integers
    # @param target, an integer to be searched
    # @return an integer
    def search(self, A, target):
        start,end = 0,len(A)-1
        while start + 1 < end:
            mid = start + (end-start)/2
            if A[mid] == target:
                return mid
            if A[start] < A[mid]:
                if target <= A[mid] and target >= A[start]:
                    end = mid
                else:
                    start = mid
            else:
                if A[mid] <=target and target <=A[end]:
                    start = mid
                else:
                    end = mid
        if A[start] == target:
            return start
        if A[end] == target:
            return end
        return -1

if __name__ == "__main__":
    s = Solution()
    print s.search([5,1,3],4)
    print s.search([1,3,5],5)
    print s.search([3,5,1],1)
    print s.search([3,5,1],3)
    print s.search([4,5,6,7,8,1,2,3], 8)
        
