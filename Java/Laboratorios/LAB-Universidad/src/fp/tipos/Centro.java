package fp.tipos;

import java.util.HashSet;
import java.util.Objects;
import java.util.Set;

public class Centro implements Comparable<Centro>{
	private String nombre;
	private String direccion;
	private Integer numeroPlantas;
	private Integer numeroSotanos;
	private Set<Espacio> espacios;
	
	public Centro(String nombre, String direccion, Integer numeroPlantas, Integer numeroSotanos,
			Set<Espacio> espacios) {
		checkPlanta(numeroPlantas);
		checkSotano(numeroSotanos);
		this.nombre = nombre;
		this.direccion = direccion;
		this.numeroPlantas = numeroPlantas;
		this.numeroSotanos = numeroSotanos;
		this.espacios = new HashSet<>();
	}
	
	private void checkPlanta(Integer numeroPlantas) {
		if (numeroPlantas <= 0) {
			throw new IllegalArgumentException("Debe tener al menos una planta.");
		}
	}
	
	private void checkSotano(Integer numeroSotanos) {
		if (numeroSotanos < 0) {
			throw new IllegalArgumentException("No puede ser negativo.");
		}
	}

	public String getNombre() {
		return nombre;
	}

	public String getDireccion() {
		return direccion;
	}

	public Integer getNumeroPlantas() {
		return numeroPlantas;
	}

	public Integer getNumeroSotanos() {
		return numeroSotanos;
	}

	public Set<Espacio> getEspacios() {
		return new HashSet<>(espacios);
	}
	
	public void nuevoEspacio(Espacio e) {
		if (e.getPlanta() <= numeroPlantas) {
			espacios.add(e);
		}	
	}
	
	public void eliminaEspacio(Espacio e) {
		if (espacios.contains(e)) {
			espacios.remove(e);
		}
	}

	public int hashCode() {
		return Objects.hash(nombre);
	}

	public boolean equals(Object obj) {
		if (this == obj)
			return true;
		if (obj == null)
			return false;
		if (getClass() != obj.getClass())
			return false;
		Centro other = (Centro) obj;
		return Objects.equals(nombre, other.nombre);
	}

	public int compareTo(Centro c) {
		Integer res = nombre.compareTo(c.getNombre());
		return res;
	}
	
	// TODO:
	
	//	getConteosEspacios, devuelve un array de 5 elementos de tipo 
	//	Integer que representan el número de espacios de tipo aula de 
	//	teoría, laboratorio, seminario, aula de examen u otro tipo, 
	//	respectivamente, que hay en el centro.
	
	
	
}
