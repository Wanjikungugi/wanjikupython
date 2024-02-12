# Area of a rectangle - length * width
length = int(input("Enter length:"))
width = int(input("Enter width:"))
print("The area is",length * width)

area = length * width
print("the area is",area)

# Perimeter of a rectangle - 2(l+w)
len= int(input("Enter length:"))
wid= int(input("Enter width:"))
perimeter = 2*(len+wid)
print("The perimeter is ",perimeter)

x = float (input("Enter first number:"))
y = float (input("Enter second number:"))
operator=input("Enter operator:")
if operator=="+":
    print("Result is:",x+y)
elif operator=="-":
    print("Result is:",x-y)
elif operator=="*":
    print("Result is:",x*y)
elif operator=="/":
    print("Result is:",x/y)
else:
    print("Invalid operator")