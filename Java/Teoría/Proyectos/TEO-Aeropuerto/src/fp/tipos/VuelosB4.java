package fp.tipos;

import java.time.LocalDate;
import java.util.Comparator;
import java.util.List;
import java.util.OptionalDouble;
import java.util.Set;
import java.util.SortedSet;
import java.util.TreeSet;
import java.util.function.Predicate;
import java.util.stream.Collectors;

public class VuelosB4 extends Vuelos {

	public VuelosB4(String nombre, List<Vuelo> vuelos) {
		super(nombre, vuelos);
	}
	
	// Dado un destino, ¿existe algún vuelo con ese destino?
	// Existe -> anyMatch
	
//	public Boolean existeVueloDestino(String destino) {
//		return getVuelos().stream()
//				.filter(x -> x.getDestino().equals(destino))
//				.map(Vuelo::getDestino)
//				.collect(Collectors.toList())
//				.contains(destino);
//	}
	
	public Boolean getExisteVueloDestino(String destino) {
		Predicate<Vuelo> predicado = 
				v -> v.getDestino()
				.equals(destino);
		return getVuelos().stream()
				.anyMatch(predicado);
	}
	
	// Dado un número n devuelve cierto si todos los vuelos tienen al 
	// menos n pasajeros.
	// ¿Todos cumplen la condición? -> allMatch
	
	public Boolean todosVuelosNPasajeros(Integer n) {
		Predicate<Vuelo> pred = 
				v -> v.getNumPasajeros() >= n;
				
		return getVuelos()
				.stream()
				.allMatch(pred);
	}
	
	// Dada una fecha, ¿cuántos vuelos hay ese día?.
	// Contador con filtro:
	// filter (intermedia) + count (terminal)
	
	public Integer getNumVuelosFecha(LocalDate fecha) {
		return (int) getVuelos().stream()
				.filter(v -> v.getFecha().equals(fecha))
				.count();
	}
	
	// Dada una fecha devuelve una lista con los vuelos 
	// posteriores a esa fecha.
	// filter + collect
	
	public List<Vuelo> getVuelosPosterioresFecha(LocalDate fecha) {
		return getVuelos().stream()
				.filter(v -> v.getFecha().isAfter(fecha))
				.collect(Collectors.toList());
	}
	
	// Dada una fecha devuelve un conjunto con los destinos de los 
	// vuelos anteriores a esa fecha.
	
	public Set<Vuelo> getVuelosAnterioresFecha(LocalDate fecha) {
		return getVuelos().stream()
				.filter(v -> v.getFecha().isBefore(fecha))
				.collect(Collectors.toSet());
	}
	
	public SortedSet<Vuelo> getVuelosAnterioresFechaOrdenados(LocalDate fecha) {
		return getVuelos().stream()
				.filter(v -> v.getFecha().isBefore(fecha))
				.collect(Collectors.toCollection(TreeSet::new));
	}
	
	// Dado un conjunto de destinos devuelve el número de pasajeros a 
	// los destinos del conjunto.
	// Acumulador (sobre una propiedad) con filtro
	// Stream: filter + mapToInt + sum
	
	public Integer getNumPasajerosConDestino(Set<String> destinos) {
		return getVuelos().stream()
				.filter(v -> destinos.contains(v.getDestino()))
				.mapToInt(v -> v.getNumPasajeros())
				.sum();
	}
	
	// Dado un mes como un entero devuelve el precio medio de los vuelos 
	// de ese mes.
	// filter + average + mapToDouble + average
	
	public Double getPrecioMedioVuelosMes(Integer mes) {
		OptionalDouble opt = getVuelos().stream()
				.filter(v -> v.getFecha().getMonthValue() == mes)
				.mapToDouble(Vuelo::getPrecio)
				.average();
		// Opción 1: get
		// (si no se puede calcular lanza excepción)
		opt.getAsDouble();
		
		// Opción 2: orElse
		return opt.orElse(0.);
	}
	
	//	Dado un año como un entero devuelve la recaudación de los vuelos 
	//	de ese año. Suponga que todos los pasajeros pagan el mismo precio.
	
	
	
	// Devuelve el vuelo con mayor número de pasajeros. 
	// Si no se puede calcular devuelve null.
	
	public Vuelo getVueloMasPasajeros() {
		return getVuelos().stream()
				.max(Comparator.comparing(Vuelo::getNumPasajeros))
				.orElse(null);
	}
	
	// Dado un destino devuelve el código del vuelo de menor precio 
	// que vuela a ese destino. Eleva NoSuchElementException si no 
	// se puede calcular.
	
	// Filtrado
	// Mínimo (Propiedad precio)
	// Transformación map
	//		Vuelo -> String(codigo)
	
	public String getCodigoMenorPrecio(String destino) {
		return getVuelos().stream()
				// Stream<Vuelo>
				.filter(v -> v.getDestino().equals(destino))
				// Stream<Vuelo>
				.min(Comparator.comparing(Vuelo::getPrecio))
				// Optional<Vuelo>
				.map(Vuelo::getCodigo)
				// Optional<String>
				.get();
				// String
	}
	
	// Dado un número n devuelve una lista con los n vuelos más baratos.
	
	public List<Vuelo> getNVuelosMasBaratos(Integer n) {
		return getVuelos().stream()
				.sorted(Comparator.comparing(Vuelo::getPrecio))
				.limit(n)
				.collect(Collectors.toList());
	}
	
	// Dado un número n devuelve una lista con los n vuelos de mayor duración.
	
	public List<Vuelo> getNVuelosMasDuracion(Integer n) {
		return getVuelos().stream()
				.sorted(Comparator.comparing(Vuelo::getDuracion).reversed())
				.limit(n)
				.collect(Collectors.toList());
	}
	
	
	
}
