package fp.tipos;

import java.time.LocalDate;
import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;
import java.util.List;

public class VuelosB2 extends Vuelos{

	public VuelosB2(String nombre, List<Vuelo> vuelos) {
		super(nombre, vuelos);
	}
	
	// Catálogo tratamientos secuenciales:
	// - (Boolean) Existe algún elemento que cumpla una condición.
	// - (Boolean) Todos los elementos cumplen una condición.
	// - (Integer) Contador.
	// - (Integer / Double) Acumulador.
	// - (Double) Calcular media.
	// - (Collection<T>) Filtrado con selección.
	// - (T) Máximo/Mínimo.
	
	// Dada una cadena de caracteres con un destino
	// devuelve el total de pasajeros a ese destino.
	
	// Acumulador
	
	public Integer getNumPasajerosDestino(String destino) {
		Integer res = 0;
		for (Vuelo v : getVuelos()) {
			if (v.getDestino().equals(destino)) {
				res += v.getNumPasajeros();
			}
		}
		return res;
	}
	
	public Integer getNumPasajerosDestinoPrefijo(String s) {
		Integer res = 0;
		for (Vuelo v : getVuelos()) {
			if (v.getDestino().startsWith(s)) {
				res += v.getNumPasajeros();
			}
		}
		return res;
	}
	
	
	
	public Double getRecaudacionDestino(String destino) {
		Double res = 0.0;
		for (Vuelo v : getVuelos()) {
			if (v.getDestino().equals(destino)) {
				res += v.getPrecio() * v.getNumPasajeros();
			}
		}
		return res;	
	}
	
	public Vuelo getPrimerVueloDestino(String destino) {
		List<Vuelo> res = new ArrayList<>();
		for (Vuelo v : getVuelos()) {
			if (v.getDestino().equals(destino)) {
				res.add(v);
			}
		}
		return Collections.min(res, Comparator.comparing(Vuelo::getFecha));
	}
	
	public Vuelo getPrimerVueloDestinoMenorPrecio(String destino) {
		List<Vuelo> res = new ArrayList<>();
		for (Vuelo v : getVuelos()) {
			if (v.getDestino().equals(destino)) {
				res.add(v);
			}
		}
		Collections.sort(getVuelos(), Comparator.comparing(Vuelo::getFecha).thenComparing(Vuelo::getPrecio));
		return res.getFirst();
	}
	
	public Boolean existeVueloMenorPrecio(Double precio) {
		Boolean res = false;
		for (Vuelo v : getVuelos()) {
			if (v.getPrecio() < precio) {
				res = true;
				break;
			}
		}
		return res;
	}
	
	public Boolean estanTodosPorcentajeMayor(Double porcentaje) {
		Boolean res = true;
		for (Vuelo v : getVuelos()) {
			Double p = v.getNumPasajeros() * 100. / v.getNumPlazas();
			if (p < porcentaje) {
				res = false;
				break;
			}
		}
		return res;
	}
	
	public Double getPrecioMedioVuelosPosteriores(LocalDate fecha) {
		Double suma = 0.;
		Integer cont = 0;
		for (Vuelo v : getVuelos()) {
			if (v.getFecha().isAfter(fecha)) {
				// v.getFecha().compareTo(fecha) > 0
				suma += v.getPrecio();
				cont ++;
			}
		}
		Double res = 0.;
		if (cont < 0) {
			res = suma / cont;
		}
		return res;
	}
}
