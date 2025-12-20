def my_function():
    x = 10   # local variable
    print("Dentro:", x)

mi_funcion()

print("Afuera:", x)   # ERROR: x do not exist as a global variable nor const
