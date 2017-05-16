import re

def printCalculator(expr):
	print(calculator(expr))

# Function which given an arithmetic expression (string),
# will return a number holding the result. 
# Follows the following order of operation:
#  - Parentheses: represented by by '(', ')' characters
#  - Exponents: '^' character e.g. 5^2 = 25
#  - Multiplication: '*'' character
#  - Division: '/' character
#  - Addition: '+' character
#  - Subtraction: '-' character
# Works by recursively calling calculator() on sub expressions
# until we are left with a string of + and - arithmetic, which can
# be evaluated iteratively. 
def calculator(expr):
	# Remove spaces for regex convenience
	expr = re.sub(r'\s', '', expr)

	# # Add implicit multiplication signs
	# #  e.g. 5(1+2) ----> 5*(1+2)
	# m = re.search('([^\^\*\-\+\/])(\()', expr)
	# while (m.group()):
	# 	match = m.group(0) + m.group(1)
	# 	matchWithMult = m.group(0) + '*' + m.group(1)
	# 	expr = expr.replace(match, matchWithMult)
	# 	m = re.search('([^\^\*\-\+\/])(\()', expr)

	# # Evaluate Brackets:
	# m = re.search('(\([^()]*\))', expr)
	# for i in range(0, len(m.group())):
	# 	withoutBrackets = re.sub('[\(\)]', '', m.group(i))
	# 	evaluatedBrackets = calculator(withoutBrackets)
	# 	expr = expr.replace(m.group(i), evaluatedBrackets)
	
	# # Evaluate exponents:
	# # Regex search for (not-operator)^(not-operator)
	# m = re.search('([^\^\*\-\+\/]+)(\^)([^\^\*\-\+\/]+)', expr)
	# while (m.group()):
	# 	match = m.group(0) + '^' + m.group(1)
	# 	lhs = m.group(0)
	# 	rhs = m.group(1)
	# 	powerResult = power(lhs, rhs)
	# 	expr = expr.replace(match, powerResult)
	# 	m = re.search('([^\^\*\-\+\/]+)(\^)([^\^\*\-\+\/]+)', expr)

	# Evaluate multiplication:

	# Evaluate division:

	# Handle: negative numbers!! ?? ---- +- ---> -
	# - at the beginning - -> negative number

	# Evaluate addition / subtraction:
	# SPLIT INTO TOKENS where a token is a number, or an operator (alternating)
	tokens = []
	characters = expr.split('')
	current = "num"
	currVal = ""
	for c in characters:
		if (c ): #is an operator
			tokens.append(int(currVal))
			tokens.append(c)
			currVal = ""
		else:
			currVal = currVal + c

	result = 0
	i = 0
	while (i < len(tokens)):
		if (tokens[i+1] == '+'):
			result -= tokens[i]
		elif (tokens[i+1] == '-'):
			result += tokens[i]
		i+=2

	return result