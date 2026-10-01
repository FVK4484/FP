import os
import webbrowser
import folium
from coordenadas import*
from sevici import*

# Ejercicio3
def crea_mapa(latitud, longitud, zoom=9):
    '''
    Función que crea un mapa folium que está centrado en la latitud y longitud
    dados como parámetro y mostrado con el nivel de zoom dado.
    ENTRADA:
        :param latitud: latitud del centro del mapa en pantalla
        :type latitud:float
        :param longitud: longitud del centro del mapa  en pantalla
        :type longitud: float
        :param zoom: nivel del zoom con el que se muestra el mapa
        :type zoom: int
    SALIDA:
        :return: objeto mapa creado
        :rtype: folium.Map
    '''
    mapa = folium.Map(location=[latitud, longitud], 
                      zoom_start=zoom)
    return mapa  

def crea_marcador (latitud, longitud, etiqueta, color):
    '''
    Función que crea un marcador rojo con un icono de tipo señal de información.
    El marcador se mostrará en el punto del mapa dado por la latitud y longitud
    y cuandos se mueva el ratón sobre él, se mostrará una etiqueta con el texto
    dado por el parámetro etiqueta
    ENTRADA:
        :param latitud: latitud del marcador
        :type latitud: float
        :param longitud: longitud del marcador
        :type longitud: float
        :param etiqueta: texto de la etiqueta que se asociará al marcador 
        :type etiqueta: str
    SALIDA:
        :return: objeto marcador creado
        :rtype:folium.Marker
    '''
    marcador = folium.Marker([latitud,longitud], 
                   popup=etiqueta, 
                   icon=folium.Icon(color=color, icon='info-sign')) 
    return marcador

def crea_mapa_estaciones(estaciones, funcion_color):
    '''Genera un objeto de tipo folium.Map con un marcador por cada
    estación dada como parámetro. El marcador tendrá como etiqueta
    el nombre de la estación, y su color se obtendrá a partir de la 
    función ```funcion_color``` que se pasa como parámetro
    ENTRADA
        :param estaciones: lista de estaciones disponibles
        :type estaciones: [Estacion(str, int, int, int, Coordenadas(float, float))]
        :param funcion_color: Función que se aplica a una estación y devuelve una cadena
            que representa el color en el que se dibuja el marcador
        :type funcion_color: function(Estacion)->str
    SALIDA
        :return: objeto mapa creado con los marcadores
        :rtype: folium.Map
    '''
    #Calculamos la media de las coordenadas de las estaciones, para poder centrar el 
    #mapa
    centro_mapa = media_coordenadas(estaciones)
    # creamos el mapa con folium
    mapa = crea_mapa(centro_mapa.latitud, centro_mapa.longitud, 13)

    for estacion in estaciones:
        etiqueta = estacion.nombre
        color = funcion_color(estacion)
        marcador = crea_marcador (estacion.ubicacion.latitud, estacion.ubicacion.longitud, etiqueta, color)
        marcador.add_to(mapa)
    
    return mapa

def guarda_mapa(mapa, ruta_fichero):
    '''Guard un mapa como archivo html

    :param mapa: Mapa a guardar
    :type mapa: folium.Map
    :param ruta_fichero: Nombre y ruta del fichero
    :type ruta_fichero: str
    '''
    mapa.save(ruta_fichero)
    # Abre el fichero creado en un navegador web
    webbrowser.open("file://" + os.path.realpath(ruta_fichero))

# Ejercicio3.1
def color_azul(estacion):   
   '''Función que devuelve siempre azul
   ENTRADA
      :param estacion: Estación para la que quiero averiguar el color
      :type estacion: Estacion(str, int, int, int, Coordenadas(float, float))
   SALIDA
      :return: El color azul
      :rtype: str
   '''
   if estacion > 0:
       res = "blue"
   return res 

# mapa_estaciones = crea_mapa_estaciones(estaciones_sevici, color_azul)
# guarda_mapa(mapa_estaciones, "./out/azul.html"))

def obten_color_bicis_disponibles(estacion):
    '''Función que devuelve "red" si la estación no tiene bicis disponibles, y verde en caso contrario 
    ENTRADA
      :param estacion: Estacion para la que quiero averiguar el color
      :type estacion: Estacion(str, int, int, int, Coordenadas(float, float))
    SALIDA
      :return: "red" o "green" dependiendo de si la estación tiene bicis disponibles o no
      :rtype: str
    '''
    res="red"
    if estacion.bicis_disponibles>0:
        res="green"
    return res

# mapa_estaciones = crea_mapa_estaciones(estaciones_sevici, obten_color_bicis_disponibles)
# guarda_mapa(mapa_estaciones, "./out/estaciones_bicis_disponibles.html")