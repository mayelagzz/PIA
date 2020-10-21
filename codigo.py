listaEstudiantes = []

class Estudiantes(object):
    def __init__ (self, nombre, apellido, matricula):
        self.nombre = nombre
        self.apellido = apellido
        self.matricula = matricula 
        self.historial = []
    def entregarDatos(self):
        print(self.nombre, self.apellido, self.matricula)

def registrarEstudiante():
    print("Registro de Estudiante")
    nombre = input("Ingrese el nombre: ")
    apellido = input("Ingrese el apellido: ")
    matricula = int(input("Ingrese el numero de matricula: "))
    objAlumno = Estudiantes(nombre, apellido, matricula)
    listaEstudiantes.append(objAlumno)

def listadoEstudiantes():
    print("Listado de Estudiantes")
    for objAlumno in listaEstudiantes:
        objAlumno.entregarDatos()

def salir():
    print("Saliendo! ...")
    exit()

def main():
    while True:
        print("¡B I E N V E N I D O!")
        print("")
        print("Seleccione una de las siguuientes opciones: ")
        print("")
        print("1.-Registrar al Estudiante")
        print("2.-Mostrar a los Estudiantes")
        print("3.-Salir")

        opcion = int(input("Opcion: "))

        if opcion == 1:
            registrarEstudiante()
        elif opcion == 2:
            listadoEstudiantes()
        elif opcion == 3:
            salir()
if __name__ == "__main__":
    main()