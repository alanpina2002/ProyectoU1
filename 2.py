class persona:
    #Atributos/Propiedades
    def __init__ (self, nombre, edad):
        self.__nombre = nombre
        self.__edad = edad


    def  set_nombre(self,nombre):
        self.__nombre=nombre
    def set_edad(self,edad):
        self.__edad = edad
        
        
    def get_nombre(self):
        return self.__nombre
    def get_nombre(self):
        return self.__edad
    
    
    def mostrar_persona(self):
        print(f'''
              
Nombre:{self.__nombre}
Edad: {self.__edad}''')
        
        
    def es_mayor_edad(self):
        print(f'{self.__nombre} es mayor de edad:') 
        print(self.__edad >= 18)

            
    def es_mayor_que(self):
        

        if self.__edad > 15:
            print(f'{self.__nombre} es mayor de 15 años de edad')
        else:
            print(f'{self.__nombre} es menor de 15 años de edad')
  
      
persona1=persona("Omar",21)
persona1.mostrar_persona()
persona1.es_mayor_edad()
persona1.es_mayor_que()

persona2=persona("Jesús",16)
persona2.mostrar_persona()
persona2.es_mayor_edad()
persona2.es_mayor_que()

