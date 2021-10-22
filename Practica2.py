

#Ejercicio 1
import string
lower=list(string.ascii_lowercase)
upper=list(string.ascii_uppercase)

#Class definition
class Grupos:
    def __init__(self,name,sex,grupo):
       self.name=name
       self.sex=sex
       self.grupo=grupo
    def printname(self,name,sex,grupo):
        print("Nombre: ",self.name,", ","Sexo: ",self.sex," => ","Grupo ",self.grupo)


#Parameters input
name=(input("Ingrese su nombre "))
sex=(input("Ingrese su sexo "))
if sex=="Mujer":
    if name[0] in lower[0:12] or name[0] in upper[0:12]:
        grupo="A"
    else:
        grupo="B"
    Test1=Grupos(name,sex,grupo)
    Test1.printname(name,sex,grupo)
elif sex=="Hombre":
    if name[0] in lower[14:26] or name[0] in upper[14:26]:
        grupo="A"
    else:
        grupo="B"
    Test1=Grupos(name,sex,grupo)
    Test1.printname(name,sex,grupo)
else:
    print("Ingrese Hombre/Mujer")



##Ejercicio 2

class Producto:
    def __init__(self,codigo,nombre,precio,departamento):
        self.codigo=codigo
        self.nombre=nombre
        self.precio=precio
        self.departamento=departamento
    def Presentacion(self):
        mensaje=input("Ingrese mensaje del producto ")
        print(self.nombre,mensaje)
    def Calculadora(self):
        cantidad=input("Ingrese cantidad ")
        print("Resultado ",int(self.precio)*int(cantidad))


x=Producto(1,"Ketchup",12,"ByB")
x.Presentacion()
x.Calculadora()