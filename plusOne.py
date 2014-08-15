class Solution:
    # @param digits, a list of integer digits
    # @return a list of integer digits
    def plusOne(self, digits):
        add_one = 1
        for i in range(len(digits)-1,-1,-1):
            digits[i] += add_one
            if digits[i] >= 10:
                digits[i] -= 10
                add_one = 1
            else:
                add_one = 0
        if add_one == 1:
            digits.insert(0,1)
        return digits
