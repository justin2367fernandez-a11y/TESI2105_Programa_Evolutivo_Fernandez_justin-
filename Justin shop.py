# ==============================================================================
# CURSO: TESI 2105 - Programación Orientada a Objetos
# LABORATORIO 2: Evolución del Programa Personal (Versión 1.0)
# ARCHIVO: programa_personal.py
# DESCRIPCIÓN: Programa secuencial para el registro y cálculo del costo total
#              de un lote de prendas en un inventario/tienda de ropa.
# ==============================================================================

# --- CONSTANTES (Uso de mayúsculas según convención) ---
TASA_IMPUESTO = 0.115  # IVU de Puerto Rico (11.5%)

# --- ENTRADAS DE DATOS (input y conversiones) ---
print("=== REGISTRO DE LOTE DE ROPA - VERSIÓN 1.0 ===")

nombre_prenda = input("Ingrese el nombre/tipo de prenda: ")
talla_prenda = input("Ingrese la talla (S, M, L, XL): ")
precio_unitario = float(input("Ingrese el precio unitario ($): "))
cantidad_unidades = int(input("Ingrese la cantidad de unidades: "))

# --- PROCESAMIENTO (Cálculos matemáticos) ---
subtotal = precio_unitario * cantidad_unidades
monto_impuesto = subtotal * TASA_IMPUESTO
costo_total = subtotal + monto_impuesto

# --- SALIDA DE DATOS ---
print("\n" + "=" * 45)
print("          RESUMEN DE COTIZACIÓN / LOTE        ")
print("=" * 45)
print(f"Prenda registrada : {nombre_prenda} (Talla: {talla_prenda})")
print(f"Cantidad          : {cantidad_unidades} unidades")
print(f"Precio Unitario   : ${precio_unitario:.2f}")
print("-" * 45)
print(f"Subtotal          : ${subtotal:.2f}")
print(f"IVU / Impuesto    : ${monto_impuesto:.2f}")
print(f"Costo Total       : ${costo_total:.2f}")
print("=" * 45)
