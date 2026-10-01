package fp.vinos;

import java.util.Collection;
import java.util.Set;

public interface Vinoteca {
	
	//	Vinoteca::calcularNumeroVinosDePais: cuenta el número de vinos 
	//	de un país dado como parámetro.
	
	Integer calcularNumeroVinosDePais(String pais);
	
	//	Vinoteca::obtenerVinosRangoPuntos: devuelve una colección de 
	//	objetos de tipo Vino solo con los vinos que estén valorados en un 
	//	rango de puntos determinado. El rango vendrá especificado por dos 
	//	enteros (inf y sup) dados como parámetros. Si el valor del límite 
	//	inferior del rango es superior al valor del límite superior, se 
	//	elevará IllegalArgumentException.
	
	Collection<Vino> obtenerVinosRangoPuntos(Integer inf, Integer sup);
	
	//	Vinoteca::calcularNumeroVinosDePaisConPuntuacionSuperior: devuelve 
	//	el número de vinos del país dado como parámetro que tienen una 
	//	puntuación superior a un umbral dado como parámetro.
	
	Integer calcularNumeroVinosDePaisConPuntuacionSuperior(String pais, Integer umbral);
	
	//	Vinoteca::obtenerVinosBaratos: obtiene un conjunto con los vinos 
	//  cuyo precio es inferior a uno dado como parámetro.
	
	Set<Vino> obtenerVinosBaratos(Double precio);
	
	//	Vinoteca::existeVinoDeUvaEnRegion: devuelve true si existe en la región dada como parámetro un vino elaborado con la uva dada como parámetro.
	
	Boolean existeVinoDeUvaEnRegion(String region, String uva);

	Object calcularTotalPuntosVinosDeRegion(String region);
	
}
