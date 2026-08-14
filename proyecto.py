# Factura de una papelería
# Ingresar el valor de los 10 productos
producto1 = float(input("Valor del producto 1: "))
producto2 = float(input("Valor del producto 2: "))
producto3 = float(input("Valor del producto 3: "))
producto4 = float(input("Valor del producto 4: "))
producto5 = float(input("Valor del producto 5: "))
producto6 = float(input("Valor del producto 6: "))
producto7 = float(input("Valor del producto 7: "))
producto8 = float(input("Valor del producto 8: "))
producto9 = float(input("Valor del producto 9: "))
producto10 = float(input("Valor del producto 10: "))

# Sumar los productos
subtotal = (producto1 + producto2 + producto3 + producto4 + producto5 + producto6 + producto7 + producto8 + producto9 + producto10)

# Calcular el IVA (19%)
iva = subtotal * 0.19
# Calcular el total
total = subtotal + iva
# Mostrar resultados
print("Subtotal:", subtotal)
print("IVA:", iva)
print("Total a pagar:", total)
