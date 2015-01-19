class Solution:
    def swap(self, array, i, j):
        tmp = array[i]
        array[i] = array[j]
        array[j] = tmp        

    def partitionArray(self, array, k):
        i, j = 0, len(array)-1

        while i < j:
            if array[i] >= k:
                self.swap(array, i, j)
                j -= 1
            else:
                i += 1
                
        return i

if __name__ == ""
            
            
        
