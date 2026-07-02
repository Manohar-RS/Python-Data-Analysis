## Day-3
## Topic : Addition And Division

## Write a Python program to do arithmetical operations addition and division.
## Addition

n1 = float(input("Enter the first number for addition: "))
n2 = float(input("Enter the second number for addition: "))
sum = num1 + num2
print(f"sum: {n1} + {n2} = {sum}")

## Division

n3 = float(input("Enter the dividend for division: "))
n4 = float(input("Enter the divisor for division: "))
if n4 == 0:
print("Division by zero is not allowed.")
else:
division = n3 / n4
print(f"Division: {n3} / {n4} = {division}")
