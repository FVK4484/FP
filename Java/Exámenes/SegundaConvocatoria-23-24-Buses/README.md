# Fundamentos de Programación
# Curso 24-25. Primera Convocatoria: Buses

**Autora:**  Toñi Reina
**Revisores:** Daniel Mateos, Mariano González.
**Última modificación:** 24/05/2025.

Se desea implementar parte de un sistema relacionado con la gestión de líneas de autobuses. Para ello se dispone de un archivo `viajes.csv`, donde la información de cada línea se corresponde con: el precio del viaje (en euros); la distancia en km que se recorre en el viaje; la duración, en horas y minutos; si el viaje es directo (Directo), tiene transbordos (Transbordo) o ha sido cancelado (Cancelado); y el trayecto viene especificado por las distintas paradas en el viaje mediante una lista, entre corchetes, de ciudades y horas separadas por comas. La ciudad está separada de la hora por un guion. La hora representa la hora de salida de la parada. La última parada del trayecto viene marcada por la palabra FIN. Dos paradas consecutivas y con el mismo nombre indican transbordo, por ejemplo, el viaje Sevilla-Lisboa que aparece en la segunda línea del archivo CSV, tiene dos transbordos: Faro y Albufeira. Los transbordos se han marcado en negrilla en en siguiente extracto del archivo CSV:

|```Precio;Distancia;Duracion;TipoViaje;Trayecto
14.99;507;7:20;Transbordo;[Sevilla-09:00, Huelva-10:10, **Faro-11:20, Faro-11:30**,Aeropuerto Faro-12:30, **Albufeira-13:40,Albufeira-14:00**, Lisboa-FIN]
64.99;1153;16:00;Transbordo;[Madrid-08:00, **Hub-09:45, Hub-11:30,** Bilbao-13:15, San Sebastián-15:00, Irún-16:45, Orthez-18:30, Toulouse-20:15, Nimes-FIN]
99.99;923;12:50;Directo;[Paris-07:00, Lyon-09:10, Chambéry-11:20, Oulx-13:30, Turín-15:40, Milán-FIN]
69.04;1487;24:50;Transbordo;[Grenoble-06:00, Valence-08:15, Aviñón-10:30, Nimes-12:45, Toulouse-15:00, Orthez-17:15, **Irún-19:30, Irún-19:40,**San Sebastián-21:45, Pamplona-00:00, Tudela-02:15, Lleida-04:30, Barcelona-FIN]```


**EJERCICIO 1 – TIPO BASE (2,5 puntos)**

Se pide implementar los tipos `Viaje`, como una clase, y `Parada`, como un record, teniendo en cuenta las siguientes descripciones:

**Tipo Parada**:

Propiedades:

- nombre, de tipo String, consultable. Nombre de la ciudad en la que el autobús realiza la parada.
- hora, de tipo LocalTime, consultable. Hora de salida del autobús para la siguiente parada del trayecto. Si la parada representa la última del trayecto, la hora será null.

Criterio de igualdad: dos paradas son iguales si tienen el mismo nombre y la misma hora de salida.

Representación como cadena: todas las propiedades básicas del tipo.

Constructores: 

- C1: un constructor que tiene un como parámetros el nombre de la parada y la hora.

**Tipo Viaje**:

Propiedades:

