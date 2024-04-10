import random

def generar_calificacion_numerica():
    """
    Genera una calificación numérica aleatoria entre 0 y 100.
    """
    return random.randint(0, 100)

def convertir_a_calificacion_literal(calificacion):
    """
    Convierte una calificación numérica en una calificación literal.
    """
    if calificacion >= 90:
        return "A"
    elif calificacion >= 80:
        return "B"
    elif calificacion >= 70:
        return "C"
    elif calificacion >= 60:
        return "D"
    else:
        return "F"

# Generar una calificación numérica aleatoria
calificacion_numerica = generar_calificacion_numerica()

# Convertir la calificación numérica en una calificación literal
calificacion_literal = convertir_a_calificacion_literal(calificacion_numerica)

# Imprimir resultados
print("Calificación numérica generada:", calificacion_numerica)
print("Calificación literal correspondiente:", calificacion_literal)
