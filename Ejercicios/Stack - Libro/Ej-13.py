"""
    Dada una pila con los trajes de Iron Man utilizados en las películas de Marvel Cinematic Universe (MCU) de los cuales se conoce 
    el nombre del modelo, nombre de la película en la que se usó y el estado en que quedó al final de la película 
    (Dañado, Impecable, Destruido), resolver las siguientes actividades:
    a. determinar si el modelo Mark XLIV (Hulkbuster) fue utilizado en alguna de las películas, además mostrar el nombre de dichas 
    películas;
    b. mostrar los modelos que quedaron dañados, sin perder información de la pila.
    c. eliminar los modelos de los trajes destruidos mostrando su nombre;
    d. un modelo de traje puede usarse en más de una película y en una película se pueden usar más de un modelo de traje, 
    estos deben cargarse por separado;
    e. agregar el modelo Mark LXXXV a la pila, tener en cuenta que no se pueden cargar modelos repetidos en una misma película;
    f. mostrar los nombre de los trajes utilizados en las películas “Spider-Man: Homecoming” y “Capitan America: Civil War”.
"""

import sys
sys.path.append("./Clases")
from stack import Stack

stack_armors = Stack()

# Carga de datos al stack
stack_armors.push({'model': 'Mark I', 'movie': 'Iron Man', 'status': 'Dañado'})
stack_armors.push({'model': 'Mark III', 'movie': 'Iron Man', 'status': 'Impecable'})
stack_armors.push({'model': 'Mark XLII', 'movie': 'Iron Man 3', 'status': 'Dañado'})
stack_armors.push({'model': 'Mark XLIII', 'movie': 'Avengers: Age of Ultron', 'status': 'Dañado'})
stack_armors.push({'model': 'Mark XLIV', 'movie': 'Avengers: Age of Ultron', 'status': 'Dañado'})
stack_armors.push({'model': 'Mark XLIV', 'movie': 'Avengers: Infinity War', 'status': 'Destruido'})
stack_armors.push({'model': 'Mark L', 'movie': 'Avengers: Infinity War', 'status': 'Dañado'})
stack_armors.push({'model': 'Mark LXXXV', 'movie': 'Avengers: Endgame', 'status': 'Destruido'})
stack_armors.push({'model': 'Mark XLVII', 'movie': 'Spider-Man: Homecoming', 'status': 'Impecable'})
stack_armors.push({'model': 'Mark XLVI', 'movie': 'Capitan America: Civil War', 'status': 'Dañado'})
stack_armors.push({'model': 'Mark XLVII', 'movie': 'Capitan America: Civil War', 'status': 'Dañado'})

# a) 
def search_hulkbuster(stack): 
    aux_stack = Stack()
    movies = Stack()
    found = False
    while stack.size() > 0:
        armor = stack.pop()
        if (armor['model'] == "Mark XLIV"):
            movies.push(armor['movie'])
            found = True
        aux_stack.push(armor)
        
    while aux_stack.size() > 0:
        stack.push(aux_stack.pop())
        
    if found:
        print("La armadura Hulkbuster fue usada en las siguientes películas: ")
        for i in range(movies.size()):
            print(f"- {movies.pop()}")
    else:
        print("La armadura Hulkbuster no fue usada en ninguna película.")

# b)
def damaged_models(stack):
    aux_stack = Stack()
    damaged = Stack()
    while stack.size() > 0:
        armor = stack.pop()
        
        if armor['status'] == 'Dañado':
            damaged.push(armor['model'])
        aux_stack.push(armor)

    while damaged.size() > 0:
        print(f"- {damaged.pop()}")
    
    while aux_stack.size() > 0:
        stack.push(aux_stack.pop())

# c)
def delete_destroyed(stack):
    aux_stack = Stack()
    destroyed = Stack()
    while stack.size() > 0:
        armor = stack.pop()
        if armor["status"] == "Destruido":
            destroyed.push(armor["model"])
        else:
            aux_stack.push(armor)
    
    while aux_stack.size() > 0:
        stack.push(aux_stack.pop())

    return destroyed

# e) 
def add_model_LXXXV(stack, model, movie, status):
    aux_stack = Stack()
    exists = False
    
    while stack.size() > 0:
        armor = stack.pop()
        
        if (armor['model'] == model) and (armor['movie'] == movie):
            exists = True
        aux_stack.push(armor)
        
    while aux_stack.size() > 0:
        stack.push(aux_stack.pop())
        
    if not exists: 
        stack.push({'model': model, 'movie': movie, 'status': status})

# f) 
def show_armors(stack, wanted_movie):
    aux_stack = Stack()
    model_stack = Stack()
    
    while stack.size() > 0:
        armor = stack.pop()
        if armor['movie'] in wanted_movie: 
            model_stack.push(armor['model'])
        aux_stack.push(armor)
            
    while aux_stack.size() > 0:
        stack.push(aux_stack.pop())

    return model_stack


print("a)")
search_hulkbuster(stack_armors)

print("b) Modelos dañados: ")
damaged_models(stack_armors)
print("Todos los modelos: ")
stack_armors.show()

print("c) Trajes destruidos: ")
destroyed = delete_destroyed(stack_armors)
destroyed.show()

print("e)")
add_model_LXXXV(stack_armors, "Mark XLIV", "Avengers: Infinity War", "Destruido") # No se debe agregar
stack_armors.show()
print("\n")
add_model_LXXXV(stack_armors, "Mark V", "Iron Man 2", "Destruido") # Se debe agregar
stack_armors.show()

print("f) Modelos en las películas 'Spider-Man: Homecoming' y 'Capitan America: Civil War': ")
wanted_movies = ["Spider-Man: Homecoming", "Capitan America: Civil War"]
models = show_armors(stack_armors, wanted_movies)
models.show()