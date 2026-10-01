package fp.tipos;

import java.time.Duration;
import java.time.LocalDate;
import java.util.ArrayList;
import java.util.Comparator;
import java.util.HashMap;
import java.util.Map;
import java.util.Map.Entry;
import java.util.SortedSet;
import java.util.TreeSet;
import java.util.function.BinaryOperator;
import java.util.stream.Collectors;
import java.util.stream.Stream;

import java.util.List;

public class Competicion {
	private SortedSet<Visita> visitas;
	
	private static final Comparator<Visita> CMP_CP =
			Comparator.comparing(Visita::getCp)
			.thenComparing(Comparator.naturalOrder());
	
	public SortedSet<Visita> getVisitas() {
		SortedSet<Visita> ss = new TreeSet<>(CMP_CP);
		ss.addAll(visitas);
		return ss;
	}
	
	public Competicion(Stream<Visita> stream) {
		this.visitas = stream.collect(Collectors.
				toCollection(() -> new TreeSet<>(CMP_CP)));
	}
	public SortedSet<String> getEmailsOrdenados(Duration d) {
		Double temperaturaMedia = getVisitas().stream()
				.mapToDouble(Visita::getTemperatura)
				.average()
				.getAsDouble();
		
		return getVisitas().stream()
				.filter(v -> v.getTiempoTranscurrido()
						.compareTo(d) > 0
						&& v.getTemperatura()
						.compareTo(temperaturaMedia) < 0)
				.map(Visita::getEmail)
				.collect(Collectors.toCollection(TreeSet::new));
		}
	
	public Integer getTotalVisitasComilones(){
		Double mediaVisitas = getVisitas().stream()
		.mapToInt(Visita::getNumEvaluaciones)
		.average()
		.getAsDouble();
		
		Long res = getVisitas().stream()
				.filter(v -> v.getNumEvaluaciones()>mediaVisitas)
				.count();
				return res.intValue();
	}
	
////String getPeorHamburgueseriaPorCalidadIngredientes(): devuelve el nombre de la hamburguesería con la peor puntuación promedio 
//en la categoría de calidad de ingredientes. Si no se puede calcular, devuelve null. (1.5 ptos)
	private Map<String, Double> getMediaIngredientesHamburgueseria(){
		return getVisitas().stream()
				.flatMap(v -> v.getEvaluaciones().stream())
				.collect(Collectors.groupingBy(Evaluacion::hamburgueseria, 
						Collectors.averagingInt(Evaluacion::calidad_ingredientes)));
		}

	public String getPeorHamburgueseriaPorCalidadIngredientes() {
		return getMediaIngredientesHamburgueseria().entrySet().stream()
				.min(Comparator.comparing(Map.Entry::getValue))
				.map(Map.Entry::getKey)
				.orElse(null);
		}
	
////Map<String, String> getTopComilonPorCPEnDia(LocalDate d): teniendo solamente en cuenta las visitas del día d, 
//devuelve un Map en el que a cada código postal le hace corresponder el email de la persona que realizó 
//la visita en la que se comieron más hamburguesas. Si hay dos visitas en las que se comió el mismo número 
//de hamburguesas, se devolverá la que tiene una fecha de entrada más tardía. Tenga en cuenta que una persona 
//hace como máximo una visita al día. (1.5 ptos)
	public Map<String, String> getTopComilonPorCPEnDia(LocalDate dia) {
		Comparator<Visita> cmp = Comparator.comparing(Visita::getNumEvaluaciones)
				.thenComparing(Visita::getEntrada);
		return getVisitas().stream()
				.filter(v -> v.getEntrada().toLocalDate().equals(dia))
				.collect(Collectors.groupingBy(
						Visita::getCp, 
						Collectors.collectingAndThen(
								Collectors.maxBy(cmp), 
								o -> o.get().getEmail())));
		}
	
////String getHamburgueseriaGanadora(): devuelve el nombre de la hamburguesería ganadora. 
//Se considera hamburguesería ganadora a aquella que ha obtenido la mayor puntuación promedio 
//basada en las puntuaciones finales de las visitas registradas. Implemente este método con bucles. (2 ptos)
	public String getHamburgueseriaGanadora() {
		String res = null;
		Double puntuacionMax = null;
		Map<String, List<Double>> mAux = getPuntuacionesHamburgueseria();
		for (Entry<String, List<Double>> e: mAux.entrySet()) {
			Double media = media(e.getValue());
			if (res == null || media > puntuacionMax) {
				res = e.getKey();
				puntuacionMax = media;
				}
			}
		return res;
		}
	public String getHamburgueseriaGanadora2() {
		Map<String, List<Double>> mAux = getPuntuacionesHamburgueseria();
		Entry<String, List<Double>> res = null;
		BinaryOperator<Map.Entry<String, List<Double>>> bo = 
				BinaryOperator.maxBy(Comparator.comparing( e -> media(e.getValue()) ));
		for (Entry<String, List<Double>> e: mAux.entrySet()) {
			if (res == null) {
				res = e;
			} else {
				res = bo.apply(res, e);
				}
			}
		return res.getKey();
		}
	private Map<String, List<Double>> getPuntuacionesHamburgueseria() {
		Map<String, List<Double>> mAux = new HashMap<>();
		for (Visita v: getVisitas()) {
			for (Evaluacion e: v.getEvaluaciones()) {
				String clave = e.hamburgueseria();
				if (mAux.containsKey(clave)) {
					mAux.get(clave).add(e.puntuacion_final());
				} else {
					List<Double> l = new ArrayList<Double>();
					l.add(e.puntuacion_final());
					mAux.put(clave, l);
					}
				}
			}
		return mAux;
		}
	private Double media(List<Double> lista) {
		Double res = 0.0;
		if (!lista.isEmpty()) {
			for (Double n: lista) {
				res += n;
				}
			res = res / lista.size();
			}
		return res;
		}
}
