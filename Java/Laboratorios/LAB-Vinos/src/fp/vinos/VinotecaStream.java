package fp.vinos;

import java.util.ArrayList;
import java.util.Collection;
import java.util.Set;
import java.util.function.Predicate;
import java.util.stream.Collectors;

import fp.utiles.Checkers;

public class VinotecaStream implements Vinoteca {
	
	private Collection<Vino> vinos;

	public VinotecaStream(Collection<Vino> vinos) {
		this.vinos = new ArrayList<Vino>(vinos);
	}

	public String toString() {
		return "Total de vinos: " + vinos.size();
	}

	// OPERACIONES 
	
	public Integer calcularNumeroVinosDePais(String pais) {
		Predicate<Vino> pred = vino -> vino.pais().equals(pais);
		Long result = vinos.stream()
				.filter(pred)
				.count();
		return result.intValue();
	}

	public Collection<Vino> obtenerVinosRangoPuntos(Integer inf, Integer sup) {
		Checkers.check("El valor del límite inferior del rango es superior al valor del límite superior.", 
				inf <= sup);
		Predicate<Vino> pred = vino -> vino.puntos() >= inf && vino.puntos() <= sup;
		return vinos.stream()
				.filter(pred)
				.toList();
	}

	public Integer calcularNumeroVinosDePaisConPuntuacionSuperior(String pais, Integer umbral) {
		Predicate<Vino> pred = vino -> vino.pais().equals(pais) && vino.puntos() > umbral;
		Long result = vinos.stream().filter(pred).count();
		return result.intValue();
	}

	public Set<Vino> obtenerVinosBaratos(Double precio) {
		Predicate<Vino> pred = vino -> vino.precio() < precio;
		return vinos.stream()
				.filter(pred)
				.collect(Collectors.toSet());
	}

	public Boolean existeVinoDeUvaEnRegion(String region, String uva) {
		Predicate<Vino> pred = vino -> vino.uva().equals(uva) && vino.region().equals(region);
		return vinos.stream().anyMatch(pred);
	}
	
}
