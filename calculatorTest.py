
#####################################
####### SOME OF ANNAS TESTS #########
#####################################
from calculator import calculator

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

# Testing division

# Testing exponents
assert(calculator("2^4") == 16)
assert(calculator("12^5") == 248832)

print("ALL TESTS PASSED. YOU ARE AWESOME :)")
