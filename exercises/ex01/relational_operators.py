"""EX 01 relational_operators boolean expresssions."""

__author__ = "730400384"

lhs_number: int = int(input("Left-hand side: "))
rhs_number: int = int(input("Right-hand side: "))
less_than: bool = lhs_number < rhs_number
at_least: bool = lhs_number >= rhs_number
equal: bool = lhs_number == rhs_number
is_not: bool = lhs_number != rhs_number
print(str(lhs_number) + " < " + str(rhs_number) + " is " + str(less_than))
print(str(lhs_number) + " >= " + str(rhs_number) + " is " + str(at_least))
print(str(lhs_number) + " == " + str(rhs_number) + " is " + str(equal))
print(str(lhs_number) + " != " + str(rhs_number) + " is " + str(is_not))