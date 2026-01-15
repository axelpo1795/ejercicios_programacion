import csv
import os


def export_to_csv(filename, students):
    if not students:
        print("\nNo hay datos para exportar.")
        return

    fieldnames = ["student_name", "student_section", "spanish", "english", "socials", "science"]
    try:
        with open(filename, "w", newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            for student in students:
                row = {
                    "student_name": student["student_name"],
                    "student_section": student["student_section"],
                    "spanish": student["student_grades"].get("spanish", ""),
                    "english": student["student_grades"].get("english", ""),
                    "socials": student["student_grades"].get("socials", ""),
                    "science": student["student_grades"].get("science", ""),
                }
                writer.writerow(row)
        print(f"\nDatos exportados correctamente a '{filename}'.")
    except Exception as e:
        print(f"Error al exportar a CSV: {e}")


def import_from_csv(filename):
    if not os.path.exists(filename):
        print(f"\nNo existe el archivo '{filename}'. Por favor exporte primero o verifique el nombre.")
        return None

    students = []
    try:
        with open(filename, "r", encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                try:
                    spanish = float(row.get("spanish", 0))
                except ValueError:
                    spanish = 0.0
                try:
                    english = float(row.get("english", 0))
                except ValueError:
                    english = 0.0
                try:
                    socials = float(row.get("socials", 0))
                except ValueError:
                    socials = 0.0
                try:
                    science = float(row.get("science", 0))
                except ValueError:
                    science = 0.0

                student = {
                    "student_name": row.get("student_name", "").strip(),
                    "student_section": row.get("student_section", "").strip(),
                    "student_grades": {
                        "spanish": spanish,
                        "english": english,
                        "socials": socials,
                        "science": science,
                    },
                }
                students.append(student)
        return students
    except Exception as e:
        print(f"Error al importar desde CSV: {e}")
        return None
