package fp.tipos;
import java.time.Duration;
import java.time.LocalDate;
import java.util.ArrayList;
import java.util.List;
import java.util.Objects;

import fp.utiles.Checkers;

public class Vuelo implements Comparable<Vuelo>{
	
	private Trayecto trayecto;
	private Double precio;
	private Integer numPasajeros;
	private Integer numPlazas;
	private String codigo;
	private LocalDate fecha;
	private Duration duracion;
	private List<String> tripulacion;
	
	public Vuelo(Trayecto trayecto, Double precio, Integer numPasajeros, Integer numPlazas, String codigo,
			LocalDate fecha, Duration duracion, List<String> tripulacion) {

		setTrayecto(trayecto);
		setPrecio(precio);
		setNumPlazas(numPlazas);
		setNumPasajeros(numPasajeros);
		setCodigo(codigo);
		setFecha(fecha);
		setDuracion(duracion);
		this.tripulacion = new ArrayList<>(tripulacion);
		
		Checkers.check("El número de tripulantes del avión debe ser superior o igual a 3 (un piloto, un copiloto y al menos un auxiliar)."
				, tripulacion.size() >= 3 && minimoTripulacion(tripulacion));
		Checkers.check("Los códigos de los tripulantes del avión deben tener 6 caracteres, los dos primeros deben ser alfabéticos (en mayúsculas) y los cuatro últimos numéricos."
				, requisitosCodigo(tripulacion));
		Checkers.check("Una tripulación debe tener al menos un piloto, un copiloto y un asistente. Si hay más de tres tripulantes, desde el cuarto en adelante deben ser auxiliares."
				, minimoTripulacion(tripulacion) && hayAuxiliares(tripulacion));
		
	}

	public Trayecto getTrayecto() {
		return trayecto;
	}

	public void setTrayecto(Trayecto trayecto) {
		this.trayecto = trayecto;
	}

	public Double getPrecio() {
		return precio;
	}

	public void setPrecio(Double precio) {
		Checkers.check("El precio debe ser mayor o igual que cero."
				, precio >= 0);
		this.precio = precio;
	}

	public Integer getNumPasajeros() {
		return numPasajeros;
	}

	public void setNumPasajeros(Integer numPasajeros) {
		Checkers.check("El número de pasajeros debe ser mayor que cero."
				, numPasajeros >= 0);
		Checkers.check("El número de pasajeros debe ser inferior o igual que el número de plazas."
				, numPasajeros <= numPlazas);
		this.numPasajeros = numPasajeros;
	}

	public Integer getNumPlazas() {
		return numPlazas;
	}

	public void setNumPlazas(Integer numPlazas) {
		Checkers.check("El número de plazas debe ser mayor o igual que cero."
				, numPlazas >= 0);
		this.numPlazas = numPlazas;
	}

	public String getCodigo() {
		return codigo;
	}

	public void setCodigo(String codigo) {
		this.codigo = codigo;
	}

	public LocalDate getFecha() {
		return fecha;
	}

	public void setFecha(LocalDate fecha) {
		this.fecha = fecha;
	}

	public Duration getDuracion() {
		return duracion;
	}

	public void setDuracion(Duration duracion) {
		this.duracion = duracion;
	}

	public List<String> getTripulacion() {
		return new ArrayList<>(tripulacion);
	}
	
	public String getOrigen() {
		return trayecto.origen();
	}
	
	public String getDestino() {
		return trayecto.destino();
	}
	
	public Integer getDuracionMinutos() {
		return (int) duracion.toMinutes();
	}
	
	public Boolean getEstaCompleto() {
		Boolean res = false;
		if (numPlazas == numPasajeros) {
			res = true;
		}
		return res;
	}
	
	public Double getPorcentajeOcupacion() {
		return (double) numPasajeros * 100 / numPlazas;
	}
	
	private boolean minimoTripulacion(List<String> tripulacion) {
		
		Boolean res = false;
		Integer cont1 = 0;
		Integer cont2 = 0;
		Integer cont3 = 0;
		
		if (tripulacion.size() >= 3) {
			for (String tripulante : tripulacion) {		
				if (tripulante.startsWith("PP")) {
					cont1 ++;
				} else if (tripulante.startsWith("CP")) {
					cont2 ++;
				} else if (tripulante.startsWith("AV")){
					cont3 ++;
				}	
			}	
		}
		if (cont1 == 1 && cont2 == 1 && cont3 >= 1) {
			res = true;
		}
		return res;
		
	}
	
	private Boolean requisitosCodigo(List<String> tripulacion) {
		Boolean res = true;
		for (String t : tripulacion) {
			if (t.length() != 6) {
				res = false;
				break;
			} else if (!t.startsWith("AV") && !t.startsWith("PP") && !t.startsWith("CP")) {
				res = false;
				break;
			} else {
				String numeros = t.substring(2);
				for (int i = 0; i < numeros.length(); i++) {
					if (!Character.isDigit(numeros.charAt(i))) {
						res = false;
						break;
					}
				}
				if (!res) break; 
			}
		}
		return res;
	}
	
	private Boolean hayAuxiliares(List<String> tripulacion) {
		Boolean res = false;
		Integer cont1 = 0;
		Integer cont2 = 0;
		Integer cont3 = 0;
		
		if (tripulacion.size() >= 3) {
			for (String tripulante : tripulacion) {		
				if (tripulante.startsWith("PP")) {
					cont1 ++;
				} else if (tripulante.startsWith("CP")) {
					cont2 ++;
				} else if (tripulante.startsWith("AV")){
					cont3 ++;
				}	
			}	
		}
		if (cont1 > 1 || cont2 > 1) {
			res = false;
		} else if (cont1 == 1 && cont2 == 1 && cont3 >= 1) {
			res = true;
		} else {
			res = false;
		}
		return res;
	}

	public String toString() {
		return "Vuelo [Trayecto=" + trayecto + ", codigo=" + codigo + ", fecha=" + fecha + "]";
	}

	public int hashCode() {
		return Objects.hash(codigo, fecha);
	}

	public boolean equals(Object obj) {
		if (this == obj)
			return true;
		if (obj == null)
			return false;
		if (getClass() != obj.getClass())
			return false;
		Vuelo other = (Vuelo) obj;
		return Objects.equals(codigo, other.codigo) && Objects.equals(fecha, other.fecha);
	}

	public int compareTo(Vuelo v) {
		Integer res = getFecha().compareTo(v.getFecha());
		if (res == 0) {
			res = getCodigo().compareTo(v.getCodigo());
		}
		return res;
	}
	
	public void incrementaPrecioPorcentaje(Double porcentaje) {
	    Double incremento = (this.precio * porcentaje) / 100;
	    this.precio += incremento;
	}

}
