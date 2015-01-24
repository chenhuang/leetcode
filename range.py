'''
Input: [5,6,80]
Output: ranges in 0-99 that does not have input elements
'''

class Solution:
    def find_range(self, input):
        s, e = 0, 1
        output = []

        input = sorted(input)

        while len(input) > 0:
            while len(input) > 0 and s == input[0]:
                s += 1
                input.pop(0)

            if len(input) > 0:
                e = input[0] - 1
                if s == e:
                    output.append(str(s))
                else:
                    output.append(str(s)+"-"+str(e))
                s = e + 1
        
        if s < 99:
            output.append(str(s)+"-99")
        if s == 99:
            output.append("99")

        return output

if __name__ == "__main__":
    s = Solution()
    print s.find_range([5,6,80])
    print s.find_range([0,5,6,80,98])
            
