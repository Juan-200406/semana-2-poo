class Personaje:                                                   
   def __init__(self, nombre, raza, clase):                      
       self.nombre = nombre                                      
       self.raza = raza                                          
       self.claseclass = clase                                   
       self.nivel = 1                                            
       print(f"El personaje {nombre} ha sido creado.")           
                                                                 
   def subir_nivel(self):                                         
       # Lógica para subir de nivel                              
       self.nivel += 1                                           
       print(f"{self.nombre} ha subido al nivel {self.nivel}!")  
                                                                 
   def __del__(self):                                            
       print(f"El personaje {self.nombre} ha sido eliminado.")   
personaje1 = Personaje("scooby doo", "perro", "mamifero")         
personaje1.subir_nivel()                                          
print(personaje1.subir_nivel())                                   
                                                                 
                                                                         