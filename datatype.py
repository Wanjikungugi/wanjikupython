# Data Type

number = 67  # int
num =78.98  #float
greeting = "Hello there"  #str
isPythonInteresting = True  #bool

# A variable storing multiple values
languages = ["Python","PHP","JavaScript"] # list
fruits =["banana","apple","orange"] # tuple
countries ={"Kenya","Chaina","America"} # Set
# Dictionary
details = {
    "firstname":"Brian",
    "age":17,
    "course":"MIT",
    "nationality": "American"
}



print(number)
print(isPythonInteresting)
print(countries)
print(details)
print(details["course"])
print(details["nationality"])



#Determining the Data Type
print(type(details))
print(type(countries))
print(type(languages))


#Typecasting-it is converting one data type to another
print(float(number))
print(int(num))


