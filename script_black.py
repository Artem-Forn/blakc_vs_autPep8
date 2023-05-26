# Wrong:
import sys, os, string


# Wrong:
i = i + 1
submitted += 1
x = x * 2 - 1
hypot2 = x * x + y * y
c = (a + b) * (a - b)

# Wrong:
x = 1
y = 2
long_variable = 3


# Wrong:
def munge(input: AnyStr):
    pass


def munge() -> PosInt:
    pass


# Wrong:
# operators sit far away from their operands
income = gross_wages + taxable_interest + (dividends - qualified_dividends) - ira_deduction - student_loan_interest

# Correct:
# easy to match operators with operands
income = gross_wages + taxable_interest + (dividends - qualified_dividends) - ira_deduction - student_loan_interest


# Wrong:
def bar(x):
    if x < 0:
        return
    return math.sqrt(x)


# _______ my variant _______

# Correct:
# easy to match operators with operands
income = (
    gross_wages
    + taxable_interest
    + (dividends - qualified_dividends)
    - ira_deduction
    - student_loan_interest
    - student_loan_interest
    - student_loan_interest
)

# Wrong :
i, a, d = "asdf", (0, "asdf"), 122
j = [1, 2, 3]

# long coment 120 + 2
# 123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890
# 1234567890 1234567890 1234567890 1234567890 1234567890 1234567890 1234567890 1234567890 1234567890 1234567890 1234567890 1234567890  2
