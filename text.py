
a = 25
print(type(a)) 

b="ganga"
print(type(b))

c=2.2
print(type(c))


a = 3+5j
b = 5j
c = -5j

print(type(a))
print(type(b))
print(type(c))



#convert from integer type to float:
a = float(3)

#convert from float type to integer:
b = int(4.5)

#convert from integer type to complex:
c = complex(3)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))



import random

print(random.randrange(5, 10))


a_int = 456
b_flo = 4.56

c = a_int + b_flo

print("datatype of a_int:",type(a_int))
print("datatype of b_flo:",type(b_flo))

print("Value of c :",c)
print("datatype of c:",type(c))


a_int = 123
b_str = "456"

print("Data type of a_int:",type(a_int))
print("Data type of b_str:",type(b_str))

print(a_int+b_str)


number_int = 123
number_str = "456"

print("Data type of number_int:",type(number_int))
print("Data type of number_str before Type Casting:",type(number_str))

number_str = int(number_str)
print("Data type of number_str after Type Casting:",type(number_str))

number_sum = number_int + number_str

print("Sum of number_int and number_str:",number_sum)
print("Data type of the sum:",type(number_sum))


number_int = 123
number_str = "456"

print("Data type of number_int:",type(number_int))
print("Data type of number_str before Type Casting:",type(number_str))

number_str = int(number_str)
print("Data type of number_str after Type Casting:",type(number_str))

number_sum = number_int + number_str

print("Sum of number_int and number_str:",number_sum)
print("Data type of the sum:",type(number_sum))