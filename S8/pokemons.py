import json

FILE_NAME = "pokemons.json"

def load_pokemons():
    try:
        with open(FILE_NAME, "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        print("Error: el archivo JSON está dañado.")
        return []

def save_pokemons(pokemons):
    with open(FILE_NAME, "w", encoding="utf-8") as file:
        json.dump(pokemons, file, indent=2, ensure_ascii=False)

def get_int_input(message):
    while True:
        try:
            return int(input(message))
        except ValueError:
            print("Error: debe ingresar un número entero.")

def print_pokemons(pokemons):
    if len(pokemons) == 0:
        print("No hay Pokémon registrados.")
        return

    for i, pokemon in enumerate(pokemons, start=1):
        print(f"\nPokémon #{i}")
        print(f"Nombre: {pokemon['name']['english']}")
        print(f"Tipos: {', '.join(pokemon['type'])}")
        print("Estadísticas:")
        for stat, value in pokemon["base"].items():
            print(f"  {stat}: {value}")

def create_pokemon():
    name = input("Nombre del Pokémon: ")

    types = []
    while True:
        pokemon_type = input("Ingrese un tipo (ENTER para terminar): ")
        if pokemon_type == "":
            if len(types) == 0:
                print("Debe ingresar al menos un tipo.")
            else:
                break
        else:
            types.append(pokemon_type)

    base_stats = {
        "HP": get_int_input("HP: "),
        "Attack": get_int_input("Attack: "),
        "Defense": get_int_input("Defense: "),
        "Sp. Attack": get_int_input("Sp. Attack: "),
        "Sp. Defense": get_int_input("Sp. Defense: "),
        "Speed": get_int_input("Speed: ")
    }

    return {
        "name": {
            "english": name
        },
        "type": types,
        "base": base_stats
    }

def show_menu():
    print("\n--- MENÚ POKÉMON ---")
    print("1. Mostrar Pokémon existentes")
    print("2. Agregar nuevo Pokémon")
    print("3. Salir")

def main():
    while True:
        show_menu()
        option = input("Seleccione una opción: ")

        if option == "1":
            pokemons = load_pokemons()
            print_pokemons(pokemons)

        elif option == "2":
            pokemons = load_pokemons()
            new_pokemon = create_pokemon()
            pokemons.append(new_pokemon)
            save_pokemons(pokemons)
            print("Pokémon guardado correctamente.")

        elif option == "3":
            print("Saliendo del programa.")
            break

        else:
            print("Opción inválida. Intente de nuevo.")

if __name__ == "__main__":
    main()
