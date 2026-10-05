salary = float(input("Enter the basic salary"))
HRA = salary *20/100
DA = salary *15/100
PF = salary *8/100
Net_salary = salary + HRA + DA - PF
print("HRA:",HRA)
print("DA:",DA)
print("PF:",PF)
print("Net Salary=",Net_salary)