"""
Gross salary calculator.
User enters basic salary.
HRA = 20% of basic, DA = 40% of basic
Gross salary = basic + HRA + DA
"""

basic = float(input("Enter basic salary: "))

hra = 0.20 * basic
da = 0.40 * basic
gross_salary = basic + hra + da

print(f"Basic Salary : {basic:.2f}")
print(f"HRA (20%)    : {hra:.2f}")
print(f"DA (40%)     : {da:.2f}")
print(f"Gross Salary : {gross_salary:.2f}")
