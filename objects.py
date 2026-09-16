'''  OBJECTS
     (1) What is object
     (2) Iterable objects & RANGE
     (3) DICTIONARY
     (4) Error handling system
'''

import array  # package/module
import math  # package
from math import ceil, asin
print("===== What is object? =====")
# An object has state and method properties.
# Everything is object in python.

print(type("Hello MIT"))
print(type(1290))
print(type(True))
print(type(array))
print(type(math))

# Paradigm > Functional Programming & OOP
# OOP 4 CONCEPTS > Abstraction | Encapsulation | Inheritense | Polimorphism

result1 = math.ceil(324.22)  # CALL
print("result1:", result1)

result2 = math.ceil(322)  # CALL
print("result2:", result2)


print("==== Error handling system =====")

car_dict = dict(name="Tayota", year=2026, electric=True)


try:
    print("passed here")
    result = car_dict["origin"]
    a = car_dict.speed
    print("result:", result)


except KeyError as err:
    print("General Error:", err)

else:
    print("Executed successfully without errors")

finally:
    print("Final closing logic")
