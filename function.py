# Inbuilt function
number = max(34, 100, 90, 67)
print(number)
y = min(45, 89, 67, 12)
print(y)

z = pow(2, 3)
print(z)


# alphabet creator to check whether it is a vowel or a constant

# user-defined function
def name():
    print("Wanjiku")


name()  # calling a function


def details():
    name = "Ngugi"
    age = 19
    course = ("MIT")
    print(name, age, course)


details()


# Parameters/variables and arguments/values
def patient(name, age, gender, marital_status):
    print(name, age, gender, marital_status)


patient("Ngugi", 19, "male", "single")
patient("Nana", 20, "female", "single")


def multiply(x, y):
    print(x * y)


multiply(23, 56)
multiply(45, 2)


# Create user-defined function called employees
# display details of five employees using the following parameters:fullname,age,position,salary

def employees(name, age, position, salary):
    print(name, age, position, salary)

employees("Frank Mbugua ",45, "CEO", KES 540000)
employees("Nancy Kiarie",35, "Resource Manager", KES 340000)
employees("Brenda Salim",23, "Director", KES 240000)
employees("Aziz Rajab",27, "Editor", KES 140000)
employees("Nicholas Oduor",22, "Supervisor", KES 40000)