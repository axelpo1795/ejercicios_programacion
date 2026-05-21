# Aplicación Gestor de Finanzas

## Estructura del Proyecto

src/
├── __init__.py          # Inicialización del paquete
├── main.py              # Punto de entrada de la ventana GUI principal
├── data_handler.py      # Clase DataHandler - maneja E/S de archivos y persistencia de datos
├── models.py            # Clases de modelo Transaction y Category
├── forms.py             # Formularios de diálogo (AddCategoryForm, AddExpenseForm, AddIncomeForm)
├── exceptions.py        # Archivo de notas (no utilizado)
├── test_logic.py        # Pruebas unitarias (16+ casos de prueba)
└── finance_data.json    # Archivo de datos (auto-generado)


## Descripción General de Módulos

### `main.py` - Clase MainWindow
El punto de entrada principal de la GUI. Contiene la clase `MainWindow` que:
- Muestra todas las transacciones en una tabla/cuadrícula
- Proporciona botones para agregar categorías, gastos e ingresos
- Muestra el cálculo de saldo en tiempo real
- Maneja operaciones de actualización y eliminación
- Gestiona el manejo de excepciones y retroalimentación del usuario

### `data_handler.py` - Clase DataHandler
Maneja toda la persistencia de datos y lógica comercial:
- Carga/guarda datos en `finance_data.json`
- Agrega transacciones y categorías
- Gestiona validación
- Calcula totales
- Maneja excepciones de E/S de archivos

### `models.py` - Clases Transaction y Category
Define los modelos de datos:
- `Transaction`: Representa transacciones individuales (ingreso o gasto)
- `Category`: Representa categorías de transacciones
- Ambas soportan serialización desde/hacia diccionarios

### `forms.py` - Formularios de Diálogo
Clases de diálogo separadas para cada tipo de formulario:
- `AddCategoryForm`: Diálogo para crear nuevas categorías
- `AddExpenseForm`: Diálogo para agregar gastos
- `AddIncomeForm`: Diálogo para agregar ingresos
- Cada uno maneja su propia validación

### `test_logic.py` - Pruebas Unitarias
Contiene 16+ casos de prueba unitaria utilizando el framework `unittest`:
- **Pruebas de Modelo**: Creación y serialización de categorías y transacciones
- **Pruebas de DataHandler**: Operaciones CRUD, validación, cálculo de saldos
- **Pruebas de Errores**: Validación de valores inválidos, duplicados, vacíos
- **Pruebas de Escenarios Complejos**: Presupuestos mensuales, múltiples fuentes de ingreso
- **Pruebas de Persistencia**: Guardado y carga de datos

## Características

**Arquitectura Modular** - Cada componente está separado por responsabilidad
**Diseño Basado en Clases** - Todo utiliza principios de POO
**Persistencia de Datos** - Guarda en archivo JSON automáticamente
**Manejo de Excepciones** - Valida entradas y maneja errores con excepciones estándar de Python
**Formularios de Diálogo** - Formularios separados para cada acción (no emergentes modales desordenados)
**Actualizaciones en Tiempo Real** - Botón de actualización y guardado automático
**Tabla de Transacciones** - Ver todas las transacciones ordenadas por fecha
**Cálculo de Saldo** - Calcula automáticamente el total con indicadores visuales (verde/rojo)


## Notas de Arquitectura

- **PySimpleGUI** proporciona el marco de la GUI
- **JSON** se utiliza para la persistencia de datos (fácil de leer/modificar)
- Todos los formularios son **clases separadas**, lo que permite reutilización y pruebas independientes
- Cada formulario maneja su propia **validación** antes de devolver datos
- **DataHandler** es la única fuente de verdad para operaciones de datos
- Se utilizan **excepciones estándar de Python** para el manejo de errores

## Pruebas

Para ejecutar las pruebas unitarias:
```bash
cd src
python -m unittest test_logic -v
```

Las pruebas cubren todos los casos principales y validan la lógica de negocio del aplicación.
