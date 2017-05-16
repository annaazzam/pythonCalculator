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
	m = re.search(r'(\([^()]*\))', 'abcdef')
	m.group(0)