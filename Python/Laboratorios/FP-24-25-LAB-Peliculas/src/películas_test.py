def test_peliculas_por_genero():
    peliculas = [
        Pelicula(titulo='El viaje de Chihiro', genero='fantasia', año=1988, duracion=120, precio=10.5),
        Pelicula(titulo='La isla de los muertos', genero='fantasia', año=1992, duracion=140, precio=12.5),
        Pelicula(titulo='El secreto de sus ojos', genero='fantasia', año=1994, duracion=160, precio=15.5),
        Pelicula(titulo='La isla de los muertos', genero='fantasia', año=1992, duracion=140, precio=12.5),
        Pelicula(titulo='El secreto de sus ojos', genero='fantasia', año=1994, duracion=160, precio=15.5),
        Pelicula(titulo='Los misterios de la isla del rey león', genero='fantasia', año=1995, duracion=180, precio=17.5),
        Pelicula(titulo='El secreto de sus ojos', genero='fantasia', año=1994, duracion=160, precio=15.5),
    ]
    assert peliculas_por_genero(peliculas) == {
        'fantasia': [1988, 1992, 1994, 1995],
        'comedia': [1995],
    }

def test_peliculas_por_año():
    peliculas = [
        Pelicula(titulo='El viaje de Chihiro', genero='fantasia', año=1988, duracion=120, precio=10.5),
        Pelicula(titulo='La isla de los muertos', genero='fantasia', año=1992, duracion=140, precio=12.5),
        Pelicula(titulo='El secreto de sus ojos', genero='fantasia', año=1994, duracion=160, precio=15.5),
        Pelicula(titulo='La isla de los muertos', genero='fantasia', año=1992, duracion=140, precio=12.5),
        Pelicula(titulo='El secreto de sus ojos', genero='fantasia', año=1994, duracion=160, precio=15.5),
        Pelicula(titulo='Los misterios de la isla del rey león', genero='fantasia', año=1995, duracion=180, precio=17.5),
        Pelicula(titulo='El secreto de sus ojos', genero='fantasia', año=1994, duracion=160, precio=15.5),
    ]
    assert peliculas_por_año(peliculas) == {
        1988: [Pelicula(titulo='El viaje de Chihiro', genero='fantasia', año=1988, duracion=120, precio=10.5)],
        1992: [Pelicula(titulo='La isla de los muertos', genero='fantasia', año=1992, duracion=140, precio=12.5), Pelicula(titulo='La isla de los muertos', genero='fantasia', año=1992, duracion=140, precio=12.5)],
        1994: [Pelicula(titulo='El secreto de sus ojos', genero='fantasia', año=1994, duracion=160, precio=15.5), Pelicula(titulo='El secreto de sus ojos', genero='fantasia', año=1994, duracion=160, precio=15.5), Pelicula(titulo='Los misterios de la isla del rey león', genero='fantasia', año=1995, duracion=180, precio=17.5)],
    }

def test_peliculas_por_fecha():
    peliculas = [
        Pelicula(titulo='El viaje de Chihiro', genero='fantasia', año=1988, duracion=120, precio=10.5),
        Pelicula(titulo='La isla de los muertos', genero='fantasia', año=1992, duracion=140, precio=12.5),
        Pelicula(titulo='El secreto de sus ojos', genero='fantasia', año=1994, duracion=160, precio=15.5),
        Pelicula(titulo='La isla de los muertos', genero='fantasia', año=1992, duracion=140, precio=12.5),
        Pelicula(titulo='El secreto de sus ojos', genero='fantasia', año=1994, duracion=160, precio=15.5),
        Pelicula(titulo='Los misterios de la isla del rey león', genero='fantasia', año=1995, duracion=180, precio=17.5),
        Pelicula(titulo='El secreto de sus ojos', genero='fantasia', año=1994, duracion=160, precio=15.5),
    ]       