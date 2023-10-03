# Módulo para trabajar con el archivo txt.
import os
# Módulo para trabajar con fechas.
from datetime import datetime

# Clase padre, Contactos
class Contactos:
    def __init__(self, tipo, nombres, direccion, fecha):
        self.tipo = tipo
        self.nombres = nombres
        self.direccion = direccion
        self.fecha = fecha

    # Mostrar campos para ambos tipo
    def mostrarCampos(self):
        print(f"Datos necesarios para ambos tipos de contacto: \n{self.tipo} de contacto.\n{self.nombres}.\n{self.direccion}.\n{self.fecha} de nacimiento o fundación.")



# Subclase Persona
class Persona(Contactos):
    def __init__(self, tipo, nombres, apellidos, dni, direccion, fecha):
        super().__init__(tipo, nombres, direccion, fecha)
        self.apellidos = apellidos
        self.dni = dni

    # Mostrar campos para ambos tipos, y los específicos para persona
    def mostrarCampos(self):
        super().mostrarCampos()
        print(f"Para los contactos PERSONA, se necesitan tambien:\n{self.apellidos}.\n{self.dni}.")
    
    # Método para crear el contacto a partir del valor q tomen los atributos    
    def crearContacto(self):
        return f"\nTipo de contacto: {self.tipo}\nNombres: {self.nombres}\nApellidos: {self.apellidos}\ndni: {self.dni}\nDirección: {self.direccion}\nFecha de nacimiento: {self.fecha}\n"
    
    # Método para formatar el atributo fecha con datetime
    def diaNacimiento(self):
        fechaObj = datetime.strptime(self.fecha, "%Y-%m-%d")
        dia = datetime.strftime(fechaObj, "%A")
        print(f"El dia de la semana del nacimiento de {self.nombres} fue {dia}")



# Subclase Empresa
class Empresa(Contactos):
    def __init__(self, tipo, nombres, cuit, direccion, fecha):
        super().__init__(tipo, nombres, direccion, fecha)
        self.cuit = cuit
    
    # Mostrar campos para ambos tipos, y los específicos para empresa
    def mostrarCampos(self):
        super().mostrarCampos()
        print(f"En el caso de que agregues a tu agenda una EMPRESA, necesitarás contar tambien con su {self.cuit}.")
    
    # Método para crear el contacto a partir del valor q tomes los atributos
    def crearContacto(self):
        return f"\nTipo de contacto: {self.tipo}\nNombres: {self.nombres}\ncuit: {self.cuit}\nDirección: {self.direccion}\nFecha de fundación: {self.fecha}\n"
    
    # Método para formatar el atributo fecha con datetime
    def fechaFundación(self):
        fechaObj = datetime.strptime(self.fecha, "%Y-%m-%d")
        dia = datetime.strftime(fechaObj, "%A")
        mes = datetime.strftime(fechaObj, "%B")
        año = datetime.strftime(fechaObj, "%Y")
        print(f"La empresa {self.nombres} fue fundada el dia {dia} del mes de {mes} del año {año}.")



# Imprimir el título
def titulo():
     print(""" 
                    *****************
                    *    AGENDA     *
                    *   PERSONAL    *
                    *****************    
     """)

# Imprimir el saludo
def saludo():
     print(""" 
                    *****************
                    *    HASTA      *
                    *    LUEGO      *
                    *****************    
     """)

# Imprimir el menu
def menu():
    print("")
    print("Opciones:\n ")
    print("1: Grabar un contacto en la agenda.")
    print("2: Borrar un contacto en la agenda.")
    print("3: Extraer un contacto de la agenda y mostrar su información.")
    print("4: Crear e imprimir una lista de todos los contactos que sean personas.")
    print("5= Mostrar todos los contactos.")
    print("6= Borrar todos los contactos.")
    print("7: Salir.")

# Grabar un contacto en el archivo txt
def grabarContacto():
    with open("T.P.2a\data\contactos.txt", "a", encoding="utf-8") as f:
        try:   
            while True:
                tipoContacto = input("Ingrse el tipo de contacto PERSONA/EMPRESA: ").upper()
                if tipoContacto == "PERSONA":
                    nombresPersona = input("Nombre del contacto: ")
                    apellidosPersona= input("Apellido del contacto: ")
                    dniPersona = input("Ingrese el dni del contacto: ")
                    direccionPersona = input("Ingrese la dirección del contacto: ")
                    fechaPersona = input("Ingrese la fecha de nacimiento del contacto aaaa-mm-dd: ")
                    nuevoContactoPersona = Persona(tipo=tipoContacto,nombres=nombresPersona,apellidos=apellidosPersona,dni=dniPersona,direccion=direccionPersona,fecha=fechaPersona)
                    print("")
                    nuevoContactoPersona.diaNacimiento()
                    f.write(nuevoContactoPersona.crearContacto())
                    break 
                elif tipoContacto == "EMPRESA":
                    nombresEmprsa = input("Ingrese el nombre de la empresa: ")
                    cuitEmpresa = input("Ingrese el cuit de la empresa: ")
                    direccionEmpresa = input("Ingrese la dirección de la empresa: ")
                    fechaEmpresa = input("Ingrese la fecha de fundación de la empresa aaaa-mm-dd: ")
                    nuevoContactoEmpresa = Empresa(tipo=tipoContacto,nombres=nombresEmprsa,cuit=cuitEmpresa,direccion=direccionEmpresa,fecha=fechaEmpresa)
                    print("")
                    nuevoContactoEmpresa.fechaFundación()
                    f.write(nuevoContactoEmpresa.crearContacto())
                    break
                else:
                    print("")
                    print("Debe ingresar PERSONA o EMPRESA.")
                    print("")
        except:
            print("")
            print("Fecha mal ingresada. aaaa-mm-dd.")
            print("")
            input("Presione enter para volver al menu: ")

