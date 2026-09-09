# ==========================================
# Programa: Panadería La Espiga v2.0
# Estudiante: Justin Kane Fernandez Ramos
# Curso: TESI 2105 - Programación Orientada a Objetos
# ==========================================

MENU = {"Pan": 0.50, "Croissant": 1.50, "Pastel": 12.00, "Café": 2.00}
IVA = 0.16  # 16% de impuesto

print("--- PANADERÍA LA ESPIGA (v2.0) ---")
# Ciclo for para mostrar el menú disponible
for producto, precio in MENU.items():
    print(f"- {producto}: ${precio:.2f}")

# Simulación de pedido mediante diccionario
compra = {"Pan": 6, "Croissant": 2, "Café": 1}

# Ciclo con acumulación para calcular subtotal
subtotal = sum(MENU[item] * cantidad for item, cantidad in compra.items())

# Decisiones (Estructura condicional if/else)
# Si la compra supera los $10.00, se otorga un 10% de descuento sobre el subtotal
if subtotal > 10.00:
    descuento = subtotal * 0.10
    subtotal_con_descuento = subtotal - descuento
    print(f"\n🎉 ¡Aplica descuento del 10%! (-${descuento:.2f})")
else:
    descuento = 0.00
    subtotal_con_descuento = subtotal

impuesto = subtotal_con_descuento * IVA
total = subtotal_con_descuento + impuesto

# Generación del ticket con ciclo for
print("\n--- TICKET DE VENTA ---")
for item, cantidad in compra.items():
    costo = MENU[item] * cantidad
    print(f"{cantidad}x {item:<10} ${costo:.2f}")

print("-" * 23)
print(f"Subtotal:     ${subtotal:.2f}")
if descuento > 0:
    print(f"Descuento:   -${descuento:.2f}")
print(f"IVA (16%):    ${impuesto:.2f}")
print(f"TOTAL:        ${total:.2f}")
