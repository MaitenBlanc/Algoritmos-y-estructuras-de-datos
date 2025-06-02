from lista_enlazada import List


def order_by_name(item):
    return item.name


def order_by_year(item):
    return item.year


class Superhero:
    def __init__(self, name, year, house, biography):
        self.name = name
        self.year = year
        self.house = house
        self.biography = biography
        self.movies = List()
        self.movies.add_criterion("name", order_by_name)
        self.movies.add_criterion("year", order_by_year)

    def __str__(self):
        return f"Nombre: {self.name} \nAño: {self.year} \nMovies:"


class Movie:
    def __init__(self, name, year):
        self.name = name
        self.year = year

    def __str__(self):
        return f"{self.name} - {self.year}"


list_superhero = List()
# list_superhero.add_criterion("name", order_by_name)

list_superhero.extend(
    [
        Superhero(
            "Linterna Verde",
            1940,
            "DC",
            "Posee un anillo de poder y viste un traje especial.",
        ),
        Superhero(
            "Wolverine",
            1974,
            "Marvel",
            "Tiene garras retráctiles y factor de curación.",
        ),
        Superhero("Dr. Strange", 1963, "DC", "Usa magia y viste una túnica."),
        Superhero(
            "Iron Man",
            1963,
            "Marvel",
            "Tony Stark usa una armadura de alta tecnología.",
        ),
        Superhero("Capitana Marvel", 1968, "Marvel", "Tiene poderes cósmicos."),
        Superhero(
            "Mujer Maravilla", 1941, "DC", "Princesa amazona con traje de batalla."
        ),
        Superhero("Flash", 1940, "DC", "Corre a velocidades increíbles."),
        Superhero("Star-Lord", 1976, "Marvel", "Usa una máscara y armadura espacial."),
        Superhero(
            "Batman", 1939, "DC", "Lucha contra el crimen con traje de murciélago."
        ),
        Superhero("Spider-Man", 1962, "Marvel", "Lleva un traje rojo y azul."),
        Superhero(
            "Magneto", 1963, "Marvel", "Controla el magnetismo y usa casco y armadura."
        ),
        Superhero("Superman", 1938, "DC", "Traje azul con capa roja."),
    ]
)

list_movie = List()
list_movie.add_criterion("name", order_by_name)

# list_superhero.show()

movie = Movie("Iron Man I", 2008)
movie2 = Movie("Iron Man II", 2010)
movie3 = Movie("Avengers", 2012)
movie4 = Movie("Civil War", 2016)

pos = list_superhero.search("Iron Man", "name")

if pos is not None:
    print(list_superhero[pos])
    hero = list_superhero[pos]
    hero.movies.append(movie)
    hero.movies.append(movie2)
    hero.movies.append(movie3)
    hero.movies.append(movie4)
    # hero.movies.sort_by_criterion("name")
    # hero.movies.sort_by_criterion("year")
    # hero.movies.show()
    # print(list_superhero[pos])
    # pos_movie = hero.movies.search('Civil War', 'name')
    # if pos_movie is not None:
    #     print(hero.movies[pos_movie])

    # pos_movie = hero.movies.search('Iron Man I', 'name')
    # if pos_movie is not None:
    #     hero.movies[pos_movie].year = 2006

    pos_movie = hero.movies.search(2016, "year")
    if pos_movie is not None:
        print(f"Pelicula eliminada: {hero.movies.delete_value(2016, 'year')}")
        
    print()

    hero.movies.show()
