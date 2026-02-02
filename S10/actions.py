def input_grade(prompt):
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


def add_students(students):
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

        student = {
            "student_name": name,
            "student_section": section,
            "student_grades": {
                "spanish": spanish,
                "english": english,
                "socials": socials,
                "science": science,
            },
        }
        students.append(student)

    print(f"\nSe agregaron {n} estudiante(s) correctamente.")


def show_students(students):
    if not students:
        print("\nNo hay estudiantes registrados.")
        return

    print("\nLista de estudiantes ingresados:")
    for idx, student in enumerate(students, start=1):
        print(f"\nEstudiante {idx}:")
        print(f"Nombre: {student['student_name']}")
        print(f"Sección: {student['student_section']}")
        print("Notas:")
        for subject, grade in student['student_grades'].items():
            print(f"  {subject.capitalize()}: {grade}")
        avg = sum(student['student_grades'].values()) / len(student['student_grades'])
        print(f"Promedio: {avg:.2f}")


def show_top_3(students):
    if not students:
        print("\nNo hay estudiantes registrados.")
        return
    with_avg = []
    for student in students:
        avg = sum(student['student_grades'].values()) / len(student['student_grades'])
        with_avg.append((avg, student))

    with_avg.sort(key=lambda x: x[0], reverse=True)
    top = with_avg[:3]
    print("\nTop estudiantes por promedio:")
    for rank, item in enumerate(top, start=1):
        avg, student = item
        print(f"\n{rank}. {student['student_name']} - Sección: {student['student_section']} - Promedio: {avg:.2f}")


def show_average_of_averages(students):
    if not students:
        print("\nNo hay estudiantes registrados.")
        return
    avgs = []
    for student in students:
        avg = sum(student['student_grades'].values()) / len(student['student_grades'])
        avgs.append(avg)
    overall = sum(avgs) / len(avgs)
    print(f"\nPromedio general (promedio de promedios): {overall:.2f}")
