"""EX 01 numeric_operators calculation problem."""

__author__ = "730400384"

lhs_number: int = int(input("Left-hand side: "))
rhs_number: int = int(input("Right-hand side: "))
exponent: float = lhs_number ** rhs_number
division: float = lhs_number / rhs_number
whole_number: float = lhs_number // rhs_number
remainder: float = lhs_number % rhs_number
print(str(lhs_number) + " ** " + str(rhs_number) + " is " + str(exponent))
print(str(lhs_number) + " / " + str(rhs_number) + " is " + str(division))
print(str(lhs_number) + " // " + str(rhs_number) + " is " + str(whole_number))
print(str(lhs_number) + " % " + str(rhs_number) + " is " + str(remainder))