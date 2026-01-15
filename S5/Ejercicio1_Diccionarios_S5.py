hotel = {
    "nombre": "Hotel Costa Azul",
    "numero_de_estrellas": 4,
    "habitaciones": [
        {
            "numero": 101,
            "piso": 1,
            "precio_por_noche": 75.0
        },
        {
            "numero": 203,
            "piso": 2,
            "precio_por_noche": 90.0
        },
        {
            "numero": 305,
            "piso": 3,
            "precio_por_noche": 120.0
        }
    ]
}

for habitacion in hotel["habitaciones"]:
    print("Habitación:", habitacion["numero"])
    print("Piso:", habitacion["piso"])
    print("Precio por noche:", habitacion["precio_por_noche"])
    print()
