import csv
import os
from actions import Student


class DataManager:
    """Gestiona la importación y exportación de datos a CSV."""
    
    def __init__(self):
        self.fieldnames = ["student_name", "student_section", "spanish", "english", "socials", "science"]
    
    def export_to_csv(self, filename, manager):
        """Exporta los estudiantes a un archivo CSV."""
        if manager.is_empty():
            print("\nNo hay datos para exportar.")
            return

        try:
            with open(filename, "w", newline='', encoding='utf-8') as f:
                writer = csv.DictWriter(f, fieldnames=self.fieldnames)
                writer.writeheader()
                for student in manager.get_all_students():
                    row = {
                        "student_name": student.name,
                        "student_section": student.section,
                        "spanish": student.grades.get("spanish", ""),
                        "english": student.grades.get("english", ""),
                        "socials": student.grades.get("socials", ""),
                        "science": student.grades.get("science", ""),
                    }
                    writer.writerow(row)
            print(f"\nDatos exportados correctamente a '{filename}'.")
        except Exception as e:
            print(f"Error al exportar a CSV: {e}")
    
    def import_from_csv(self, filename):
        """Importa estudiantes desde un archivo CSV."""
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

                    student = Student(
                        row.get("student_name", "").strip(),
                        row.get("student_section", "").strip(),
                        spanish,
                        english,
                        socials,
                        science,
                    )
                    students.append(student)
            return students
        except Exception as e:
            print(f"Error al importar desde CSV: {e}")
            return None