# Mostrar todos los contactos
def mostrarContactos():
    # Abrir archivo
    with open ("T.P.2a\data\contactos.txt", "r", encoding="utf-8") as f:
        contactos = f.read()
        print(contactos)
    input("Presione enter para volver al menu: ")

# Mostras solo los contactos PERSONA
def mostrarContactoPersonas():
   with open ("T.P.2a\data\contactos.txt", "r", encoding="utf-8") as f:
        contador = 0
        coto = 0
        lineas = f.readlines()
        for linea in lineas:
            coto += 1
            if f"Tipo de contacto: PERSONA" in linea:
               contador += 1
               contactoPersona = lineas[coto-1:coto+5]
               print("\n",*contactoPersona)
        input("Presiona enter para volver al menú: ")
        if contador == 0:
            print("No tienes contactos PERSONA.")
            print("")
            input("Presiona enter para volver al menú: ")

# Mostrar un contacto en específico
def mostrarContacto():
    with open ("T.P.2a\data\contactos.txt", "r", encoding="utf-8") as f:
        contador = 0
        coto = 0
        contactoSeleccionado = []
        identificador = input("Ingrese el dni o cuit del contacto a mostrar: ")
        lineas = f.readlines()
        for linea in lineas:
            coto += 1
            if f"dni: {identificador}" in linea: 
                contador = 1
                contactoSeleccionado = lineas[coto-4:coto+3]
                print("\n",*contactoSeleccionado)
                input("Presione enter para continuar")
                break
            elif f"cuit: {identificador}" in linea:
                contador = 1
                contactoSeleccionado = lineas[coto-3:coto+3]
                print("\n",*contactoSeleccionado)
                input("Presione enter para continuar")
                break
        if contador == 0:
            print("\nNo existe un contacto con ese dni/cuit.")
            print("")
            input("Presione enter para continuar")
# Borrar un contacto   
def borrarContacto():
    f = open("T.P.2a\data\contactos.txt", "r", encoding="utf-8")
    contador = 0
    coto = 0
    contactoSeleccionado = []
    identificador = input("Ingrese el dni o cuit del contacto a borrar: ")
    lineas = f.readlines()
    for linea in lineas:
        coto += 1
        if f"dni: {identificador}" in linea:
            contador = 1
            contactoSeleccionado = lineas[coto-5:coto+2]
            print("")
            print("Contacto a elimenar: ")
            print(*contactoSeleccionado)
            print("")
            while True:
                confirma = input("Conforma la eliminación de este contacto? si/no: ").lower()
                if confirma == "si":
                    del lineas[coto-5:coto+2]
                    break
                elif confirma == "no":
                    break
                else:
                    print("")
                    print("Debe ingrsar si/no.")
                    print("")
        elif f"cuit: {identificador}" in linea:
            contador = 1
            contactoSleccionado =lineas[coto-4:coto+2]
            print("")
            print("Contacto a eliminar: ")
            print(*contactoSleccionado)
            print("")
            while True:
                confirma = input("Confirma la eliminación de este contacto? si/no: ").lower()
                if confirma == "si":
                    del lineas[coto-4:coto+2]
                    break
                elif confirma == "no":
                    break
                else:
                    print("")
                    print("Debe ingrsar si/no.")
                    print("")
    if contador == 0:
        print("\nNo existe un contacto con ese dni/cuit.")
        print("")
        input("Presione enter para volver al menu: ")
    f.close()
    f = open("T.P.2a\data\contactos.txt", "w", encoding="utf-8")
    f.truncate()
    f.writelines(lineas)
    f.close() 

# Borrar todo el txto del archivo txt
def borrarTodosLosContactos():
    f = open("T.P.2a\data\contactos.txt", "w", encoding="utf-8")
    print("Vas a borrar todos tus contactos")
    while True:
        confirma = input("\nComfirna si/no: ")
        if confirma == "si":
            f.truncate()
            break
        elif confirma == "no":
            break
        else:
            print("\nDebes ingresar si/no.")



################################################################################################

titulo()
print("Que quieres hacer?\n")
while True:
    menu()
    seleccion = input("\nIngrese la opción a realizar 1/7: ")
    print("")
    if seleccion == "1":
        grabarContacto()
    elif seleccion == "2":
        borrarContacto()
    elif seleccion == "3":
        mostrarContacto() 
    elif seleccion == "4":
        mostrarContactoPersonas()
    elif seleccion == "5":
        mostrarContactos()
    elif seleccion == "6":
        borrarTodosLosContactos()
    elif seleccion == "7":
        break
    else:
        print("Opción incorrecta.")
    
