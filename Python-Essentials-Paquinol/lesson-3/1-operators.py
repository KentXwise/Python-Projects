# Arithmetic Operators

# + addition, - subtraction, * multiplication, / division, % modulus, ** exponentiation

x = 10
y = 3

print(x + y) # 10 + 3 = 13
print(x - y) # 10 - 3 = 7
print(x * y) # 10 * 3 = 30
print(x / y) # 10 / 3 = 3.3333333333333335
print(x % y) # 10 % 3 = 1
print(x ** y) # 10 ** 3 = 1000

# Comparison Operators

# == equal to, != not equal to, > greater than, < less than, >= greater than or equal to, <= less than or equal to

x = 10
y = 3

print(x == y) # False
print(x != y) # True
print(x > y) # True
print(x < y) # False
print(x >= y) # True
print(x <= y) # False

# Logical Operators

# and, or, not

x = True
y = False

print(x and y) # False
print(x or y) # True
print(not x) # False
print(not y) # True



# Assignment Operators

# = assignment, += addition assignment, -= subtraction assignment, *= multiplication assignment, /= division assignment, %= modulus assignment, **= exponentiation assignment

x = 10
y = 3

x += 5 # x = x + 5
y -= 2 # y = y - 2

print(x)
print(y)

# Membership Operators

# in, not in

x = "Hello"
y = "World"
z = "Zebra"

print("H" in x) # True
print("H" not in y) # True
print("H" in z) # False

# Identity Operators

# is, is not

x = 10
y = 10
z = 20
print(x is y) # True
print(x is not z) # True

# Bitwise Operators

# & bitwise and, | bitwise or, ^ bitwise xor, ~ bitwise not, << left shift, >> right shift

x = 10
y = 3

print(x & y) # 2
print(x | y) # 11
print(x ^ y) # 9
print(~x) # -11
print(x << 1) # 20
print(x >> 1) # 5
print(y << 1) # 6
print(y >> 1) # 1