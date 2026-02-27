def log_io(func):
    def wrapper(*args, **kwargs):
        print(f"Llamando a {func.__name__} con args={args}, kwargs={kwargs}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} devolvió {result!r}")
        return result
    return wrapper

@log_io
def saludar(nombre, saludo="Hola"):
	return f"{saludo}, {nombre}!"


if __name__ == "__main__":
	response = saludar("Ana", saludo="Buenas")
	print("Resultados recibidos:", response)

