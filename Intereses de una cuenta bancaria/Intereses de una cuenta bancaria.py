def calcular_intereses(saldo, tasa_interes):
    """
    Calcula los intereses de una cuenta bancaria dado el saldo y la tasa de interés.
    """
    intereses = saldo * (tasa_interes / 100)
    return intereses

# Ejemplo de uso:
saldo_actual = 1000  # Saldo actual en la cuenta bancaria
tasa_interes_anual = 5  # Tasa de interés anual (en porcentaje)

intereses_generados = calcular_intereses(saldo_actual, tasa_interes_anual)
print("Los intereses generados son:", intereses_generados)
