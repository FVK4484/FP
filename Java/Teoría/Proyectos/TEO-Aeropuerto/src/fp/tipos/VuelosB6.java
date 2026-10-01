package fp.tipos;

import java.time.LocalDate;
import java.util.Comparator;
import java.util.List;
import java.util.Map;
import java.util.Map.Entry;
import java.util.NoSuchElementException;
import java.util.Optional;
import java.util.SortedMap;
import java.util.TreeMap;
import java.util.stream.Collectors;

public class VuelosB6 extends Vuelos {

	public VuelosB6(String nombre, List<Vuelo> vuelos) {
		super(nombre, vuelos);
	}
	
	// 1. Método que devuelve un Map tal que a cada destino 
	// le hace corresponder un Optional con el vuelo más barato 
	// a ese destino.
	public Map<String, Optional<Vuelo>> getVueloMasBaratoPorDestino1() {
		return getVuelos().stream()
				.collect(Collectors.groupingBy(Vuelo::getDestino, 
						Collectors.minBy(Comparator.comparing(Vuelo::getPrecio))));
	}
	
	// 2. Método que devuelve un Map tal que a cada destino le hace 
	// corresponder el vuelo más barato a ese destino.
	public Map<String, Vuelo> getVueloMasBaratoPorDestino2() {
		return getVuelos().stream()
				.collect(Collectors.groupingBy(Vuelo::getDestino, 
						Collectors.collectingAndThen(Collectors.minBy(Comparator.comparing(Vuelo::getPrecio)), 
								opt -> opt.get())));
	}
	
	// 3. Método que devuelve un Map tal que a cada destino le hace
	// corresponder el código del Vuelo con el vuelo más barato a ese destino.
	public Map<String, String> getCodigoVueloMasBaratoPorDestino() {
		return getVuelos().stream()
				.collect(Collectors.groupingBy(Vuelo::getDestino, 
						Collectors.collectingAndThen(Collectors.minBy(Comparator.comparing(Vuelo::getPrecio)), 
								opt -> opt.get().getCodigo())));
	}
	
	// 4. Método que devuelve el destino con más vuelos. Si no se puede 
	// calcular eleva NoSuchElementException.
	public String getDestinoMasVuelos() {
		return getVuelos().stream()
				.collect(Collectors.groupingBy(Vuelo::getDestino, 
						Collectors.counting()))
				.entrySet().stream()
		//		.max(Map.Entry.comparingByValue())
				.max(Comparator.comparing(e -> e.getValue()))
	    //		.map(Map.Entry::getKey)
				.map(e -> e.getKey()) // Optional<String>
				.get();
	    //		.orElseThrow(NoSuchElementException::new);
	}
	
	// 5. Método que devuelve cuál es el segundo destino con más vuelos. 
	// Si no se puede calcular eleva NoSuchElementException.
	public String getSegundoDestinoMasVuelos() {
		Comparator<Entry<String, Long>> cmp = Comparator.comparing(Entry::getValue);
		return getVuelos().stream()
				.collect(Collectors.groupingBy(Vuelo::getDestino, 
						Collectors.counting()))
				.entrySet().stream()
				.sorted(cmp.reversed())
				.skip(1)
				.findFirst()
				.map(e -> e.getKey())
				.get();			
	}
	
	// 7. Método que devuelve un Map que a cada destino le haga corresponder el 
	// porcentaje de plazas de los vuelos a ese destino con respecto al total de plazas.
	public Map<String, Double> testGetPorcentajePlazasPorDestino() {
		
		Integer totalPlazas = getVuelos().stream()
				.mapToInt(Vuelo::getNumPlazas)
				.sum();
		
		return getVuelos().stream()
				.collect(Collectors.groupingBy(Vuelo::getDestino, 
						Collectors.collectingAndThen(Collectors.summingInt(Vuelo::getNumPlazas), 
								plazas -> plazas * 100. / totalPlazas)));				

	}
	
	public Map<String, Double> testGetPorcentajePlazasPorDestino2() {
		
		Integer totalPlazas = getVuelos().stream()
				.mapToInt(Vuelo::getNumPlazas)
				.sum();
		
		return getVuelos().stream()
				.collect(Collectors.groupingBy(Vuelo::getDestino, 
						Collectors.summingInt(Vuelo::getNumPlazas)))
				.entrySet().stream()
				.collect(Collectors.toMap(Entry::getKey, e -> e.getValue() * 100. / totalPlazas));				

	}
	
	// 9. Método que dado un entero que representa un año devuelve un SortedMap que relacione cada 
	// destino con el total de pasajeros a ese destino en el año dado como parámetro.
	public SortedMap<String, Integer> getNumPasajerosPorDestinoDeAnyo(Integer anyo) {
		return getVuelos().stream()
				.filter(V -> V.getFecha().getYear() == anyo)
				.collect(Collectors.groupingBy(Vuelo::getDestino, 
					 // TreeMap::new,
						() -> new TreeMap<>(Comparator.reverseOrder()),
						Collectors.summingInt(Vuelo::getNumPasajeros)));
	}
	
	// 10. Método que devuelve un Map tal que dado un entero n haga corresponder a cada fecha la lista 
	// de los n destinos distintos de los vuelos de mayor duración.
	public Map<LocalDate, List<String>> getNDestinosMayorDuracionPorFecha(Integer n) {
		return getVuelos().stream()
				.collect(Collectors.groupingBy(Vuelo::getFecha, 
						Collectors.collectingAndThen(Collectors.toList(), 
								lista -> getNDestinosMasDuracion(lista, n))));
				
	}

	private List<String> getNDestinosMasDuracion(List<Vuelo> lista, Integer n) {
		return lista.stream()
				.sorted(Comparator.comparing(Vuelo::getDuracion).reversed())
				.map(Vuelo::getDestino)
				.distinct()
				.limit(n)
				.collect(Collectors.toList());
	}
	
}
