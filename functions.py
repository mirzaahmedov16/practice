'''
FUNCTIONS:
(1) DEFINE & CALL
(2)PARAMETR & ARGUMENT
(3) KEYWORD & DEFINE ARGUMENTS
(4) SCOPE
'''


print("==== DEFINE vS CALL =====")
# build in function > print() type()
# Function - reusable block of code!
# Instead of block {} in JAVA, Python uses indentation!


# DEFINE
def greet(a):
    print(f"How do you do, {a}")


def greeting(b):
    print("greeting is executed")
    return f"Hi {b}"

# CALL


result1 = greet('neo')
print('result1:', result1)

result2 = greet('Justin')
print('result2:', result2)

print(" ===== Keyword & Default arguments =====")

#
# DEFINE


def give_greet(name, age=20):
    print("give_greet is execute")
    return f"Hi {name}, you are {age} years old!"


# CALL
result3 = give_greet(name="Justin", age=28)
print("result3:", result3)

result4 = give_greet(name="Neo")
print("result4:", result4)
