class BANCO():
    def __init__(self, Beneficiario,TipodeCuenta, NumerodeCuenta, SaldoDisponible, SaldoUtilizado ):
            #ATRIBUTOS
            self.Beneficiario= Beneficiario
            self.TipodeCuenta= TipodeCuenta
            self.__NumerodeCuenta= NumerodeCuenta
            self.SaldoDisponible= SaldoDisponible
            self.SaldoUtilizado= SaldoUtilizado

                #METODOS
    def EstadodeCuenta(self):
        print(self.Beneficiario, ":", sep="")
        print("Tiene una", self.TipodeCuenta)
        print("Con numero de cuenta", self.__NumerodeCuenta)
        print("Y su saldo disponible es", self.SaldoDisponible)
        print("Con un adeudo pendiente de", self.SaldoUtilizado)
        #ENCAPSULAMIENTO
def getNumerodeCuenta(self):
                print(self.__NumerodeCuenta)
       

class USUARIO1(BANCO):
    '''def cuenta(self):
            print("Cuenta")'''
    def __init__(self, Beneficiario,TipodeCuenta, NumerodeCuenta, SaldoDisponible, SaldoUtilizado ):
        self.Beneficiario= Beneficiario
        self.TipodeCuenta= TipodeCuenta
        self.__NumerodeCuenta= NumerodeCuenta#encapsular
        self.SaldoDisponible= SaldoDisponible
        self.SaldoUtilizado= SaldoUtilizado

        pass
            

            

    def EstadodeCuenta(self):
        print(self.Beneficiario, ":", sep="")
        print("Tiene una", self.TipodeCuenta)
        print("Con numero de cuenta", self.__NumerodeCuenta)
        print("Y su saldo disponible es", self.SaldoDisponible)
        print("Con un adeudo pendiente de", self.SaldoUtilizado)

                

class USUARIO2(BANCO):
    '''def cuenta(self):
            print("Cuenta")'''
    def __init__(self, Beneficiario, TipodeCuenta, NumerodeCuenta, SaldoDisponible, SaldoUtilizado ):
            
            self.Beneficiario= Beneficiario
            self.TipodeCuenta= TipodeCuenta
            self.__NumerodeCuenta= NumerodeCuenta#encapsular
            self.SaldoDisponible= SaldoDisponible
            self.SaldoUtilizado= SaldoUtilizado

            pass

    def EstadodeCuenta(self):
        print(self.Beneficiario, ":", sep="")
        print("Tiene una", self.TipodeCuenta)
        print("Con numero de cuenta", self.__NumerodeCuenta)
        print("Y su saldo disponible es", self.SaldoDisponible)
        print("Con un adeudo pendiente de", self.SaldoUtilizado)

                

class USUARIO3(BANCO):
    '''def cuenta(self):
            print("Cuenta")'''
    def __init__(self, Beneficiario, TipodeCuenta, NumerodeCuenta, SaldoDisponible, SaldoUtilizado ):
            
            self.Beneficiario= Beneficiario
            self.TipodeCuenta= TipodeCuenta
            self.__NumerodeCuenta= NumerodeCuenta
            self.SaldoDisponible= SaldoDisponible
            self.SaldoUtilizado= SaldoUtilizado

            pass

    def EstadodeCuenta(self):
        print(self.Beneficiario, ":", sep="")
        print("Tiene una", self.TipodeCuenta)
        print("Con numero de cuenta", self.__NumerodeCuenta)
        print("Y su saldo disponible es", self.SaldoDisponible)
        print("Con un adeudo pendiente de", self.SaldoUtilizado)
        

print('''
            BIENVENIDO AL BANCO KRIPTO
            INGRESE TU NIP PARA VER TU ESTADO DE CUENTA
            ''')
opcion=int(input())
print(f"TU NIP ES {opcion}")

if opcion==1:
            def DatosUsuario(usuario):
                pass

            
            personaje_1 = USUARIO1("FERNANDO", "CUENTA BASICA", 20560402, 3000, 7000)
            
            personaje_1.__NumerodeCuenta=10
            personaje_1.EstadodeCuenta()

            DatosUsuario(personaje_1)


            
elif opcion==2:
            def DatosUsuario(usuario):
                pass

            
           
            personaje_2 = USUARIO2("ALAN", "CUENTA EJECUTIVA",  20560105, 10000, 10000)
            
            personaje_2.EstadodeCuenta()

            DatosUsuario(personaje_2)
elif opcion==3:
            def DatosUsuario(usuario):
                pass

            
           
            personaje_3 = USUARIO3("JESUS", "CUENTA PREMIUM",  20560105, 50000, 20000)
            
            personaje_3.EstadodeCuenta()

            DatosUsuario(personaje_3)

            

           
            
else:
            print("Opcion invalida")
pass
