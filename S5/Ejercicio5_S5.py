numbers = []

for i in range(10):
    user_input = float(input(f"Ingrese el número #{i + 1}: "))
    numbers.append(user_input)
    
highest = max(numbers)

print(numbers)
print(f"El más alto fue {highest}.")
