def crear_registro_estudiante(nombre, edad, promedio, activo):
  """Crea un diccionario que representa un registro de estudiante.
  Args:
    nombre: El nombre del estudiante (string).
    edad: La edad del estudiante (integer).
    promedio: El promedio académico del estudiante (float).
    activo: Indica si el estudiante está activo o no (boolean).
  Returns:
    Un diccionario con los datos del estudiante.
  """
  return {
    "nombre": nombre,
    "edad": edad,
    "promedio": promedio,
    "activo": activo
  }
def mostrar_registro_estudiante(registro):
  """Muestra la información de un registro de estudiante en pantalla.
    registro: Un diccionario que representa un registro de estudiante.
  """
  print(f"Nombre: {registro['nombre']}")
  print(f"Edad: {registro['edad']}")
  print(f"Promedio: {registro['promedio']}")
  print(f"Activo: {registro['activo']}")

# Crear un registro de estudiante
estudiante1 = crear_registro_estudiante("Juan Pérez", 18, 8.5, True)

# Mostrar la información del estudiante
mostrar_registro_estudiante(estudiante1)

