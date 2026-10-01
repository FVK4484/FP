package fp.tipos;

import java.util.ArrayList;
import java.util.Collection;
import java.util.Collections;
import java.util.List;
import java.util.Objects;

public class Vuelos {
	private String nombre;
	private List<Vuelo> vuelos;
	
	public Vuelos(String nombre, List<Vuelo> vuelos) {
		
		this.nombre = nombre;
		this.vuelos = new ArrayList<>(vuelos);
		
	}
	public String getNombre() {
		return nombre;
	}
	public List<Vuelo> getVuelos() {
		return new ArrayList<>(vuelos);
	}
	
	public Integer getNumeroVuelos() {
		return vuelos.size();
	}
	
	public Integer getNumeroPasajeros() {
		Integer numPasajeros = 0;
		for (Vuelo v : vuelos) {
			numPasajeros += v.getNumPasajeros();
		}
		return numPasajeros;
	}
	
	public Double getPrecioMedio() {
		if (vuelos.isEmpty()) {
			return 0.0;
		}
		Double precio = 0.0;
		for (Vuelo v : vuelos) {
			precio += v.getPrecio();
		}
		return precio / vuelos.size();
	}
	
	public Integer getNumeroDestinos() {
		List<String> res = new ArrayList<>();
		for (Vuelo v : vuelos) {
			if (res.contains(v.getDestino())) {
				continue;
			} else {
				res.add(v.getDestino());
			}
		}
		return res.size();
	}
	
	public String toString() {
	    if (vuelos.isEmpty()) {
	        return ""; 
	    }

	    String resultado = "";
	    
	    for (Vuelo v : vuelos) {
	        resultado += v.toString() + "\n"; 
	    }
	
	    // Borramos el último carácter (\n) usando substring
	    return resultado.substring(0, resultado.length() - 1);
	}

	public int hashCode() {
		return Objects.hash(nombre, vuelos);
	}

	public boolean equals(Object obj) {
		if (this == obj)
			return true;
		if (obj == null)
			return false;
		if (getClass() != obj.getClass())
			return false;
		Vuelos other = (Vuelos) obj;
		return Objects.equals(nombre, other.nombre) && Objects.equals(vuelos, other.vuelos);
	}
	
	// OPERACIONES:
	
	public Integer getNumPasajerosDestino(String destino) {
		Integer res = 0;
		for(Vuelo v : vuelos) {
			if (v.getDestino().equals(destino)) {
				res += v.getNumPasajeros();
			}
		}
		return res;
	}
	
	public void incorporaVuelo(Vuelo v) {
		vuelos.add(v);
	}
	
	public void incorporaVuelos(Collection<Vuelo> nuevosVuelos) {
		vuelos.addAll(nuevosVuelos);
	}
	
	public void eliminaVuelo(Vuelo v) {
		vuelos.remove(v);
	}
	
	public void ordena() {
		Collections.sort(vuelos);
	}
	
	public Boolean existeVueloDestino(String destino) {
		Boolean res = false;
		for (Vuelo v : vuelos) {
			if (v.getDestino().equals(destino)) {
				res = true;
				break;
			} 
		}
		return res;
	}
	
}
