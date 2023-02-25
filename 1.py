class persona:
    #Atributos/Propiedades
    def inicializar(self, nombre, edad, DNI):
        self.nombre = nombre
        self.edad = edad
        self.DNI = DNI

    def imprimir(self):
        print("nombre:",self.nombre)
        print("edad:",self.edad)
        print("DNI:",self.DNI)

    def mayor_edad(self):
        if self.edad >= 18:
            print("es mayor de edad")
        else:
            print("no es mayor de edad")

persona1=persona()
persona1.inicializar("ALAN",20,20560451)
persona2=persona()
persona2.inicializar("FERNANDO",16,20560151)
persona1.imprimir()
persona1.mayor_edad()
persona2.imprimir()
persona2.mayor_edad()
