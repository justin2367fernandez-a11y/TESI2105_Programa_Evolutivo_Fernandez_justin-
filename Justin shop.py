# ==============================================================================
# CURSO: TESI 2105 - Programación Orientada a Objetos
# LABORATORIO 2: Evolución del Programa Personal (Versión 2.0)
# ARCHIVO: programa_personal.py
# DESCRIPCIÓN: Programa personal con estructuras de control (while e if/else)
# ==============================================================================

# --- CONSTANTES (Se conservan de v1.0) ---
TASA_IMPUESTO = 0.115  # IVU de Puerto Rico (11.5%)

# --- ESTRUCTURA DE CONTROL 1: CICLO WHILE ---
# Permite repetir la tarea sin cerrar el programa
opcion_repetir = "si"

while opcion_repetir.lower() == "si":
    print("\n=== REGISTRO DE LOTE DE ROPA - VERSIÓN 2.0 ===")

    # --- ENTRADAS DE DATOS (Exactamente las mismas de v1.0) ---
    nombre_prenda = input("Ingrese el nombre/tipo de prenda: ")
    talla_prenda = input("Ingrese la talla (S, M, L, XL): ")
    precio_unitario = float(input("Ingrese el precio unitario ($): "))
    cantidad_unidades = int(input("Ingrese la cantidad de unidades: "))

    # --- PROCESAMIENTO INICIAL (Se conserva de v1.0) ---
    subtotal = precio_unitario * cantidad_unidades

    # --- ESTRUCTURA DE CONTROL 2: DECISIÓN IF / ELIF / ELSE ---
    # Aplica un descuento sencillo según la cantidad comprada
    if cantidad_unidades >= 20:
        descuento = subtotal * 0.10  # 10% de descuento si lleva 20 o más
    elif cantidad_unidades >= 10:
        descuento = subtotal * 0.05  # 5% de descuento si lleva 10 o más
    else:
        descuento = 0.0  # Sin descuento si lleva menos de 10

    # --- PROCESAMIENTO FINAL CON DESCUENTO ---
    subtotal_con_descuento = subtotal - descuento
    monto_impuesto = subtotal_con_descuento * TASA_IMPUESTO
    costo_total = subtotal_con_descuento + monto_impuesto

    # --- SALIDA DE DATOS ---
    print("\n" + "=" * 45)
    print("          RESUMEN DE COTIZACIÓN / LOTE        ")
    print("=" * 45)
    print(f"Prenda registrada : {nombre_prenda} (Talla: {talla_prenda})")
    print(f"Cantidad          : {cantidad_unidades} unidades")
    print(f"Precio Unitario   : ${precio_unitario:.2f}")
    print("-" * 45)
    print(f"Subtotal Inicial  : ${subtotal:.2f}")
    print(f"Descuento         : -${descuento:.2f}")
    print(f"Subtotal Ajustado : ${subtotal_con_descuento:.2f}")
    print(f"IVU / Impuesto    : ${monto_impuesto:.2f}")
    print(f"Costo Total       : ${costo_total:.2f}")
    print("=" * 45)

    # --- CONDICIÓN DE SALIDA DEL CICLO WHILE ---
    opcion_repetir = input("\n¿Desea cotizar otra prenda? (si/no): ")

print("\n¡Gracias por usar el programa!")
