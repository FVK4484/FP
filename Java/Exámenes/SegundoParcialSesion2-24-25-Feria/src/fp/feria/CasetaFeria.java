package fp.feria;

import java.util.HashSet;
import java.util.Objects;
import java.util.Set;

import fp.utiles.Checkers;

public class CasetaFeria implements Comparable<CasetaFeria>{
	
	private String nombre;
	private TipoCaseta tipoCaseta;
	private Integer modulo;
	private Integer aforo;
	private Set<Producto> menu;
	private String musica;
	private Boolean accesoAdaptado;
	private Double valoracion;
	
	public static final Double PRECIO_BARATO = 10.0;
	
	public CasetaFeria(String nombre, TipoCaseta tipoCaseta, Integer modulo, Integer aforo, Set<Producto> menu, String musica,
			Boolean accesoAdaptado, Double valoracion) {
		this.nombre = nombre;
		this.tipoCaseta = tipoCaseta;
		this.modulo = modulo;
		this.aforo = aforo;
		Checkers.check("Debe haber al menos un elemento dentro del menú"
				, menu.size() > 0);
		this.menu = new HashSet<>(menu);
		setMusica(musica);
		this.accesoAdaptado = accesoAdaptado;
		setValoracion(valoracion);
	}

	public String getMusica() {
		return musica;
	}

	public void setMusica(String musica) {
		this.musica = musica;
	}

	public Double getValoracion() {
		return valoracion;
	}

	public void setValoracion(Double valoracion) {
		Checkers.check("La valoración debe estar comprendida entre 0 y 100."
				, valoracion >= 0 && valoracion <= 100);
		this.valoracion = valoracion;
	}

	public String getNombre() {
		return nombre;
	}

	public TipoCaseta getTipoCaseta() {
		return tipoCaseta;
	}

	public Integer getModulo() {
		return modulo;
	}

	public Integer getAforo() {
		return aforo;
	}

	public Set<Producto> getMenu() {
		return new HashSet<>(menu);
	}

	public Boolean getAccesoAdaptado() {
		return accesoAdaptado;
	}
	
	public Double getPrecioMedio() {
		Double res = menu.stream()
				.mapToDouble(Producto::precio)
				.average()
				.getAsDouble();
		return res;
	}
	
	public Boolean getCasetaBarata() { 
		Boolean res = true; 
		for (Producto producto : getMenu()) { 
			if(!(producto.precio() < PRECIO_BARATO)) { 
				res = false; 
				break; 
			} 
		} 
		return res; 
	}

	public String toString() {
		return "CasetaFeria [nombre=" + nombre + ", tipoCaseta=" + tipoCaseta + ", modulo=" + modulo + ", aforo="
				+ aforo + ", menu=" + menu.size() + ", musica=" + musica + ", accesoAdaptado=" + accesoAdaptado
				+ ", valoracion=" + valoracion + "]";
	}

	public int hashCode() {
		return Objects.hash(modulo, nombre);
	}

	public boolean equals(Object obj) {
		if (this == obj)
			return true;
		if (obj == null)
			return false;
		if (getClass() != obj.getClass())
			return false;
		CasetaFeria other = (CasetaFeria) obj;
		return Objects.equals(modulo, other.modulo) 
				&& Objects.equals(nombre, other.nombre);
	}

	public int compareTo(CasetaFeria cf) {
		Integer res = getModulo().compareTo(cf.getModulo());
		if (res == 0) {
			res = getNombre().compareTo(cf.getNombre());
		}	
		return res;
	}
	
}
