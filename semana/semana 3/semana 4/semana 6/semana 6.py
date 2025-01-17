class pais:
    def __init__(self,_pais):
        self._pais=_pais
class capital(pais):
    def __init__(self ,_pais, _capital):
        super().__init__(_pais)
        self._capital=_capital
    def nombre_capital(self):
        return (f"la capital de {self._pais} es {self._capital}")

#ejemplo de polimofismo
class ciudades(capital):
    def __init__(self,_pais,_capital,_ciudad):
        super().__init__(_pais,_capital)
        self._ciudad=_ciudad

    def nombre_ciudad(self):
        return (f"la ciudad de {self.nombre_capital()} es {self._ciudad}")

__pais =pais("ecuador")
print(__pais._pais)

__capital =capital("colombia","capital")
print(__capital.nombre_capital())
__ciudad=ciudades("peru" ,"lima" ,"cusco")
print(__ciudad.nombre_ciudad())