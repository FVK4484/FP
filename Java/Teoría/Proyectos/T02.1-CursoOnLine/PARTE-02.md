# Tipo Contenedor - Gestor Cursos
Autora: Toñi Reina

Se quiere implementar el tipo GestorCursos para ayudar en la gestión de cursos on line. Implemente el tipo `GestorCursos` en el paquete `fp.tipos.cursos` atendiendo a la siguiente descripción:

Propiedades:

- *nombre*, de tipo String, consultable.
- *url*, de tipo String, consultable y modificable.
- *cursos*, de tipo `List<CursoOnLine>`, consultable.

Constructores:

- *C1* : Constructor con valores para el nombre y la url, creando una colección vacía de cursos.

Representación como cadena: 

Nombre de la empresa que oferta los cursos, seguido de su url entre paréntesis (si es que la tiene), y el número de cursos ofertados. Ejemplo: ```class central (https://www.classcentral.com)  - 10 cursos```.

Criterio de igualdad: Dos gestores de cursos serán iguales si tienen el mismo nombre y la misma url.

Restricciones:
- R1: El nombre no puede ser null.
- R2: La url debe comenzar por http o https.

Otras operaciones:

- *void agregaCurso (CursoOnLine c)*. Añade un nuevo curso, que se pasa como parámetro a la lista de cursos del gestor. Se admiten cursos duplicados en la biblioteca. Si el curso tiene el valor null la operación no tiene efecto.

- *void eliminaCurso(CursoOnLine c)*. Se elimina el curso que se pasa como parámetro de la lista de cursos. Si el curso no existe, se eleva IllegalArgumentException.

- *void agregaCursos(Collection<CursoOnLine> cursos)*. Agrega los cursos de la colección que se pasa como parámetro a la biblioteca.





