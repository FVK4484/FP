package fp.tipos;

import java.util.Objects;

public class Espacio implements Comparable <Espacio>{
	private TipoEspacio tipoEspacio;
	private String nombre;
	private Integer capacidad;
	private Integer planta;
	
	public Espacio(TipoEspacio tipoEspacio, String nombre, Integer capacidad, Integer planta) {
		checkCapacidad(capacidad);
		this.tipoEspacio = tipoEspacio;
		this.nombre = nombre;
		this.capacidad = capacidad;
		this.planta = planta;
	}
	public TipoEspacio getTipoEspacio() {
		return tipoEspacio;
	}
	public void setTipoEspacio(TipoEspacio tipoEspacio) {
		this.tipoEspacio = tipoEspacio;
	}
	public String getNombre() {
		return nombre;
	}
	public void setNombre(String nombre) {
		this.nombre = nombre;
	}
	public Integer getCapacidad() {
		return capacidad;
	}
	public void setCapacidad(Integer capacidad) {
		checkCapacidad(capacidad);
		this.capacidad = capacidad;
	}
	public Integer getPlanta() {
		return planta;
	}
	public String toString() {
		return nombre + " (planta "+ planta + ")";
	}	
	
	private void checkCapacidad(Integer capacidad) {
		if (capacidad <= 0) {
			throw new IllegalArgumentException
			("La capacidad debe ser mayor que 0.");
		}
	}

	public int hashCode() {
		return Objects.hash(nombre, planta);
	}

	public boolean equals(Object obj) {
		if (this == obj)
			return true;
		if (obj == null)
			return false;
		if (getClass() != obj.getClass())
			return false;
		Espacio other = (Espacio) obj;
		return Objects.equals(nombre, other.nombre) 
				&& Objects.equals(planta, other.planta);
	}

	public int compareTo(Espacio e) {
		Integer res = getPlanta().compareTo(e.getPlanta());
		if (res == 0) {
			res = getNombre().compareTo(e.getNombre());
		}
		return res;
	}
	
}
