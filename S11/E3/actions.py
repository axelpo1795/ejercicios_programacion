class Student:
    """Representa un estudiante con sus notas y sección."""
    
    def __init__(self, name, section, spanish, english, socials, science):
        self.name = name
        self.section = section
        self.grades = {
            "spanish": spanish,
            "english": english,
            "socials": socials,
            "science": science,
        }
    
    def get_average(self):
        """Calcula el promedio de las notas del estudiante."""
        return sum(self.grades.values()) / len(self.grades)
    
    def __str__(self):
        avg = self.get_average()
        grades_str = "\n".join([f"  {subject.capitalize()}: {grade}" for subject, grade in self.grades.items()])
        return f"Nombre: {self.name}\nSección: {self.section}\nNotas:\n{grades_str}\nPromedio: {avg:.2f}"
    
    def to_dict(self):
        """Convierte el estudiante a un diccionario."""
        return {
            "student_name": self.name,
            "student_section": self.section,
            "student_grades": self.grades,
        }
    
    @classmethod
    def from_dict(cls, data):
        """Crea un estudiante desde un diccionario."""
        return cls(
            data["student_name"],
            data["student_section"],
            data["student_grades"]["spanish"],
            data["student_grades"]["english"],
            data["student_grades"]["socials"],
            data["student_grades"]["science"],
        )


class StudentManager:
    """Gestiona la colección de estudiantes."""
    
    def __init__(self):
        self.students = []
    
    def add_student(self, student):
        """Añade un estudiante a la lista."""
        self.students.append(student)
    
    def get_all_students(self):
        """Retorna todos los estudiantes."""
        return self.students
    
    def get_student_count(self):
        """Retorna la cantidad de estudiantes."""
        return len(self.students)
    
    def is_empty(self):
        """Verifica si no hay estudiantes."""
        return len(self.students) == 0
    
    def get_top_3(self):
        """Retorna los top 3 estudiantes por promedio."""
        if self.is_empty():
            return []
        sorted_students = sorted(self.students, key=lambda s: s.get_average(), reverse=True)
        return sorted_students[:3]
    
    def get_average_of_averages(self):
        """Calcula el promedio general de los promedios de todos los estudiantes."""
        if self.is_empty():
            return 0
        averages = [student.get_average() for student in self.students]
        return sum(averages) / len(averages)
    
    def clear(self):
        """Limpia la lista de estudiantes."""
        self.students.clear()
    
    def extend(self, students):
        """Añade múltiples estudiantes."""
        self.students.extend(students)


def input_grade(prompt):
    """Solicita una nota válida al usuario."""
    while True:
        val = input(prompt)
        try:
            num = float(val)
            if 0 <= num <= 100:
                return num
            else:
                print("La nota debe estar entre 0 y 100. Intente de nuevo.")
        except ValueError:
            print("Entrada no válida. Ingrese un número (ej. 85.5).")


def add_students(manager):
    """Añade nuevos estudiantes al gestor."""
    while True:
        cantidad = input("¿Cuántos estudiantes desea ingresar? ")
        try:
            n = int(cantidad)
            if n <= 0:
                print("Ingrese un número mayor que 0.")
                continue
            break
        except ValueError:
            print("Entrada no válida. Ingrese un número entero.")

    for i in range(1, n + 1):
        print(f"\nIngresando estudiante {i} de {n}:")
        name = input("Ingrese el nombre completo del estudiante: ").strip()
        section = input("Ingrese la sección (ej. 11B): ").strip()
        spanish = input_grade("Nota de Español: ")
        english = input_grade("Nota de Inglés: ")
        socials = input_grade("Nota de Sociales: ")
        science = input_grade("Nota de Ciencias: ")

        student = Student(name, section, spanish, english, socials, science)
        manager.add_student(student)

    print(f"\nSe agregaron {n} estudiante(s) correctamente.")


def show_students(manager):
    """Muestra todos los estudiantes registrados."""
    if manager.is_empty():
        print("\nNo hay estudiantes registrados.")
        return

    print("\nLista de estudiantes ingresados:")
    for idx, student in enumerate(manager.get_all_students(), start=1):
        print(f"\nEstudiante {idx}:")
        print(student)


def show_top_3(manager):
    """Muestra los top 3 estudiantes por promedio."""
    if manager.is_empty():
        print("\nNo hay estudiantes registrados.")
        return
    
    top = manager.get_top_3()
    print("\nTop estudiantes por promedio:")
    for rank, student in enumerate(top, start=1):
        print(f"\n{rank}. {student.name} - Sección: {student.section} - Promedio: {student.get_average():.2f}")


def show_average_of_averages(manager):
    """Muestra el promedio general de promedios."""
    if manager.is_empty():
        print("\nNo hay estudiantes registrados.")
        return
    
    overall = manager.get_average_of_averages()
    print(f"\nPromedio general (promedio de promedios): {overall:.2f}")
