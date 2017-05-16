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
def calculator(expr):
	# Remove spaces:
	expr = re.sub(r'\s', '', expr)

	# Add implicit multiplication signs
	#  e.g. 5(1+2) ----> 5*(1+2)
	m = re.search('([^\^\*\-\+\/])(\()', expr)
	while (m.group()):
		match = m.group(0) + m.group(1)
		matchWithMult = m.group(0) + '*' + m.group(1)
		expr = expr.replace(match, matchWithMult)
		m = re.search('([^\^\*\-\+\/])(\()', expr)

	# Evaluate Brackets:
	m = re.search('(\([^()]*\))', expr)
	for i in range(0, m.group().length):
		withoutBrackets = re.sub('[\(\)]', '', m.group(i))
		evaluatedBrackets = calculator(withoutBrackets)
		expr = expr.replace(m.group(i), evaluatedBrackets)
	
	# Evaluate exponents:
	# Regex search for (not-operator)^(not-operator)
	m = re.search('([^\^\*\-\+\/]+)(\^)([^\^\*\-\+\/]+)', expr)
	while (m.group()):
		powerResult = power()
	m = re.search('()\^()', expr)

	return expr