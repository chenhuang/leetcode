'''
Pascal's Triangle 

Given numRows, generate the first numRows of Pascal's triangle.

For example, given numRows = 5,
Return

[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]

https://oj.leetcode.com/problems/pascals-triangle/
'''

'''
Pascal's Triangle II Given an index k, return the kth row of the Pascal's triangle.

For example, given k = 3,
Return [1,3,3,1].

Note:
Could you optimize your algorithm to use only O(k) extra space?

https://oj.leetcode.com/problems/pascals-triangle-ii/
'''

class Solution:
    # @return a list of lists of integers
    def generate(self, numRows):
        if numRows == 0: return []
        result = [[1]]
        
        for i in range(2,numRows+1):    
            result.append([1,1])
            while len(result[-1]) < i:
                for j in range(len(result[-2])-1):
                    result[-1].insert(1,result[-2][j]+result[-2][j+1])
        return result

    def getRow_II(self, rowIndex):
        inter_result = [0 for i in range(rowIndex+1)]
        result = [0 for i in range(rowIndex+1)]

        result[0] = 1
        for i in range(rowIndex+1):
            if i == 1:
                result[1] = 1
            inter_result[0]=1
            inter_result[i]=1
            for j in range(1,i):
                inter_result[j] = result[j-1]+result[j]
            tmp = result
            result = inter_result
            inter_result = tmp
        
        return result

if __name__ == "__main__":
    s = Solution()
    #print s.generate(5)
    print s.getRow_II(4)
                
            
