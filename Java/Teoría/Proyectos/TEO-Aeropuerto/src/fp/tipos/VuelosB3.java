package fp.tipos;

import java.time.LocalDate;
import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;
import java.util.HashMap;
import java.util.HashSet;
import java.util.List;
import java.util.Map;
import java.util.Set;
import java.util.SortedSet;
import java.util.TreeSet;

public class VuelosB3 extends Vuelos{
	
	public VuelosB3(String nombre, List<Vuelo> vuelos) {
		super(nombre, vuelos);
	}
	
//	1. Devuelve un Map que asigne a cada destino el número de vuelos.
	
	public Map<String, Integer> getNumVuelosPorDestino() {
		Map<String, Integer> res = new HashMap<>();
		for (Vuelo v : getVuelos()) {
			String clave = v.getDestino();
			if (res.containsKey(clave)) {
				Integer valor = res.get(clave);
				valor += 1;
				res.put(clave, valor);
			} else {
				res.put(clave, 1);
			}
		}
		return res;
	}
	
//	2. Devuelve un Map que asigne a cada fecha el número de pasajeros.
	
	public Map<LocalDate, Integer> getNumPasajerosFecha() {
		Map<LocalDate, Integer> res = new HashMap<>();
		for (Vuelo v : getVuelos()) {
			LocalDate clave = v.getFecha();
			if (res.containsKey(clave)) {
				Integer valor = res.get(clave);
				valor += v.getNumPasajeros();
				res.put(clave, valor);
			} else {
				res.put(clave, v.getNumPasajeros());
			}
		}
		return res;
		
	}
	
//	3. Devuelve un Map que asigne a cada destino una lista con los códigos de los vuelos a ese destino.
	
	public Map<String, List<String>> getCodigosPorDestino() {
		Map<String, List<String>> res = new HashMap<>();
		for (Vuelo v : getVuelos()) {
			String clave = v.getDestino();
			if (res.containsKey(clave)) {
//				List<String> valor = res.get(clave);
//				valor.add(v.getCodigo());
//				res.put(clave, valor);
				res.get(clave).add(v.getCodigo());
			} else {
				List<String> l = new ArrayList<>();
				l.add(v.getCodigo());
				res.put(clave, l);
			}
		}
		return res;
	}
	
//	4. Devuelve un Map que asigne a cada destino la fecha máxima de vuelos a ese destino con plazas libres.
//	Map que calcula el máximo.
	
	public Map<String, LocalDate> getFechaMaximaPorDestino() {
		Map<String, LocalDate> res = new HashMap<>();
		for (Vuelo v : getVuelos()) {
			if (!v.getEstaCompleto()) {
				String clave = v.getDestino();
				if (res.containsKey(clave)) {
					LocalDate valorMax = res.get(clave);
					if (v.getFecha().isAfter(valorMax)) {
						res.put(clave, v.getFecha());
					}
				} else {
					res.put(clave, v.getFecha());
				}
			}
		}
		return res;
	}
	
	public String getDestinoFechaMaximaTotal() {
		Map<String, LocalDate> fechaMaxPorDestino = getFechaMaximaPorDestino();
		
//		Set<Map.Entry<String, LocalDate>> entries = fechaMaxPorDestino.entrySet();
		
		Map.Entry<String, LocalDate> res = null;
		for (Map.Entry<String, LocalDate> entry : fechaMaxPorDestino.entrySet()) {
			if (res == null || entry.getValue().isAfter(res.getValue())) {
				res = entry;
 			}
		}
		return res.getKey();
	}
	
//	5. Dado un destino devuelve un SortedSet con las fechas de los vuelos a ese destino.
	
	public SortedSet<LocalDate> getConjOrdVuelosPorFecha(String destino) {
		SortedSet<LocalDate> conjunto = new TreeSet<>(Comparator.reverseOrder());
		for (Vuelo v : getVuelos()) {
			if (v.getDestino().equals(destino)) {
				conjunto.add(v.getFecha());
			}
		}
		return conjunto;
	}
	
//	6. Devuelve un SortedSet con todos los vuelos ordenados por fecha.
	
	public SortedSet<Vuelo> getConjOrdVuelosPorFecha() {
		Comparator<Vuelo> cmp = Comparator
				.comparing(Vuelo::getFecha
						// v -> v.getFecha()
							) // Por defecto: menor a mayor
				.reversed() // Reversed: mayor a menor
				.thenComparing(Comparator.naturalOrder());
		
		SortedSet<Vuelo> conjunto = new TreeSet<>(cmp);
		for (Vuelo v : getVuelos()) {
			conjunto.add(v);
		}
		return conjunto;
	}
	
//	7. Devuelve un SortedSet con todos los vuelos ordenados por orden alfabético de destino.
	
	public SortedSet<Vuelo> getVuelosOrdenadosPorOrdenAlfabeticoDeDestino() {
		Comparator<Vuelo> cmp = Comparator
				.comparing(Vuelo::getDestino);
		SortedSet<Vuelo> conjOrdVuelos = new TreeSet<Vuelo>(cmp);
		for (Vuelo vuelo : getVuelos()) {
			conjOrdVuelos.add(vuelo);
		}
		return conjOrdVuelos;
	}
	
//	10. Implemente un método que devuelva cuál es el destino con más vuelos.
	
	public String getDestinoMasVuelos() {
		Map<String, Integer> mpAux = 
				getNumVuelosPorDestino();
		
		Set<Map.Entry<String, Integer>> eset =
				mpAux.entrySet();
		
		Comparator<Map.Entry<String, Integer>> cmp = 
				Comparator
				.comparing( // Map.Entry::getValue
						e -> e.getValue());
		
		Map.Entry<String, Integer> eMax = Collections.max(eset, cmp);
		
		return eMax.getKey();
	}
	
}
