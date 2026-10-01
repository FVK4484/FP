# T02.1-CursoOnLine
Se está desarrollando un sistema para gestionar cursos online. Para ello el primer paso es diseñar el tipo `CursoOnLine` que se describe a continuación e implementar el tipo. 

Cada curso tiene un _identificador_ único que es una cadena alfanumérica única que lo distingue de otros cursos en la plataforma y está formado por tres letras seguidas de 5 dígitos (por ejemplo, COU00001). 

Otros datos del curso son su _título_, que es una descripción breve y descriptiva del contenido del curso (por ejemplo, “Aprende a programar en Python”); la _organización_ que lo oferta (por ejemplo, “Coursera”); las _fechas de inicio y finalización_ (por ejemplo, 14 de Febrero de 2023 y 14 de Mayo de 2023, respectivamente), siendo siempre la fecha de finalización posterior a la fecha de inicio;  la _duración_ en horas del curso (por ejemplo, 60 horas), teniendo en cuenta que la duración mínima de un curso es de 1 hora; el tipo de _certificación_ que otorga el curso, que puede ser "CURSO", "ESPECIALIZACIÓN" o "CERTIFICACIÓN PROFESIONAL“; la _valoración_ promedio, otorgada por los estudiantes han completado el curso, por ejemplo, 4.8, que debe estar comprendida entre 0 y 5; el _nivel de dificultad_ del curso, que puede tomar los valores Principiante, Intermedio o Avanzado; el _número de estudiantes_ que se han matriculado en el curso, por ejemplo, 1200, no pudiendo ser nunca un número negativo; y un indicador booleano para indicar si el curso es _gratuito_. La aplicación necesita conocer la _media de horas semanales_ que hay que dedicarle al curso, que se calcula a partir de la duración en semanas del curso y el número de horas del mismo; y el _estado del curso_, que puede tomar los valores EN_CURSO, FINALIZADO y PROXIMO, que se calculará dependiendo de la fecha actual y las fechas de inicio y finalización del curso.

Una vez creado el curso en el sistema, solamente las fechas de inicio y fin, el número de horas y la gratuidad del curso pueden ser cambiados.

Se considera que dos objetos de tipo CursoOnLine son iguales si tienen el mismo id y el midmo título.

Los CursosOnLine se pueden ordenar, de manera natural, por el título, y en caso de coincidencia por el id.


