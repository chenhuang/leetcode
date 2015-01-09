class Solution:
    def parseString(self, inputString, x):
        (left,right) = inputString.split("=")
        left_num = self.computeEquation(left)
        right_num = self.computeEquation(right)
        result = self.add(left_num, self.reverse(right_num))
        return float( result[0] + x * result[1] ) * (-1) / float(result[2])

    def add(self, num2, num1):
        return (num2[0]+num1[0], num2[1]+num1[1], num2[2]+num1[2])

    def reverse(self, num):
        return (-1*num[0],-1*num[1],-1*num[2])

    def computeEquation(self, input):
        itms = input.split(" ")
        num_stack = [] # stores (a,b,c): a: numeric, b: x coeffi, c: y coeffi
        oper_stack = []

        # add numbers
        for itm in itms:
            print num_stack, oper_stack, itm
            if itm in ['+','-','(',')']:
                if itm != ')':
                    oper_stack.append(itm)
                else:
                    oper = oper_stack.pop()
                    while oper != '(':
                        num1 = num_stack.pop()
                        num2 = num_stack.pop()

                        if oper == '+':
                            num_stack.append(self.add(num2,num1))
                        if oper == '-':
                            num_stack.append(self.add(num2,self.reverse(num1)))
                        oper = oper_stack.pop()
            else:
                if 'x' in itm:
                    if itm == 'x':
                        num_stack.append((0,1,0))
                    else:
                        num_stack.append((0,int(itm[0:-1]),0))
                elif 'y' in itm:
                    if itm == 'y':
                        num_stack.append((0,0,1))
                    else:
                        num_stack.append((0,0,int(itm[0:-1])))
                elif itm.isdigit():
                    num_stack.append((int(itm),0,0))

                if len(oper_stack) > 0 and oper_stack[-1] == '-':
                    num_stack.append(self.reverse(num_stack.pop()))
                    oper_stack[-1] = '+'

       # copute results 
        while len(oper_stack) > 0:
            num1 = num_stack.pop()
            num2 = num_stack.pop()
            oper_stack.pop()
            num_stack.append(self.add(num2,num1))

        return num_stack.pop()

class Solution1():
    def __init__(self):
        self.prior = {"(":4, "-":2, "+":2, ")":1}
    def parseString(self, input_string, x):
        (left, right) = input_string.split("=")

        left_num = self.computeEquation(left)
        right_num = self.computeEquation(right)
        result = self.minus(left_num, right_num)
        return float( result[0] + x * result[1] ) * (-1) / float(result[2])

    def add(self, num2, num1):
        return (num2[0]+num1[0],num2[1]+num1[1],num2[2]+num1[2])

    def minus(self, num2, num1):
        return (num2[0]-num1[0],num2[1]-num1[1],num2[2]-num1[2])

    def computeEquation(self, input_string):
        num_stack = []
        oper_stack = []

        itms = input_string.split(" ")
        for itm in itms:
            if len(itm) == 0:
                continue

            if itm in ['+','-','(',')']:
                if len(oper_stack) > 0 and self.prior[oper_stack[-1]] >= self.prior[itm]:
                    if oper_stack[-1] == "+":
                        num_stack.append(self.add(num_stack.pop(),num_stack.pop()))
                        oper_stack.pop()
                    elif oper_stack[-1] == "-":
                        num1 = num_stack.pop()
                        num2 = num_stack.pop()
                        num_stack.append(self.minus(num2,num1))
                        oper_stack.pop()
                oper_stack.append(itm)
                if oper_stack[-1] == ')':
                    oper_stack.pop()
                    oper_stack.pop()
            else: 
                if itm.isdigit():
                    num_stack.append((int(itm),0,0))
                else:
                    if 'x' in itm:
                        if itm == 'x':
                            num_stack.append((0,1,0))
                        else:
                            num_stack.append((0,int(itm[0:-1]),0))
                    else:
                        if itm == 'y':
                            num_stack.append((0,0,1))
                        else:
                            num_stack.append((0,0,int(itm[0:-1])))

        while len(oper_stack) > 0:
            num1 = num_stack.pop()
            num2 = num_stack.pop()
            oper = oper_stack.pop()
            if oper == '+':
                num_stack.append(self.add(num1,num2))
            elif oper == "-":
                num_stack.append(self.minus(num2,num1))

        return num_stack.pop()

if __name__ == "__main__":
    s = Solution1()
    print s.parseString("x - ( y - ( 5 + 3y ) ) = 3y + 2x - 1", 2)
    print s.parseString("5 + 2x - ( 3y + 2x - ( 7 - 2x ) - 9 ) = 3 + 4y", 2)
    print s.parseString("2y - ( y + 5 ) = 3y + 6", 2)
    print s.parseString("10x + y = 2y - 10", 2)
    print s.parseString("x + 5 + y = 2y - 3x - 10", 2)
