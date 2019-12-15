#!/usr/bin/env python3

# Using bisection search, calculate the minimum payment needed to repay loan
# balance - the loan amount
# annualInterestRate - the annual rate
#
# Test Case 1:
# ---------------------------------------------------------------------
balance = 320000
annualInterestRate = 0.2
print("Result Your Code Should Generate:")
print("Lowest Payment: 29157.09")


# Test Case 2:
# ---------------------------------------------------------------------
balance = 999999
annualInterestRate = 0.18

print("Result Your Code Should Generate:")
print("Lowest Payment: 90325.03")


def yearResult(balance, monthlyPayment):
    for m in range(12):
        balance -= monthlyPayment
        balance += balance * monthlyInterestRate
    return balance


monthlyInterestRate = annualInterestRate / 12.0
paymentLowBound = balance / 12
paymentUppBound = balance * ((1 + monthlyInterestRate) ** 12) / 12.0
epsilon = 0.01
guess = 0

# while yearResult using current guess is not near enough to balance:
while abs(yearResult(balance, guess)) > epsilon:
    guess = (paymentLowBound + paymentUppBound) / 2.0

    if yearResult(balance, guess) < 0:
        paymentUppBound = guess
    else:
        paymentLowBound = guess

print("Lowest Payment:", str(round(guess, 2)))
