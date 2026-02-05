# Definimos el nombre de la tienda como una constante
TIENDA = "La Tienda Pulenta"

# 1. ESTRUCTURA DE DATOS
inventario = [
    {"nombre": "Monitor 24'", "precio": 150.0, "cantidad": 10, "categoria": "Monitor"},
    {"nombre": "Teclado Mecanico", "precio": 45.0, "cantidad": 3, "categoria": "Teclado"},
    {"nombre": "Mouse Gamer", "precio": 25.0, "cantidad": 12, "categoria": "Mouse"},
    {"nombre": "Audifonos BT", "precio": 60.0, "cantidad": 2, "categoria": "Audio"},
    {"nombre": "Webcam HD", "precio": 35.0, "cantidad": 7, "categoria": "Video"}
]

# 2. INGRESO DE DATOS
print(f"\n--- Bienvenido al sistema de {TIENDA} ---")
print("Registro de Nuevo Producto:")

nombre_p = input("Nombre del producto: ")
# Recuerda ingresar solo números en precio y cantidad para evitar el ValueError
precio_p = float(input("Precio: ")) 
cant_p = int(input("Cantidad: "))
cat_p = input("Categoria: ")

nuevo = {"nombre": nombre_p, "precio": precio_p, "cantidad": cant_p, "categoria": cat_p}
inventario.append(nuevo)

# 3. PROCESAMIENTO Y LÓGICA
print(f"\n--- Estado del Inventario en {TIENDA} ---")
valor_total_stock = 0

for producto in inventario:
    aviso = ""
    if producto["cantidad"] < 5:
        aviso = " - ADVERTENCIA: Stock Bajo"
    
    print(f"Producto: {producto['nombre']}{aviso}")
    print(f"Precio: ${producto['precio']} | Stock: {producto['cantidad']}")
    print("-" * 40)
    
    valor_total_stock += (producto["precio"] * producto["cantidad"])

print(f"VALOR TOTAL DEL INVENTARIO: ${valor_total_stock}")

# 4. BÚSQUEDA
print(f"\n--- Buscador de {TIENDA} ---")
busqueda = input("¿Qué producto buscas hoy?: ")
encontrado = False

for producto in inventario:
    if producto["nombre"].lower() == busqueda.lower():
        print(f"\n¡Producto Encontrado!")
        print(f"Detalles: {producto}")
        encontrado = True
        break 

if not encontrado:
    print(f"\nEl producto no está en el stock de {TIENDA}.")

print(f"\nGracias por usar el sistema de {TIENDA}. ¡Vuelva pronto!")