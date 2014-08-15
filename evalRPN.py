#! /usr/bin/python

'''
Evaluate Reverse Polish Notation:

Evaluate the value of an arithmetic expression in Reverse Polish Notation.

Valid operators are +, -, *, /. Each operand may be an integer or another expression.

Some examples:
  ["2", "1", "+", "3", "*"] -> ((2 + 1) * 3) -> 9
  ["4", "13", "5", "/", "+"] -> (4 + (13 / 5)) -> 6
'''

def evalRPN(tokens):
	number_stack = []
	operand_stack = []
	operands = ['+','-','*','/']
	for i in tokens:
		if i not in operands:
			number_stack.insert(0,int(i))
		if i in operands:
			n1 = number_stack.pop(0)
			n2 = number_stack.pop(0)
			if i == '+':
				number_stack.insert(0,(n2)+(n1))
			if i == '-':
				number_stack.insert(0,(n2)-(n1))
			if i == '*':
				number_stack.insert(0,(n2)*(n1))
			if i == '/':
				number_stack.insert(0,(n2)/(n1))
	return (number_stack.pop())

print evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"])
print evalRPN(["4", "13", "5", "/", "+"])
