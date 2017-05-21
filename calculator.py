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

	# Add implicit multiplication signs
	#  e.g. 5(1+2) ----> 5*(1+2)
	m = re.search('([0-9\)])(\()', expr)
	while (m and m.group()):
		match = m.group(0)[0] + m.group(0)[1]
		matchWithMult = m.group(0)[0] + '*' + m.group(0)[1]
		expr = expr.replace(match, matchWithMult)
		m = re.search('([0-9]\))(\()', expr)

	# Evaluate Brackets:
	m = re.search('(\([^()]*\))', expr)
	while (m and m.group()):
		withoutBrackets = re.sub('[\(\)]', '', m.group(0))
		evaluatedBrackets = calculator(withoutBrackets)
		expr = expr.replace(m.group(0), str(evaluatedBrackets))
		m = re.search('(\([^()]*\))', expr)
	
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

	# Evaluate addition / subtraction:

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


	# Evaluate multiplication:
	i = -1
	while (i < len(tokens) - 2):
		i += 1
		if (not isOperator(tokens[i])
			and tokens[i+1] == '*'
			and not isOperator(tokens[i+2])):
			multiplicationResult = tokens[i] * tokens[i+2]
			tokens[i] = multiplicationResult
			tokens.pop(i+2)
			tokens.pop(i+1)
			i = -1
		

	# Evaluate division:
	i = -1
	while (i < len(tokens) - 2):
		i += 1
		if (not isOperator(tokens[i])
			and tokens[i+1] == '/'
			and not isOperator(tokens[i+2])):
			multiplicationResult = tokens[i] / tokens[i+2]
			tokens[i] = multiplicationResult
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


#####################################
####### SOME OF ANNAS TESTS #########
#####################################

# Simple addition
assert(calculator("5+3") == 8)
assert(calculator("5+3+2+6+8+12") == 36)

# Decimals
calcVal = calculator("52.1+3251+112+6+8.7+1")
assert(abs(3430.8 - calcVal) <= 0.0000000001) # because of f.p. error

# Simple addition and subtraction
assert(calculator("5-3-2+6-8-12") == -14)

# First number negative
assert(calculator("-5-3-2+6-8-12") == -24)

# Testing adding spaces
assert(calculator("-5 - 3 - 2 + 6 - 8 - 12") == -24)


# Testing basic brackets
assert(calculator("(5+3)") == 8)

# .. and more complicated brackets
assert(calculator("-5-(3-2)+(6-8)-12") == -20)
assert(calculator("-5-((3-2)+(6-8))-12") == -16)

# Testing multiplication
assert(calculator("5 * 1") == 5)
assert(calculator("5 * 2") == 10)
assert(calculator("5 * 3") == 15)
assert(calculator("1 * 12 * 5 * 3") == 180)

# Testing implicit multiplication sign insertion
assert(calculator("2(5 + 3)") == 16)
calcVal = calculator("6(22.1 + 56.35)")
assert(abs(470.7 - calcVal) <= 0.0000000001) # because of f.p. error
assert(calculator("(66 + 10)(4 + 15)") == 1444)


print("ALL TESTS PASSED. YOU ARE AWESOME :)")


# PUT CODE HERE TO READ IN INPUT #