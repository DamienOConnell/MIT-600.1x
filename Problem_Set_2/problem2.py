#!/usr/bin/env python3


balance = 484
annualInterestRate = 0.2


def yearResult(balance, fixedMonthlyPayment):
    for m in range(12):
        balance -= fixedMonthlyPayment
        balance += balance * monthlyInterestRate
    return balance


monthlyInterestRate = annualInterestRate / 12.0
fixedMonthlyPayment = 0

while (yearResult(balance, fixedMonthlyPayment)) > 0:
    fixedMonthlyPayment += 10

print(fixedMonthlyPayment)
