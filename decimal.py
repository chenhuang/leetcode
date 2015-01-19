class Solution:
    #@param n: Given a decimal number that is passed in as a string
    #@return: A string
    def binaryRepresentation1(self, n):
        # write you code here
        integer_part, decimal_part = n.split(".")
        output = ""

        if int(decimal_part) == 0:
            multiplier = 0
        else:
            multiplier = len(decimal_part)
            
        n = float(n)
        n *= pow(2, multiplier*2)

        print n, int(n), multiplier
        if n - int(n) != 0.0:
            return "ERROR"
        
        n = int(n)
        while n > 0 or multiplier > 0:
            output = str(n >> 1 << 1 ^ n) + output
            n = n >> 1
            multiplier -= 1
            if multiplier == 0:
                output = "." + output

        if output[0] == '.':
            output = '0' + output
                
        return output

    def binaryRepresentation(self, n):
        float_n = float(n)
        i = 0
        while True:
            if float_n - int(float_n) == 0.0:
                break
            decimal_part = float_n - int(float_n) 
            float_n *= 2
            i += 1
            if float_n - int(float_n) < decimal_part and decimal_part != 0.5:
                print float_n, decimal_part
                return "ERROR"
        
        float_n = str(bin(int(float_n))[2:])
        if i != 0:
            return float_n[0:len(float_n) - i]+'.'+float_n[len(float_n) - i:]
        else:
            return float_n
            
        
if __name__ == "__main__":
    s = Solution()
    print s.binaryRepresentation('0.6418459415435791')
    print s.binaryRepresentation('0.0625')

