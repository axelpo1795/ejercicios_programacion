# Gestor de Finanzas - Guía Rápida de Instalación y Ejecución


## Estructura del Proyecto

S18 Python Project/
├── src/
│   ├── main.py              # Punto de entrada GUI principal
│   ├── data_handler.py      # Capa de persistencia de datos
│   ├── models.py            # Clases Transaction y Category
│   ├── forms.py             # Ventanas de diálogo
│   ├── exceptions.py        # Archivo de notas (no utilizado)
│   ├── test_logic.py        # Pruebas unitarias (16+ casos)
│   └── finance_data.json    # Almacenamiento de datos (auto-creado)
└── README.md                # Documentación

### Componentes Principales

**MainWindow** (main.py)
- Interfaz GUI principal con tabla de transacciones
- Maneja clics de botones e interacciones del usuario
- Visualización de saldo en tiempo real con código de colores

**DataHandler** (data_handler.py)
- Gestiona todas las operaciones de datos (CRUD)
- Maneja entrada/salida con JSON
- Persistencia automática de datos
- Lógica de validación

**Models** (models.py)
- `Transaction`: Representa entradas de ingreso/gasto
- `Category`: Representa categorías de transacciones
- Serialización automática a/desde JSON

**Forms** (forms.py)
- Clases de diálogo separadas para cada operación
- Lógica de validación independiente
- Componentes de formulario reutilizables

**Exceptions** (exceptions.py)
- Jerarquía de excepciones personalizada
- Manejo de errores específico para diferentes e
## Características Implementadas

**Arquitectura modular basada en clases**
- Módulos separados para cada responsabilidad
- Fácil de extender y mantener

**Persistencia de datos**
- Guardado automático en finance_data.json
- Carga al iniciar

**GUI con tabla de transacciones**
- Vista de tabla PySimpleGUI
- Muestra: Detalle, Categoría, Monto (con +/-), Tipo, Fecha
- Visualización de saldo en tiempo real

**Cuatro operaciones principales**
- Agregar Categoría (con protección contra duplicados)
- Agregar Gasto (con validación)
- Agregar Ingreso (con validación)
- Eliminar Transacción

**Manejo de excepciones**
- Advertencia de sin categorías
- Validación de cantidad inválida
- Manejo de errores de E/S de archivos
- Mensajes de error amigables

**Formularios como clases separadas**
- `AddCategoryForm`: Crear nueva categoría
- `AddExpenseForm`: Agregar gasto con validación
- `AddIncomeForm`: Agregar ingreso con validación
- Cada formulario maneja su propia validación

## Ejemplos de Uso

### Agregar una Categoría
1. Haz clic en "Agregar Categoría"
2. Ingresa el nombre de la categoría (ej: "Comida", "Transporte")
3. Haz clic en "Crear"

### Agregar un Gasto
1. Haz clic en "Agregar Gasto"
2. Ingresa el detalle (ej: "Compra en supermercado")
3. Selecciona una categoría del menú desplegable
4. Ingresa el monto
5. Haz clic en "Agregar"

### Agregar un Ingreso
1. Haz clic en "Agregar Ingreso"
2. Ingresa el detalle (ej: "Pago de trabajo")
3. Selecciona una categoría
4. Ingresa el monto
5. Haz clic en "Agregar"

### Eliminar una Transacción
1. Selecciona una fila en la tabla de transacciones
2. Haz clic en "Eliminar Seleccionado"

### Calcular Total
- El saldo se muestra automáticamente en la parte inferior
- Verde = positivo (ingreso > gasto)
- Rojo = negativo (gasto > ingreso)

## Formato del Archivo de Datos

La aplicación almacena datos en formato JSON:
```json
{
    "transactions": [
        {
            "detail": "Compra en supermercado",
            "category": "Comida",
            "amount": 45.50,
            "transaction_type": "gasto",
            "date": "2026-05-01"
        }
    ],
    "categories": [
        {
            "name": "Comida",
            "category_id": "..."
        }
    ]
}
```

## Manejo de Errores

La aplicación maneja:
- Sin categorías al agregar transacción
- Montos no numéricos
- Operaciones de archivo inválidas
- Categorías duplicadas
- Campos vacíos

## Desarrollo

### Agregar Nuevas Características

1. **Nuevo Formulario**: Crea una clase en `forms.py` heredando de la base apropiada
2. **Nueva Operación**: Añade un método a `MainWindow` y un botón en el diseño
3. **Nuevo Campo de Datos**: Actualiza `models.py` y `data_handler.py`

## Ejecución de Pruebas

Para ejecutar las pruebas unitarias:
```bash
cd src
python -m unittest test_logic -v
```

Las pruebas incluyen 16+ casos cubriendo:
- Creación de categorías
- Creación de transacciones (ingreso y gasto)
- Cálculo de saldos
- Persistencia de datos
- Validación de errores
- Escenarios complejos

## Notas

- Todos los datos se almacenan localmente en `finance_data.json`
- La aplicación está completamente basada en clases y es modular
- Los formularios son clases separadas, no incrustados en la ventana principal
- Fácil de extender con nuevas características
- La moneda utilizada es el Colón (₡)
