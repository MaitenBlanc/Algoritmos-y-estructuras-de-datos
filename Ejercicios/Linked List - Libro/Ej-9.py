"""Se tiene una lista de los alumnos de un curso, de los que se sabe nombre, apellido y legajo.
Por otro lado se tienen las notas de los diferentes parciales que rindió cada uno de ellos con
la siguiente información: materia que rindió, nota obtenida y fecha de parcial. Desarrollar un
algoritmo que permita realizar la siguientes actividades:
a. mostrar los alumnos ordenados alfabéticamente por apellido;
b. indicar los alumnos que no desaprobaron ningún parcial;
c. determinar los alumnos que tienen promedio mayor a 8,89;
d. mostrar toda la información de los alumnos cuyos apellidos comienzan con L;
e. mostrar el promedio de cada uno de los alumnos;
f. mostrar todos los alumnos que rindieron la cátedra “Algoritmos y estructuras de datos”;
g. indicar el porcentaje de parciales aprobados de un alumno indicado por el usuario;
h. indicar cuantos alumnos aprobaron y desaprobaron parciales de la cátedra “Base de datos”;
i. mostrar todos los alumnos que rindieron en el año 2020;
j. debe modificar el TDA para implementar lista de lista."""

import sys

sys.path.append("./Clases")
from lista_enlazada import List


class Student:
    def __init__(self, name, last_name, file):
        self.name = name
        self.last_name = last_name
        self.file = file
        self.notes = List()


class Notes:
    def __init__(self, subject, note, date):
        self.subject = subject
        self.note = note
        self.date = date  # Formato: YYYY-MM-DD


students_list = List()

# Cargar datos
notas_juan = List(
    [
        Notes("Algoritmos y estructuras de datos", 9, "2020-05-12"),
        Notes("Base de datos", 8, "2020-09-01"),
    ]
)

notas_maria = List(
    [
        Notes("Matemática Discreta", 7, "2021-03-10"),
        Notes("Base de datos", 5, "2021-07-15"),
    ]
)

notas_lucas = List(
    [
        Notes("Algoritmos y estructuras de datos", 10, "2021-11-05"),
        Notes("Base de datos", 10, "2020-12-01"),
    ]
)

students_list.extend(
    [
        [Student("Juan", "González", 101), notas_juan],
        [Student("María", "Fernández", 102), notas_maria],
        [Student("Lucas", "Ledesma", 103), notas_lucas],
    ]
)


# a)
def sort_by_last_name(lista):
    lista.add_criterion("last_name", lambda x: x[0].last_name)

    lista.sort_by_criterion("last_name")

    return lista


print("a) ")
for student in sort_by_last_name(students_list):
    student = student[0]
    print(f"{student.last_name}, {student.name} - Legajo: {student.file}")


# b)
def not_disapprove(lista):
    result = List()
    for student_data in lista:
        student, notes = student_data[0], student_data[1]
        if all(note.note >= 7 for note in notes):
            result.append([student, notes])
    return result


print("b) ")

for student, notes in not_disapprove(students_list):
    print(f"{student.last_name}, {student.name} - Legajo: {student.file}")

# c)
def calculate_average(lista, limit):
    result = List()
    for student, notes in lista:
        avg = sum(note.note for note in notes) / len(notes) if notes else 0
        if avg > limit:
            result.append([student, notes])

    return result


print("c) ")
for student in calculate_average(students_list, 8.89):
    student = student[0]
    print(f"{student.last_name}, {student.name}")


# d)
def show_by_initial(lista, initial):
    result = List()
    for student, notes in lista:
        if student.last_name.startswith(initial):
            result.append([student, notes])
    return result


print("d) ")
for student, notes in show_by_initial(students_list, "L"):
    print(f"{student.last_name}, {student.name} - Legajo: {student.file}")
    for note in notes:
        print(f"Materia: {note.subject}, Nota: {note.note}, Fecha: {note.date}")


# e)
def show_average(lista):
    result = List()
    for student, notes in lista:
        if notes:
            average = sum(note.note for note in notes) / len(notes)
            result.append([student, average])
    return result


print("e) ")
for student, average in show_average(students_list):
    print(f"{student.last_name}, {student.name} - Legajo: {student.file}")
    print(f"Promedio: {average}")


# f)
def show_subject(lista, subj):
    result = List()
    for student, notes in lista:
        for note in notes:
            if note.subject == subj:
                result.append([student, notes])
    return result


print("f) ")
for student, average in show_subject(
    students_list, "Algoritmos y estructuras de datos"
):
    print(f"{student.last_name}, {student.name} - Legajo: {student.file}")


# g)
def pass_percentaje(lista, file_key):
    approvated = 0
    for student, notes in lista:
        if student.file == file_key:
            for note in notes:
                if note.note >= 7:
                    approvated += 1
            return (approvated / len(notes)) * 100
    return None


print("g) ")
student = int(input("Ingrese legajo: "))
percentaje = pass_percentaje(students_list, student)
if percentaje is not None:
    print(f"Porcentaje de parciales aprobados: {percentaje}%.")
else:
    print("Alumno no encontrado.")


# h)
def show_data_base(lista, subj):
    approved = 0
    disapproved = 0
    for student, notes in lista:
        for note in notes:
            if note.subject == subj:
                if note.note >= 7:
                    approved += 1
                else:
                    disapproved += 1
    return approved, disapproved


print("h) ")
approved, disapproved = show_data_base(students_list, "Base de datos")
print(f"Alumnos aprobados: {approved}")
print(f"Alumnos desaprobados: {disapproved}")


# i. mostrar todos los alumnos que rindieron en el año 2020;
def show_student_by_year(lista, year):
    result = List()
    for student, notes in lista:
        for note in notes:
            if note.date.startswith(year):
                result.append([student, notes])
                break
    return result


print("i) ")
for student, notes in show_student_by_year(students_list, "2020"):
    print(f"{student.last_name}, {student.name} - Legajo: {student.file}")
    for note in notes:
        if note.date.startswith("2020"):
            print(f"Materia: {note.subject}, Nota: {note.note}, Fecha: {note.date}")
