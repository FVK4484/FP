package fp.tipos;

import java.time.LocalDate;
import java.util.ArrayList;
import java.util.Comparator;
import java.util.List;
import java.util.Map;
import java.util.Objects;
import java.util.SortedMap;
import java.util.TreeMap;
import java.util.function.Predicate;
import java.util.stream.Collectors;
import java.util.stream.Stream;

public class EstadisticasEncuestas {
	private List<Encuesta> encuestas;

	public EstadisticasEncuestas(Stream<Encuesta> encuestas) {
		this.encuestas = encuestas.collect(Collectors.toList());
	}

	public List<Encuesta> getEncuestas() {
		return new ArrayList<>(encuestas);
	}

	public String toString() {
		return "EstadisticasEncuestas [encuestas=" + encuestas + "]";
	}

	public int hashCode() {
		return Objects.hash(encuestas);
	}

	public boolean equals(Object obj) {
		if (this == obj)
			return true;
		if (obj == null)
			return false;
		if (getClass() != obj.getClass())
			return false;
		EstadisticasEncuestas other = (EstadisticasEncuestas) obj;
		return Objects.equals(encuestas, other.encuestas);
	}
	
	public Double getMediaNumEncuestadosConsultorayFecha(String consultora, LocalDate fechaMaxima) { 
		return encuestas.stream()
				.filter(e -> e.getNombre().equals(consultora) && e.getFechaFin().isBefore(fechaMaxima))
				.mapToInt(Encuesta::getNumeroEncuestados)
				.average()
				.orElse(0.);
	}
	
//	2. Encuesta getEncuestaMasEncuestadosPorDia(TipoEncuesta tipo): Devuelve la encuesta, del tipo dado como parámetro, que tiene un 
//	mayor ratio de número de encuestados por día de duración. Si no se puede calcular, se eleva la excepción NoSuchElementException (1 pto)
	
	public Encuesta getEncuestaMasEncuestadosPorDia(TipoEncuesta tipo) {
		Predicate<Encuesta> pred = encuesta -> encuesta.getTipoEncuesta().equals(tipo);
		Comparator<Encuesta> comp = Comparator.comparing(Encuesta::getRatioEncuestadosDia);
		return encuestas.stream()
				.filter(pred)
				.max(comp)
				.get();
	}
	
//	3. List<String> getPartidosMasFrecuentesOrdenados(Integer n): Dado un valor n, devuelve una lista con los n partidos que más veces aparecen en 
//	las encuestas ordenados de mayor a menor número de apariciones. (1,5 ptos)
	
	public List<String> getPartidosMasFrecuentesOrdenados(Integer n) {
		Map<String, Long> contarPartidos = 
				encuestas.stream()
				.flatMap(encuesta -> encuesta.getResultados().stream())
				.collect(Collectors.groupingBy(
						Resultado::partido, Collectors.counting()));
		Comparator<Map.Entry<String, Long>> c = Map.Entry.comparingByValue();
		
		return contarPartidos.entrySet().stream()
				.sorted(c.reversed())
				.limit(n)
				.map(Map.Entry::getKey)
				.toList();
	}
	
//	4. SortedMap<String, Boolean> getSuperaEncuestadosPorPais(Integer umbral): Devuelve un SortedMap, cuyas claves están ordenadas por orden natural, 
//	en el que a cada país le hace corresponder un Boolean con un valor de True si todas las encuestas de ese país tienen un número de encuestados 
//	superior al umbral dado como parámetro. (1,75 pto)
	
	public SortedMap<String, Boolean> getSuperaEncuestadosPorPais(Integer umbral) {
		return encuestas.stream()
				.collect(Collectors.groupingBy(
						Encuesta::getPais,
						TreeMap::new,
						Collectors.collectingAndThen(
								Collectors.toList(), encuestas -> todasEncuestasSuperanUmbral(
										encuestas, umbral))));
	}
	
	private Boolean todasEncuestasSuperanUmbral(List<Encuesta> encuestas, Integer umbral) {
		return encuestas.stream()
				.allMatch(e -> e.getNumeroEncuestados() > umbral); 
	} 
	
}
