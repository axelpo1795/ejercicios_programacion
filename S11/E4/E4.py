class Hand:
    """Representa una mano."""
    
    def __init__(self):
        """Constructor una mano."""
        self.fingers = 5
    
    def __str__(self):
        return f"Mano ({self.fingers} dedos)"


class Arm:
    """Representa un brazo con una mano."""
    
    def __init__(self, hand):
        """
        Constructor un brazo.
        
        Args:
            hand: Una instancia de la clase Hand.
        """
        self.hand = hand
    
    def __str__(self):
        return f"Brazo -> {self.hand}"


class Feet:
    """Representa unos pies."""
    
    def __init__(self):
        """Constructor unos pies."""
        self.toes = 5
    
    def __str__(self):
        return f"Pies ({self.toes} dedos)"


class Leg:
    """Representa una pierna con pies."""
    
    def __init__(self, feet):
        """
        Constructor una pierna.
        """
        self.feet = feet
    
    def __str__(self):
        return f"Pierna -> {self.feet}"


class Head:
    """Representa una cabeza."""
    
    def __init__(self, color_hair="castaño", color_eyes="marrón"):
        """
        Constructor una cabeza.
        
        Args:
            color_hair: Color del cabello.
            color_eyes: Color de los ojos.
        """
        self.color_hair = color_hair
        self.color_eyes = color_eyes
    
    def __str__(self):
        return f"Cabeza (Cabello: {self.color_hair}, Ojos: {self.color_eyes})"


class Torso:
    """Representa un torso con cabeza, brazos y piernas."""
    
    def __init__(self, head, right_arm, left_arm, right_leg, left_leg):
        """
        Constructor un torso.
        
        Args:
            head: Una instancia de la clase Head.
            right_arm: Una instancia de la clase Arm (brazo derecho).
            left_arm: Una instancia de la clase Arm (brazo izquierdo).
            right_leg: Una instancia de la clase Leg (pierna derecha).
            left_leg: Una instancia de la clase Leg (pierna izquierda).
        """
        self.head = head
        self.right_arm = right_arm
        self.left_arm = left_arm
        self.right_leg = right_leg
        self.left_leg = left_leg
    
    def __str__(self):
        return (f"Torso:\n"
                f"  - {self.head}\n"
                f"  - Brazo derecho: {self.right_arm}\n"
                f"  - Brazo izquierdo: {self.left_arm}\n"
                f"  - Pierna derecha: {self.right_leg}\n"
                f"  - Pierna izquierda: {self.left_leg}")


class Human:
    """Representa un ser humano con todas sus partes del cuerpo."""
    
    def __init__(self, name, torso):
        """
        Constructor un ser humano.
        
        Args:
            name: Nombre de la persona.
            torso: Una instancia de la clase Torso.
        """
        self.name = name
        self.torso = torso
    
    def __str__(self):
        return f"{self.name}:\n{self.torso}"


# Ejemplo de uso
if __name__ == "__main__":
    # Crear manos
    right_hand = Hand()
    left_hand = Hand()
    
    # Crear brazos con manos
    right_arm = Arm(right_hand)
    left_arm = Arm(left_hand)
    
    # Crear pies
    right_feet = Feet()
    left_feet = Feet()
    
    # Crear piernas con pies
    right_leg = Leg(right_feet)
    left_leg = Leg(left_feet)
    
    # Crear cabeza
    head = Head("rubio", "azul")
    
    # Crear torso conectando todas las partes
    torso = Torso(head, right_arm, left_arm, right_leg, left_leg)
    
    # Crear un ser humano
    human = Human("Carlos", torso)
    
    print("=== Representación del ser humano ===")
    print(human)
    
    print("\n=== Acceso a partes específicas ===")
    print(f"Nombre: {human.name}")
    print(f"Cabeza: {human.torso.head}")
    print(f"Mano derecha: {human.torso.right_arm.hand}")
    print(f"Pies derechos: {human.torso.right_leg.feet}")
