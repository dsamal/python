__author__ = 'DEBASISH'

# Fibonacci Series:
# The sum of two elements defines the next

print("Hello, Please print a fibonanci series numbers till 100")
print("Well here yo go")

a, b = 0, 1
print("The Fibonacci Series is:", end='')
while a < 100:
	print(a, end=',')
	a, b = b, a+b