- precio, de tipo Double, consultable y modificable.
- distancia (en km), de tipo Integer, consultable y modificable. Distancia total recorrida en el viaje.
- duracion (en horas y minutos), de tipo Duration, consultable y modificable.
- tipo, de TipoViaje, consultable y modificable.  Puede tomar los valores DIRECTO, TRANSBORDO, CANCELADO. Indica si el viaje es directo, tiene transbordos o se ha cancelado. 
- trayecto, de tipo `List<Parada>`, consultable y modificable. Lista con las paradas del viaje, ordenadas de origen a destino.
- velocidad media (en km/h), de tipo Double. Velocidad media, que se calcula a partir de la distancia y la duración.
- número de paradas, de tipo Integer. Número de paradas intermedias entre el origen y el destino, **sin contar dos veces los transbordos**. Por ejemplo, el viaje Sevilla-Lisboa que aparece en la segunda línea del archivo CSV tiene 4 paradas intermedias: Huelva, Faro, Aeropuerto de Faro y Albufeira.
- intermedias, de tipo List<String>, Nombres de las paradas intermedias del trayecto, teniendo en cuenta los transbordos. La lista estará vacía si no hay paradas intermedias. Por ejemplo, la lista de paradas para el viaje Sevilla-Lisboa que aparece en la cuarta línea del archivo CSV sería: ["Huelva", "Faro", "Faro", "Aeropuerto de Faro", "Albufeira", "Albufeira"].
- origen, de tipo String. Nombre del primer punto del trayecto.
- destino, de tipo String, derivada. Último punto del trayecto.
- numero transbordos, de tipo Integer. Un transbordo se identifica en un trayecto porque la ciudad o punto de transbordo aparece repetida de forma consecutiva en el trayecto. Por ejemplo, en el viaje de Madrid a Nimes que aparece en la tercera línea del CSV hay un transbordo en Hub, y en el viaje Grenoble-Barcelona de la cuarta línea hay un transbordo en Irún.

Criterio de igualdad: Dos viajes son iguales si tienen los mismos trayectos.

Representación como cadena: La generada por defecto por Eclipse.

Constructores: 

- C1: Constructor que tiene como parámetros el precio, la distancia, la duración (de tipo Duration), el tipo de viaje, la parada origen y la parada destino del trayecto, ambas de tipo Parada.
- C2:  Constructor que tiene como parámetros cada una de las propiedades básicas del tipo.

Restricciones:

- R1: El trayecto debe tener al menos dos paradas (origen y destino).
- R2: La distancia, la duración y el precio deben ser mayores que cero.
- R3: El tipo de viaje de un viaje con solo un origen y un destino no puede ser TRANSBORDO.

**EJERCICIO 2 – FACTORÍA (1 punto)**

En la clase **FactoriaViajes**, que se le da parcialmente implementada, implemente el método:

`Viaje parseaViaje(String lineaCSV)`: crea un objeto de tipo Viaje a partir de una cadena de caracteres. La cadena de caracteres debe tener el mismo formato que las líneas del fichero CSV.

**EJERCICIO 3 – TIPO CONTENEDOR (6,5 puntos)**

Implemente el tipo contenedor **AgenciaBus**. La descripción del tipo es la siguiente:

Propiedades:

- nombre, de tipo String. Consultable. Nombre de la agencia.
- viajes, de tipo `List<Viaje>`. Consultable. Lista con viajes.

Constructores: 

- Un constructor que tiene como parámetros un nombre y un Stream<Viaje> y crea un objeto de tipo AgenciaBus a partir del nombre y el Stream dados. (se supone implementado)

Representación como cadena: una cadena con todos los viajes. Cada viaje aparecerá en una línea distinta.

Criterio de igualdad: dos objetos de tipo AgenciaBus son iguales si lo son sus viajes.

Implemente el tipo **AgenciaBus** y añada los siguientes tratamientos secuenciales. Debe resolver todos los métodos **mediante streams, salvo que se indique lo contrario**:

1. `Duration getMaximaDuracion`: Devuelve la duración de tipo Duration del viaje más largo, siendo el viaje más largo aquél que consta de un mayor número de paradas intermedias, sin contar los transbordos. En caso de que no exista el viaje más largo, el método debe devolver una duración de cero. (1 punto)

1. `void añadirTiempoDescanso(String parada, Integer minutos)`: Dados el nombre de una parada intermedia, de tipo String,  y un tiempo extra en minutos, de tipo Integer, añade ese tiempo extra a los viajes cuyo trayecto incluya dicha parada. (1 punto)

1. `SortedMap<String, Duration> getDuracionMinimaPorDestino(TipoViaje tipo)`: Devuelve un `SortedMap<String, Duration>` que relaciona los destinos de los viajes del tipo dado como parámetro con la duración del viaje de menor duración a dicho destino. Las claves estarán ordenadas en orden alfabético. (1,5 puntos)

