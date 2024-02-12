try:
    print(x)
except:
    print("NameError occured")


num1 = 20
num2 = 10
try:
    print(num1 / num2)
except:
    print("ZeroDivisionError occured")


#User-defined function
try:
 def sum(first,second):
     return first + second

except:
    print("Exception occured")
finally:
 print("finally")

print(sum(10,20))
finally:

print("finally")
