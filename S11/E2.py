class Person:
    "Clase persona."
    
    def __init__(self, name, age):
        """
        Contructor persona.
        """
        try:
            if not isinstance(name, str) or not name.strip():
                raise ValueError("El nombre debe ser una cadena no vacía.")
            if not isinstance(age, (int, float)) or age < 0:
                raise ValueError("La edad debe ser un número positivo.")
            self.name = name.strip()
            self.age = int(age)
        except (ValueError, TypeError) as e:
            print(f"Error al crear persona: {e}")
            raise
    
    def __str__(self):
        return f"{self.name} ({self.age} años)"


class Bus:
    "Clase autobús con un número máximo de pasajeros."
    
    def __init__(self, max_passengers):
        """
        Constructor autobús.
        """
        try:
            if not isinstance(max_passengers, int) or max_passengers <= 0:
                raise ValueError("La capacidad máxima debe ser un número entero positivo.")
            self.max_passengers = max_passengers
            self.passengers = []
        except (ValueError, TypeError) as e:
            print(f"Error al crear autobús: {e}")
            raise
    
    def add_passenger(self, person):
        """
        Agrega un pasajero al autobús si hay espacio disponible.
        """
        try:
            if not isinstance(person, Person):
                raise TypeError("El pasajero debe ser una instancia de la clase Person.")
            if len(self.passengers) < self.max_passengers:
                self.passengers.append(person)
                print(f"{person.name} ha subido al autobús. ({len(self.passengers)}/{self.max_passengers})")
            else:
                print(f"El autobús está lleno. No se puede agregar a {person.name}.")
        except (TypeError, AttributeError) as e:
            print(f"Error al agregar pasajero: {e}")
    
    def remove_passenger(self, person):
        """
        Baja un pasajero del autobús.
        """
        try:
            if not isinstance(person, Person):
                raise TypeError("El pasajero debe ser una instancia de la clase Person.")
            if person in self.passengers:
                self.passengers.remove(person)
                print(f"{person.name} ha bajado del autobús. ({len(self.passengers)}/{self.max_passengers})")
            else:
                print(f"{person.name} no está en el autobús.")
        except (TypeError, AttributeError) as e:
            print(f"Error al bajar pasajero: {e}")
    
    def get_passengers(self):
        "Retorna la lista de pasajeros actuales."
        return self.passengers
    
    def get_current_capacity(self):
        "Retorna la cantidad actual de pasajeros."
        return len(self.passengers)
    
    def is_full(self):
        "Verifica si el autobús está lleno."
        return len(self.passengers) == self.max_passengers
    
    def __str__(self):
        "Retorna una representación en string del autobús y sus pasajeros."
        passengers_str = "\n  ".join([str(p) for p in self.passengers]) if self.passengers else "Ninguno"
        return f"Autobús (Capacidad: {len(self.passengers)}/{self.max_passengers})\nPasajeros:\n  {passengers_str}"


# Ejemplo de uso
if __name__ == "__main__":
    # Crear personas
    person1 = Person("Juan", 25)
    person2 = Person("María", 30)
    
    # Crear un autobús con capacidad para 1
    bus = Bus(1)
    
    print("=== Agregando pasajeros ===")
    bus.add_passenger(person1)
    bus.add_passenger(person2)
    
    print("\n=== Estado actual del autobús ===")
    print(bus)
    
    print("\n=== Bajando pasajeros ===")
    bus.remove_passenger(person1)
    
    print("\n=== Estado después de bajar pasajeros ===")
    print(bus)
    
    print("\n=== Agregando más pasajeros ===")
    bus.add_passenger(person2)
