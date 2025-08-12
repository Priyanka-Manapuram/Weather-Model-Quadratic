a = float(input("Enter the coeffient a: "))
b = float(input("Enter the coefficient b: "))
c = float(input("Enter the coefficient of c:"))
t = float(input("Enter the time t (hour/day): "))

T = a * t ** 2 + b * t + c

print(f"Predicted temperature at t={t}: {T: .2f}C")