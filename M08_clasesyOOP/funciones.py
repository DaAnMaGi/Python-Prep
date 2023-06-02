# funciones.py

class Funciones_lista:

    def __init__(self,lista):
        if (type(lista) != list):
           self.lista = []
           raise ValueError('Se ha creado una lista vacía. Se esperaba una lista de núemeros enteros')  
        else:
           self.lista = lista
    
    def primos_lista(self):
        primos = []
        no_primos = []
        if (1) in self.lista:
            primos.append((1))
        if (2) in self.lista:
            primos.append(2)
        for i,e in enumerate(self.lista):
            if self.__es_primo(e) == True:
                primos.append(e)
            else: 
                no_primos.append(e)
        return print(f"son primos los siguentes: {primos}"), print(f"No son primos los siguientes {no_primos}")
    
    def factorial_lista(self):
        for i in self.lista:
            print(f"el factorial de {i} es {self.__factorial(i)}")
    
    def grados_lista(self,origen,destino):
        parametros_esperados = ["C","F","K"]
        lista_conversion = []
        
        if str(origen) not in parametros_esperados:
            print(f"{origen} no cumple con los parámetros esperados. Estos son 'C' para Celcius, 'K' para Kelvin y 'F' para Farenheit")
        if str(destino) not in parametros_esperados:
            print(f"{destino} no cumple con los parámetros esperados.Los parámetros esperados son 'C' para Celcius, 'K' para Kelvin y 'F' para Farenheit")
        for i in self.lista:
            lista_conversion.append(self.__conversion(i,origen,destino))
            return lista_conversion

    def __es_primo(self,numero):
        primo = True
        for i in range(2,numero):
            if numero%i == 0:
                primo = False
                break
            return primo
        
    def modal(self,datomenorrequerido=False):
        unicos = [] 
        repetidos = []
        if len(self.lista) == 0:
            return None 
        for e in self.lista:
            if e in unicos:
                i = unicos.index(e) 
                repetidos[i] +=1 
            else:
                unicos.append(e) 
                repetidos.append(1)
        moda = unicos[0]
        maximo = repetidos[0] 
        menor = repetidos[0] 
        if datomenorrequerido == True: 
            for i,e in enumerate(unicos):
                if repetidos[i] > 1:
                    if repetidos[i] < menor: 
                        moda = unicos[i]
                        menor = repetidos[i]
            return print(f"El dato {moda} es, de los datos que se repiten, el que menos lo hace, con {menor} repeticiones")
        else:
            for i,e in enumerate(unicos):
                if repetidos[i] > maximo:
                    moda = unicos[i]
                    maximo = repetidos[i]
            return print(f"El número {moda} es el que más se repite, con {maximo} repeticiones")
        
    def __conversion(self,valor,origen,destino):
        if origen == "C":
            if destino == "K":
                r = valor + 273.15
                return r
            elif destino == "F":
                r = (valor * 9/5) + 32
                return r
            elif destino == "C":
                r = valor
                return r
        elif origen == "K":
            if destino == "C":
                r = valor - 273.15
                return r
            elif destino == "F":
                r = (self.__conversion(valor,origen,"C")* 9/5) + 32
                return r
            elif destino == "K":
                r = valor
                return r
        elif origen == "F":
            if destino == "C":
                r = (valor - 32) * 5/9
                return r
            elif destino == "K":
                r = (self.__conversion(valor,origen,"C")) - 273.15
                return r
            elif destino == "F":
                r = valor
                return r
        else: print("No se puede convertir")

    def __factorial (self,numero):
        if numero < 0:
            print("El número es negativo, no se puede factorizar")
        elif type(numero) == int:
            if numero > 1: 
                numero = numero * self.__factorial(numero-1)
            return numero
        else: print("El número no es un entero")

class Funciones:
    def __init__(self) -> None:
        pass
    
    def es_primo(self,numero):
        primo = True
        for i in range(2,numero):
            if numero%i == 0:
                primo = False
                break
            return primo
        
    def modal(self,lista,datomenorrequerido=False):
        unicos = [] 
        repetidos = []
        if len(lista) == 0:
            return None 
        for e in lista:
            if e in unicos:
                i = unicos.index(e) 
                repetidos[i] +=1 
            else:
                unicos.append(e) 
                repetidos.append(1)
        moda = unicos[0]
        maximo = repetidos[0] 
        menor = repetidos[0] 
        if datomenorrequerido == True: 
            for i,e in enumerate(unicos):
                if repetidos[i] > 1:
                    if repetidos[i] < menor: 
                        moda = unicos[i]
                        menor = repetidos[i]
            return print(f"El dato {moda} es, de los datos que se repiten, el que menos lo hace, con {menor} repeticiones")
        else:
            for i,e in enumerate(unicos):
                if repetidos[i] > maximo:
                    moda = unicos[i]
                    maximo = repetidos[i]
            return print(f"El número {moda} es el que más se repite, con {maximo} repeticiones")
        
    def conversion(self,valor,origen,destino):
        if destino == "C":
            if origen == "K":
                r = valor - 273.15
                return r
            elif origen == "F":
                r = (valor - 32) * 5/9
                return r
            elif origen == "C":
                r = valor
                return r
        elif destino == "K":
            if origen == "C":
                r = valor + 273.15
                return r
            elif origen == "F":
                r = self.conversion(valor,"F","C") + 273.15
                return r
            elif origen == "K":
                r = valor
                return r
        elif destino == "F":
            if origen == "C":
                r = (valor * 9/5) + 32
                return r
            elif origen == "K":
                r = (self.conversion(valor,"K","C")* 9/5) + 32
                return r
            elif origen == "F":
                r = valor
                return r
        else: print("No se puede convertir")

    def factorial (self,numero):
        if numero < 0:
            print("El número es negativo, no se puede factorizar")
        elif type(numero) == int:
            if numero > 1: 
                numero = numero * self.factorial(numero-1)
            return numero
        else: print("El número no es un entero")