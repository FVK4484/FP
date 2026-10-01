# Constructor a partir de String y Factoría
Autora: Toñi Reina


## EJERCICIO 1
Se quiere dotar a la clase CursoOnLine de un constructor de String, que permita construir objetos de tipo CursoOnLine a partir de una cadena con el siguiente formato:

```
id,titulo,organizacion,fechaInicio,fechaFin,duracion,tipoCertificacion,valoracion,nivelDificultad,numeroEstudiantes,gratuito
```

Por ejemplo, 

```
ABC12345,Introducción a la Programación,Universidad X,01/04/2024,30/05/2024,60,Curso,4.5,Intermedio,100,true
```

Implemente un nuevo constructor en el tipo CursoOnLine a partir de un parámetro de tipo String.

## EJERCICIO 2

En el paquete `fp.tipos.cursos` implemente una factoría estática que tenga los siguientes métodos creacionales:

-  Un método creacional por cada constructor de `CursoOnLine`, que reciba los mismos parámetros que el constructor correspondiente.

- Un método creacional a partir de fichero. Este método recibe la ruta de un fichero de texto y debe devolver una lista de objetos creados a partir de cada línea del fichero. Use la clase `Ficheros.java` [^1].  

- Un método creacional copia, que reciba un objeto del tipo en cuestión y construya uno nuevo con los mismos valores en todas las propiedades.

[^1]: Descarga la clase [Ficheros.java](https://github.com/FP-25-26/LAB-Universidad/blob/master/src/fp/utiles/Ficheros.java) y cópiala en el paquete `fp.utiles`.


