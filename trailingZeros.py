class Solution:
    # @return an integer
    def trailingZeroes(self, n):
        count_5 = [0,0]
        count_5_sum = 0
        
        for i in range(2,n):
            count_5.append(0)
            if i%5 == 0:
                count_5[i] = count_5[i/5]+1
                count_5_sum += count_5[i]
        
        return min(count_2_sum, count_5_sum)

    def trailingZeroes_1(self, n):
        div = 5
        result = 0
        while div <= n:
            result += n//div
            div = div*5
        return result

if __name__ == "__main__":
    s = Solution()

    print s.trailingZeroes(7178)
    print s.trailingZeroes_1(7178)

