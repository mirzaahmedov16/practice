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


# DEFINE - build

def greet(a):
    print(f"How do you do, {a}")


def greeting(b):
    print("greeting is executed")
    return f"Hi {b}"

# CALL - execute


result1 = greet('neo')
print('result1:', result1)

result2 = greet('Justin')
print('result2:', result2)
