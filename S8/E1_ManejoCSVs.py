import csv

games_list = []

game_headers = (
    'name',
    'genre',
    'developer',
    'esrb_rating',
)

def write_csv_file(file_path, data, headers):
    try:
        with open(file_path, 'w', encoding='utf-8', newline='') as file:
            writer = csv.DictWriter(file, headers)
            writer.writeheader()
            writer.writerows(data)
        print("Archivo CSV creado correctamente.")
    except Exception as error:
        print("Ocurrió un error al escribir el archivo CSV:", error)

def fill_games_list():
    try:
        amount = int(input("¿Cuántos videojuegos desea ingresar? "))
    except ValueError:
        print("Debe ingresar un número entero.")
        return

    for i in range(amount):
        print(f"\nVideojuego #{i+1}")
        try:
            name = input("Nombre: ")
            genre = input("Género: ")
            developer = input("Desarrollador: ")
            esrb_rating = input("Clasificación ESRB: ")

            game = {
                'name': name,
                'genre': genre,
                'developer': developer,
                'esrb_rating': esrb_rating,
            }

            games_list.append(game)

        except Exception as error:
            print("Ocurrió un error al recibir los datos del videojuego:", error)

    try:
        write_csv_file('video_games.csv', games_list, game_headers)
    except Exception as error:
        print("Ocurrió un error inesperado:", error)

fill_games_list()
