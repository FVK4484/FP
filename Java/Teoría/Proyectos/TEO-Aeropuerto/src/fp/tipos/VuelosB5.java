package fp.tipos;

import java.time.LocalDate;
import java.util.Comparator;
import java.util.List;
import java.util.Map;
import java.util.Set;
import java.util.SortedSet;
import java.util.TreeSet;
import java.util.stream.Collectors;

public class VuelosB5 extends Vuelos {

	public VuelosB5(String nombre, List<Vuelo> vuelos) {
		super(nombre, vuelos);
	}
	
	// 1. Dada una fecha f devuelve el número de destinos 
	// diferentes de todos los vuelos de esa fecha.
	public Integer getNumDestinosDiferentesFecha(LocalDate f) {
		return getVuelos().stream()
				.filter(v -> v.getFecha().equals(f))
				.map(v -> v.getDestino())
				.distinct()
				.collect(Collectors.collectingAndThen(Collectors.counting(), Long::intValue));
	}
	
	// 2. Devuelve un conjunto ordenado con los vuelos ordenados 
	// por el orden natural del tipo.
	public SortedSet<Vuelo> getVuelosOrdenados() {
		return getVuelos().stream()
				.collect(Collectors.toCollection(TreeSet::new));
	}	
	
	// 3. Dada una letra devuelve un conjunto ordenado alfabéticamente 
	// de manera ascendente con los destinos que empiezan por esa letra.
	public SortedSet<String> getDestinosOrdenados(Character l) {
		return getVuelos().stream()
				.filter(v -> l.equals(v.getDestino().charAt(0)))  // v.getDestino().startsWith(l))
				.map(Vuelo::getDestino)
				.collect(Collectors.toCollection(TreeSet::new));
	}
	
	// 4. Devuelve un conjunto ordenado por longitud de caracteres con 
	// los destinos de todos los vuelos.
	public SortedSet<String> getDestinosOrdenadosPorLongitud() {
		Comparator<String> cmp = Comparator
				.comparing(String::length)
				.thenComparing(Comparator.naturalOrder());
		return getVuelos().stream()
				.map(Vuelo::getDestino)
				.collect(Collectors.toCollection(() -> new TreeSet<>(cmp)));
	}
	
	// 5. Usa el método collect junto con la clase Collectors para los 
	// siguientes ejercicios que ya hemos resuelto de otra manera:
	
	
	
	// MAP
	
	// 1. Devuelve un Map que a cada fecha le haga corresponder una 
	// lista con sus vuelos.
	public Map<LocalDate, List<Vuelo>> getVuelosPorFecha() {
		return getVuelos().stream()
				.collect(Collectors.groupingBy(Vuelo::getFecha, 
						Collectors.toList()));
	}
	
	// 2. Devuelve un Map que a cada fecha le haga corresponder un conjunto 
	// con sus vuelos.
	public Map<LocalDate, Set<Vuelo>> getVuelosPorFecha2() {
		return getVuelos().stream()
				.collect(Collectors.groupingBy(Vuelo::getFecha, 
						Collectors.toSet()));
	}
		
	// 3. Devuelve un Map que a cada fecha le haga corresponder el número de 
	// vuelos.
	public Map<LocalDate, Integer> getNumVuelosPorFecha() {
		return getVuelos().stream()
				.collect(Collectors.groupingBy(Vuelo::getFecha, 
						Collectors.collectingAndThen(Collectors.counting(), Long::intValue)));
	}
	
	// 4. Devuelve un Map que a cada destino le haga corresponder 
	// el número total de plazas.
	public Map<String, Integer> getNumPlazasPorDestino() {
		return getVuelos().stream()
				.collect(Collectors.groupingBy(Vuelo::getDestino, 
						Collectors.summingInt(Vuelo::getNumPasajeros)));
	}
	
	// 5. Devuelve un Map que a cada destino le haga corresponder el precio medio de sus vuelos.
	public Map<String, Double> getPrecioMedioPorDestino() {
		return getVuelos().stream()
				.collect(Collectors.groupingBy(Vuelo::getDestino, 
						Collectors.averagingDouble(Vuelo::getPrecio)));
	}
	
	// 6. Devuelve un Map que a cada destino le haga corresponder un conjunto con las fechas 
	// de los vuelos a ese destino.
	public Map<String, Set<LocalDate>> getFechasPorDestino() {
		return getVuelos().stream()
				.collect(Collectors.groupingBy(Vuelo::getDestino, 
						Collectors.mapping(Vuelo::getFecha, Collectors.toSet())));
	}
	
	public Map<String, List<String>> getTripulacionPorDestino() {
		return getVuelos().stream()
				.collect(Collectors.groupingBy(Vuelo::getDestino, 
						Collectors.flatMapping(v -> v.getTripulacion().stream(), Collectors.toList())));
	}
	
}
