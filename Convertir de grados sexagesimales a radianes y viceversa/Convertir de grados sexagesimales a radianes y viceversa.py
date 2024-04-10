import math

def grados_a_radianes(grados):
    """
    Convierte grados sexagesimales a radianes.
    """
    return (grados * math.pi) / 180

def radianes_a_grados(radianes):
    """
    Convierte radianes a grados sexagesimales.
    """
    return (radianes * 180) / math.pi

# Pedir al usuario que ingrese los grados
grados_usuario = float(input("Ingrese los grados a convertir: "))

# Convertir grados a radianes
radianes_convertidos = grados_a_radianes(grados_usuario)
print(f"{grados_usuario} grados = {radianes_convertidos} radianes")

# Pedir al usuario que ingrese los radianes
radianes_usuario = float(input("Ingrese los radianes a convertir: "))

# Convertir radianes a grados
grados_convertidos = radianes_a_grados(radianes_usuario)
print(f"{radianes_usuario} radianes = {grados_convertidos} grados")
