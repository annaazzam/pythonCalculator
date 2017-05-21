import re
import sys

# Reads in input and prints the calculated result
def main():
	for expression in sys.stdin:
		printCalculator(expression)

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
	# Add implicit multiplication signs
	#  e.g. 5(1+2) ----> 5*(1+2)
	m = re.search('([0-9\)])(\()', expr)
	while (m and m.group()):
		match = m.group(0)[0] + m.group(0)[1]
		matchWithMult = m.group(0)[0] + '*' + m.group(0)[1]
		expr = expr.replace(match, matchWithMult)
		m = re.search('([0-9]\))(\()', expr)

	# Evaluate Brackets:
	m = re.search('(\([^\(\)]*\))', expr)
	while (m and m.group()):
		withoutBrackets = re.sub('[\(\)]', '', m.group(0))
		evaluatedBrackets = calculator(withoutBrackets)
		expr = expr.replace(m.group(0), str(evaluatedBrackets))
		m = re.search('(\([^()]*\))', expr)


	# Split into tokens where a token is a number, or an operator (alternating)
	tokens = []
	characters = list(expr)
	current = "num"
	currVal = ""
	for c in characters:
		if (isOperator(c)):
			if (currVal != ""):
				tokens.append(float(currVal))
			tokens.append(c)
			currVal = ""
		else:
			currVal = currVal + c
	tokens.append(float(currVal))

	# deal with (syntactically correct) operator at the beginning
	if (tokens[0] == '+'):
		tokens.pop(0)
	elif (tokens[0] == '-'):
		tokens[1] = tokens[1] * -1
		tokens.pop(0)

	# Handle double operators e.g. +-
	i = 0
	while (i < len(tokens) - 1):
		if (isOperator(tokens[i])):
			if (tokens[i+1] == '-'):
				tokens[i+2] = tokens[i+2] * -1
				tokens.pop(i+1)
			if (tokens[i+1] == '+'):
				tokens.pop(i+1)
		i += 1

	# Evaluate multiplication, division, exponents:
	i = -1
	while (i < len(tokens) - 2):
		i += 1
		if (not isOperator(tokens[i])
			and not isOperator(tokens[i+2])):
			result = 0
			if (tokens[i+1] == '*'):
				result = tokens[i] * tokens[i+2]
			elif (tokens[i+1] == '/'):
				result = tokens[i] / tokens[i+2]
			elif (tokens[i+1] == '^'):
				result = power(tokens[i], tokens[i+2])
			else:
				continue
			tokens[i] = result
			tokens.pop(i+2)
			tokens.pop(i+1)
			i = -1

	result = tokens[0]
	i = 2
	while (i < len(tokens)):
		tokens.append(currVal)
		if (tokens[i-1] == '+'):
			result += tokens[i]
		elif (tokens[i-1] == '-'):
			result -= tokens[i]
		i += 2

	return result


def isOperator(token):
	if (token == '+' or token == '-'
			or token == '*' or token == '/' or token == '^'):
		return 1
	return 0

def power(base, exponent):
	if (exponent == 0):
		return 1
	i = 1
	curr = base
	while (i < exponent):
		curr = curr * base
		i += 1
	return curr

if __name__ == "__main__":
   main()