package fp.vinos;

import java.util.ArrayList;
import java.util.Collection;
import java.util.HashSet;
import java.util.Set;

import fp.utiles.Checkers;

public class VinotecaBucles implements Vinoteca {
	
	private Collection<Vino> vinos;

	public VinotecaBucles(Collection<Vino> vinos) {
		this.vinos = new ArrayList<Vino>(vinos);
	}
	
	public String toString() {
		return "Total de vinos: " + vinos.size();
	}

	// OPERACIONES 
	
	public Integer calcularNumeroVinosDePais(String pais) {
		Integer numVinos = 0;
		for (Vino vino : vinos) {
			if (vino.pais().equals(pais)) {
				numVinos++;
			}
		}
		return numVinos;
	}

	public Collection<Vino> obtenerVinosRangoPuntos(Integer inf, Integer sup) {
		Checkers.check("El valor del límite inferior del rango es superior al valor del límite superior.", 
				inf <= sup);
		Collection<Vino> coleccion = new HashSet<Vino>();
		for (Vino vino : vinos) {
			if (vino.puntos() >= inf && vino.puntos() <= sup) {
				coleccion.add(vino);
			}
		}
		return coleccion;
	}

	public Integer calcularNumeroVinosDePaisConPuntuacionSuperior(String pais, Integer umbral) {
		Integer numVinos = 0;
		for (Vino vino : vinos) {
			if (vino.pais().equals(pais) && vino.puntos() > umbral) {
				numVinos++;
			}
		}
		return numVinos;
	}

	public Set<Vino> obtenerVinosBaratos(Double precio) {
		Set<Vino> conjVinos = new HashSet<Vino>();
		for (Vino vino : vinos) {
			if (vino.precio() < precio) {
				conjVinos.add(vino);
			}
		}
		return conjVinos;
	}

	public Boolean existeVinoDeUvaEnRegion(String region, String uva) {
		Boolean result = false;
		for (Vino vino : vinos) {
			if (vino.region().equals(region) && vino.uva().equals(uva)) {
				result = true;
				break;
			}
		}
		return result;
	}

}
