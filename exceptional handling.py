x=int(input("Enter first number"))
y=int(input("Enter second number"))
try:
    z=x/y
    print("Division result",z)
except ZeroDivisionError:
  print("Invalid attempt of division")
print("Hello this line is last line")   