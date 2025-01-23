class Emergencia:
    def __init__(self, paciente, muy_grave, grave, estable):
        self.paciente = paciente
        self.muy_grave = muy_grave
        self.grave = grave
        self.estable = estable

    def determinar_categoria(self):
        if self.paciente == self.muy_grave:
            return "rojo"
        elif self.paciente  == self.grave:
            return "amarillo"
        else:
            return "verde"

class Atencion:
    def __init__(self, categoria):
        self.categoria = categoria

    def asignar_atencion(self):
        if self.categoria == "rojo":
            print("Necesita un cirujano")
        elif self.categoria == "amarillo":
            print("Necesita un doctor")
        else:
            print("Necesita hacer unos exámenes")

# Crear una instancia de Emergencia
emergencia1 = Emergencia("Juan", 8, 6, 4)

# Determinar la categoría y crear una instancia de Atención
categoria = emergencia1.determinar_categoria()
atencion1 = Atencion(categoria)

# Asignar la atención
atencion1.asignar_atencion()
