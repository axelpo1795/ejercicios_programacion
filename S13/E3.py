from datetime import datetime, date


class User:
    def __init__(self, name, date_of_birth):
        self.name = name
        self.date_of_birth = date_of_birth
    
    @property
    def age(self):
        """Calcula la edad actual del usuario."""
        today = date.today()
        edad = today.year - self.date_of_birth.year
        # Ajusta si aún no ha cumplido años este año
        if (today.month, today.day) < (self.date_of_birth.month, self.date_of_birth.day):
            edad -= 1
        return edad
    
    def __repr__(self):
        return f"User(name='{self.name}', age={self.age})"


def require_legal_age(func):
    def wrapper(user, *args, **kwargs):
        if not isinstance(user, User):
            raise TypeError(f"El primer parámetro debe ser un User, se recibió {type(user).__name__}")
        
        if user.age < 18:
            raise ValueError(f"El usuario {user.name} no es mayor de edad. Edad actual: {user.age} años")
        
        return func(user, *args, **kwargs)
    return wrapper


@require_legal_age
def vote(user):
    return f"{user.name} votó exitosamente (edad: {user.age})"


@require_legal_age
def rent_car(user, days):
    return f"{user.name} alquiló un auto por {days} días (edad: {user.age})"


if __name__ == "__main__":
    # Crear usuarios
    juan = User("Juan", date(2010, 5, 15))  # 13 años (aproximadamente)
    maria = User("María", date(2004, 8, 20))  # 21 años (aproximadamente)
    
    print("Usuarios creados:")
    print(f"  {juan}")
    print(f"  {maria}")
    print()
    
    print("Casos válidos (mayor de edad):")
    
    try:
        print(f"  {vote(maria)}")
    except ValueError as e:
        print(f"  Error: {e}")
    
    try:
        print(f"  {rent_car(maria, 3)}")
    except ValueError as e:
        print(f"  Error: {e}")
    
    print()
    print("Casos inválidos (menor de edad):")
    
    try:
        print(f"  {vote(juan)}")
    except ValueError as e:
        print(f"  Error: {e}")
    
    try:
        print(f"  {rent_car(juan, 1)}")
    except ValueError as e:
        print(f"  Error: {e}")
