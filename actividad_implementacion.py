#Crear una clase Student que tiene los siguientes atributos: name, age y grades (una lista de números)
#Crear un constructor que inicialice los atributos
class Student:
    def __init__(self, name, age, grades):
        self.name = name
        self.age = age
        self.grades = grades
#Crear un método llamado add_grade que recibe un número como parámetro y lo agrega a la lista grades.
    def add_grade(self, grade):
        self.grades.append(grade)
#Crear otro método llamado average_grade que calcule y retorne la nota promedio de la lista de notas grades
    def average_grade(self):
        return sum(self.grades) / len(self.grades)


# Crear una lista de diccionarios donde cada diccionario contiene la información de un estudiante.
estudiantes = [
    {"nombre": "Karim", "edad": 21, "grades": [91, 97, 99]},
    {"nombre": "Luka", "edad": 15, "grades": [72, 82, 74]},
    {"nombre": "Miguel", "edad": 18, "grades": [67, 78, 88]}
]

# Usar un list comprehension para crear una lista de objetos de la clase Student a partir de la lista de diccionarios.
students = [Student(inf["nombre"], inf["edad"], inf["grades"]) for inf in estudiantes]

#Usar otro list comprehension para filtrar los estudiantes, excluyendo los que tienen una nota promedio menor que un umbral dado.
umbral = 70
filtro = [student for student in students if student.average_grade() >= umbral]

filtro_encima = {student.nombre: student for student in estudiantes if student.average_grade() > umbral}