1. `Map<String, Set<Viaje>> getViajesPorParadas(Double precio)`: Devuelve un `Map<String, Set<Viaje>>` que relaciona los nombres de las paradas el conjunto de viajes que pasan por esa parada, siempre que el precio del viaje no supere al dado como parámetro. Si el precio dado como parámetro es null, entonces no se tiene en cuenta el precio. El inicio y fin de trayecto se deben incluir como paradas. **Implemente este método mediante bucles.** (1,5 puntos)

1. `SortedMap<String, Double> getPrecioMedioViajesPorParada():` Devuelve un `Map<String, Double>` que relaciona los nombres de las paradas por las que pasa más de un viaje con el precio medio de los viajes que pasan por esa parada. (1,5 puntos)

Escriba una clase **TestAgenciaBus**. En la clase se leerán los datos del fichero y se probarán todos los tratamientos secuenciales, definiendo un método de test por cada tratamiento secuencial a probar. No se obtendrá la puntuación máxima del ejercicio si no se realiza el test, este ejecuta y su valor es el esperado. Los resultados esperados para el dataset proporcionado, con los valores indicados en los tests, son:


```
Test lectura ==========================================================================

Se han leido 19 viajes
Los tres primeros son:
Viaje [precio=14.99, distancia=507, duracion=PT7H20M, tipo=TRANSBORDO, trayecto=[Parada[nombre=Sevilla, horaSalida=09:00], Parada[nombre=Huelva, horaSalida=10:10], Parada[nombre=Faro, horaSalida=11:20], Parada[nombre=Faro, horaSalida=11:30], Parada[nombre=Aeropuerto Faro, horaSalida=12:30], Parada[nombre=Albufeira, horaSalida=13:40], Parada[nombre=Albufeira, horaSalida=14:00], Parada[nombre=Lisboa, horaSalida=null]]]
Viaje [precio=64.99, distancia=1153, duracion=PT16H, tipo=TRANSBORDO, trayecto=[Parada[nombre=Madrid, horaSalida=08:00], Parada[nombre=Hub, horaSalida=09:45], Parada[nombre=Hub, horaSalida=11:30], Parada[nombre=Bilbao, horaSalida=13:15], Parada[nombre=San Sebastián, horaSalida=15:00], Parada[nombre=Irún, horaSalida=16:45], Parada[nombre=Orthez, horaSalida=18:30], Parada[nombre=Toulouse, horaSalida=20:15], Parada[nombre=Nimes, horaSalida=null]]]
Viaje [precio=99.99, distancia=923, duracion=PT12H50M, tipo=DIRECTO, trayecto=[Parada[nombre=Paris, horaSalida=07:00], Parada[nombre=Lyon, horaSalida=09:10], Parada[nombre=Chambéry, horaSalida=11:20], Parada[nombre=Oulx, horaSalida=13:30], Parada[nombre=Turín, horaSalida=15:40], Parada[nombre=Milán, horaSalida=null]]]

Test 4.a ==============================================================================
La duración máxima es PT24H50M

Test 4.b ==============================================================================
Se van a añadir 30 minutos a los viajes con la parada Bilbao, que son

Viaje [precio=64.99, distancia=1153, duracion=PT16H, tipo=TRANSBORDO, trayecto=[Parada[nombre=Madrid, horaSalida=08:00], Parada[nombre=Hub, horaSalida=09:45], Parada[nombre=Hub, horaSalida=11:30], Parada[nombre=Bilbao, horaSalida=13:15], Parada[nombre=San Sebastián, horaSalida=15:00], Parada[nombre=Irún, horaSalida=16:45], Parada[nombre=Orthez, horaSalida=18:30], Parada[nombre=Toulouse, horaSalida=20:15], Parada[nombre=Nimes, horaSalida=null]]]
Viaje [precio=110.99, distancia=1450, duracion=PT18H, tipo=TRANSBORDO, trayecto=[Parada[nombre=Lisbon, horaSalida=05:00], Parada[nombre=Porto, horaSalida=08:00], Parada[nombre=Porto, horaSalida=08:15], Parada[nombre=Bilbao, horaSalida=12:10], Parada[nombre=Bordeaux, horaSalida=15:30], Parada[nombre=Bordeaux, horaSalida=15:40], Parada[nombre=Paris, horaSalida=null]]]

Los viajes tras la modificación son

Viaje [precio=64.99, distancia=1153, duracion=PT16H30M, tipo=TRANSBORDO, trayecto=[Parada[nombre=Madrid, horaSalida=08:00], Parada[nombre=Hub, horaSalida=09:45], Parada[nombre=Hub, horaSalida=11:30], Parada[nombre=Bilbao, horaSalida=13:15], Parada[nombre=San Sebastián, horaSalida=15:00], Parada[nombre=Irún, horaSalida=16:45], Parada[nombre=Orthez, horaSalida=18:30], Parada[nombre=Toulouse, horaSalida=20:15], Parada[nombre=Nimes, horaSalida=null]]]
Viaje [precio=110.99, distancia=1450, duracion=PT18H30M, tipo=TRANSBORDO, trayecto=[Parada[nombre=Lisbon, horaSalida=05:00], Parada[nombre=Porto, horaSalida=08:00], Parada[nombre=Porto, horaSalida=08:15], Parada[nombre=Bilbao, horaSalida=12:10], Parada[nombre=Bordeaux, horaSalida=15:30], Parada[nombre=Bordeaux, horaSalida=15:40], Parada[nombre=Paris, horaSalida=null]]]

Test 4.c ==============================================================================

La duración minima por cada destino para viajes de tipo TRANSBORDO es 
Barcelona=PT24H50M
Berlin=PT21H
Copenhagen=PT9H
Hamburg=PT6H
Lisboa=PT7H20M
Nimes=PT16H30M
Paris=PT18H30M
Roma=PT14H
Sevilla=PT10H
Vienna=PT14H30M

La duración minima por cada destino para viajes de tipo DIRECTO es 
Barcelona=PT4H30M
Edinburgh=PT8H
Krakow=PT4H
Madrid=PT9H
Milán=PT12H50M
Prague=PT5H
Thessaloniki=PT6H30M
Vienna=PT8H30M

Test 4.d ==============================================================================
Hay 6 paradas con viajes con precio inferior a 20,00 Euros son 
Aeropuerto Faro=[Viaje [precio=14.99, distancia=507, duracion=PT7H20M, tipo=TRANSBORDO, trayecto=[Parada[nombre=Sevilla, horaSalida=09:00], Parada[nombre=Huelva, horaSalida=10:10], Parada[nombre=Faro, horaSalida=11:20], Parada[nombre=Faro, horaSalida=11:30], Parada[nombre=Aeropuerto Faro, horaSalida=12:30], Parada[nombre=Albufeira, horaSalida=13:40], Parada[nombre=Albufeira, horaSalida=14:00], Parada[nombre=Lisboa, horaSalida=null]]]]
Albufeira=[Viaje [precio=14.99, distancia=507, duracion=PT7H20M, tipo=TRANSBORDO, trayecto=[Parada[nombre=Sevilla, horaSalida=09:00], Parada[nombre=Huelva, horaSalida=10:10], Parada[nombre=Faro, horaSalida=11:20], Parada[nombre=Faro, horaSalida=11:30], Parada[nombre=Aeropuerto Faro, horaSalida=12:30], Parada[nombre=Albufeira, horaSalida=13:40], Parada[nombre=Albufeira, horaSalida=14:00], Parada[nombre=Lisboa, horaSalida=null]]]]
Faro=[Viaje [precio=14.99, distancia=507, duracion=PT7H20M, tipo=TRANSBORDO, trayecto=[Parada[nombre=Sevilla, horaSalida=09:00], Parada[nombre=Huelva, horaSalida=10:10], Parada[nombre=Faro, horaSalida=11:20], Parada[nombre=Faro, horaSalida=11:30], Parada[nombre=Aeropuerto Faro, horaSalida=12:30], Parada[nombre=Albufeira, horaSalida=13:40], Parada[nombre=Albufeira, horaSalida=14:00], Parada[nombre=Lisboa, horaSalida=null]]]]
Huelva=[Viaje [precio=14.99, distancia=507, duracion=PT7H20M, tipo=TRANSBORDO, trayecto=[Parada[nombre=Sevilla, horaSalida=09:00], Parada[nombre=Huelva, horaSalida=10:10], Parada[nombre=Faro, horaSalida=11:20], Parada[nombre=Faro, horaSalida=11:30], Parada[nombre=Aeropuerto Faro, horaSalida=12:30], Parada[nombre=Albufeira, horaSalida=13:40], Parada[nombre=Albufeira, horaSalida=14:00], Parada[nombre=Lisboa, horaSalida=null]]]]
Lisboa=[Viaje [precio=14.99, distancia=507, duracion=PT7H20M, tipo=TRANSBORDO, trayecto=[Parada[nombre=Sevilla, horaSalida=09:00], Parada[nombre=Huelva, horaSalida=10:10], Parada[nombre=Faro, horaSalida=11:20], Parada[nombre=Faro, horaSalida=11:30], Parada[nombre=Aeropuerto Faro, horaSalida=12:30], Parada[nombre=Albufeira, horaSalida=13:40], Parada[nombre=Albufeira, horaSalida=14:00], Parada[nombre=Lisboa, horaSalida=null]]]]
Sevilla=[Viaje [precio=14.99, distancia=507, duracion=PT7H20M, tipo=TRANSBORDO, trayecto=[Parada[nombre=Sevilla, horaSalida=09:00], Parada[nombre=Huelva, horaSalida=10:10], Parada[nombre=Faro, horaSalida=11:20], Parada[nombre=Faro, horaSalida=11:30], Parada[nombre=Aeropuerto Faro, horaSalida=12:30], Parada[nombre=Albufeira, horaSalida=13:40], Parada[nombre=Albufeira, horaSalida=14:00], Parada[nombre=Lisboa, horaSalida=null]]]]

Hay 73 paradas con viajes con precio inferior a null Euros son 
Aeropuerto Faro=[Viaje [precio=14.99, distancia=507, duracion=PT7H20M, tipo=TRANSBORDO, trayecto=[Parada[nombre=Sevilla, horaSalida=09:00], Parada[nombre=Huelva, horaSalida=10:10], Parada[nombre=Faro, horaSalida=11:20], Parada[nombre=Faro, horaSalida=11:30], Parada[nombre=Aeropuerto Faro, horaSalida=12:30], Parada[nombre=Albufeira, horaSalida=13:40], Parada[nombre=Albufeira, horaSalida=14:00], Parada[nombre=Lisboa, horaSalida=null]]]]
Albufeira=[Viaje [precio=14.99, distancia=507, duracion=PT7H20M, tipo=TRANSBORDO, trayecto=[Parada[nombre=Sevilla, horaSalida=09:00], Parada[nombre=Huelva, horaSalida=10:10], Parada[nombre=Faro, horaSalida=11:20], Parada[nombre=Faro, horaSalida=11:30], Parada[nombre=Aeropuerto Faro, horaSalida=12:30], Parada[nombre=Albufeira, horaSalida=13:40], Parada[nombre=Albufeira, horaSalida=14:00], Parada[nombre=Lisboa, horaSalida=null]]]]

... (se omite el resto por cuestión de esapacio)

Ústí nad Labem=[Viaje [precio=30.99, distancia=350, duracion=PT5H, tipo=DIRECTO, trayecto=[Parada[nombre=Berlin, horaSalida=07:00], Parada[nombre=Dresden, horaSalida=09:00], Parada[nombre=Ústí nad Labem, horaSalida=10:30], Parada[nombre=Prague, horaSalida=null]]]]

Test 4.e ==============================================================================

El precio medio de los viajes por parada es 
Amsterdam=110.99
Barcelona=78.51
Berlin=80.99000000000001
Bilbao=88.65666666666665
Copenhagen=65.99
Frankfurt=117.65666666666668
Hub=83.9925
Innsbruck=92.995
Irún=67.015
Lisboa=32.49
Lyon=115.49000000000001
Madrid=83.99000000000001
Munich=107.995
Nimes=67.015
Orthez=67.015
Paris=105.49
Salzburg=80.99
San Sebastián=67.015
Sevilla=52.489999999999995
Toulouse=67.015
Vienna=80.99
Zurich=95.99
```