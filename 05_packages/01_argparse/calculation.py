from __future__ import print_function
import argparse

def main():
	parser = argparse.ArgumentParser(description='This code is written for practice about argparse')
	parser.add_argument('X', type=float,
			metavar='First_number',
			help='What is the first number?')
	parser.add_argument('Y', type=float,
			metavar='Second_number',
			help='What is the second number?')
	parser.add_argument('--op', type=str, default='add',
			choices=['add','sub','mul','div'],
			help='What operation?')
	args = parser.parse_args()

	X = args.X
	Y = args.Y
	op = args.op
	print(calc(X,Y,op))

def calc(x, y, op):
	if op == 'add':
		return x + y
	elif op == 'sub':
		return x - y
	elif op == 'mul':
		return x * y
	elif op == 'div':
		return x / y

if __name__=="__main__":
	main()

