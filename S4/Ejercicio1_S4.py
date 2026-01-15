# Ejercicio1_S4.py
# string + string
result_1 = "Hello " + "World"
print("string + string →", result_1)

# string + int
try:
    result_2 = "Age: " + 25
except TypeError as e:
    print("string + int → Error:", e)

# int + string
try:
    result_3 = 10 + "5"
except TypeError as e:
    print("int + string → Error:", e)

# list + list
result_4 = [1, 2, 3] + [4, 5]
print("list + list →", result_4)

# string + list
try:
    result_5 = "Data" + [1, 2, 3]
except TypeError as e:
    print("string + list → Error:", e)

# float + int
result_6 = 3.5 + 2
print("float + int →", result_6)

# bool + bool
result_7 = True + False
print("bool + bool →", result_7)