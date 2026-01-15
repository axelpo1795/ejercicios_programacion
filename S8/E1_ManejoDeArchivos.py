def sort_songs(input_file, output_file):
    try:
        with open(input_file, "r", encoding="utf-8") as f:
            songs = f.readlines()

        # strip() elimina espacios al inicio y al final, incluyendo el salto de línea
        songs = [c.strip() for c in songs]

        songs.sort()

        with open(output_file, "w", encoding="utf-8") as f:
            for c in songs:
                f.write(c + "\n")

        print("Las canciones se han ordenado correctamente.")
    except FileNotFoundError:
        print("El archivo de entrada no existe.")
    except Exception as e:
        print("Ocurrió un error:", e)

sort_songs("canciones.txt", "canciones_ordenadas.txt")
