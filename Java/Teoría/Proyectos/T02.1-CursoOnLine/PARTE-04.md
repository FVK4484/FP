# Map/SortedMap
Autora: Toñi Reina

Se quieren añadir las siguientes operaciones al tipo `GestorCursos` para trabajar con `Map` y `SortedMap`:

- `Map<NivelDificultad, Integer> contarCursosPorNivelDificultad()`: Cuenta el número de cursos por cada nivel de dificultad. Por ejemplo, `{AVANZADO=2, INTERMEDIO=2, BASICO=1}`
- `SortedMap<Integer, Integer> contarCursosPorMes()`: Cuenta el número de cursos por mes de impartición.
- `Map<String, Integer> contarCursosGratuitosPorOrganizacion()`: Cuenta el número de cursos gratuitos impartidos por organización.
- `SortedMap<Integer, Integer> getTotalEstudiantesPorAño()`: Devuelve un SortedMap en el que las claves son los años, y el número de estudiantes que finalizaron el curso ese año. 
- `SortedMap<LocalDate, List<CursoOnLine>> getCursosPorMesAño()`: Devuelve un `SortedMap` en el que las claves son los meses y los valores una lista con los cursos de ese mes y año. El representante canónico del mes es el día 1.
- `SortedMap<Integer, Set<String>> getOrganizacionesPorDuracion()`: Devuelve un `SortedMap` donde cada clave representa la duración de los cursos, y cada valor es un conjunto con los nombres de las organizaciones que ofrecen cursos con esa duración.
- `Map<String, CursoOnLine> getCursoMasEstudiantesPorOrganizacion()`:Devuelve un `Map` en el que las claves son las organizaciones, y los valores el curso de esa organización con más estudiantes.
- `SortedMap<Integer, Set<String>> getOrganizacionesPorNumCursosGratuitos()`: Devuelve un `SortedMap` donde cada clave representa el número de cursos gratuitos ofertados, y cada valor es un conjunto con los nombres de las organizaciones con ese número de cursos gratuitos. 



