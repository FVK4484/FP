package fp.tipos;

import java.time.Duration;
import java.util.Comparator;
import java.util.List;
import java.util.SortedMap;
import java.util.TreeMap;
import java.util.stream.Collectors;

public class AgenciaBus {
	private String nombre;
	private List<Viaje> viajes;
	
	public Duration getMaximaDuracion() {
		return viajes.stream()
				.max(Comparator.comparing(Viaje::getNumeroParadas))
				.map(Viaje::getDuracion)
				.orElse(Duration.ZERO);
	}
	
	public void añadirTiempoDescanso(String parada, Integer minutos) {
		viajes.stream()
		.filter(v -> v.getParadas().contains(parada))
		.forEach(v -> v.getDuracion().plusMinutes(minutos));
	}
	
	public SortedMap<String, Duration> getDuracionMinimaPorDestino(TipoViaje tipo) {
		return viajes.stream()
				.filter(v -> v.getTipoViaje().equals(tipo))
				.collect(Collectors.groupingBy(v -> v.getDestino(),
						TreeMap::new,
						Collectors.collectingAndThen(
								Collectors.minBy(Comparator.comparing(Viaje::getDuracion)),
								o -> o.get().getDuracion())));
	}
}

//SortedMap<String, Duration> getDuracionMinimaPorDestino(TipoViaje tipo): Devuelve un SortedMap<String, Duration> que relaciona los 
//destinos de los viajes del tipo dado como parámetro con la duración del viaje de menor duración a dicho destino. Las claves estarán 
//ordenadas en orden alfabético. (1,5 puntos)