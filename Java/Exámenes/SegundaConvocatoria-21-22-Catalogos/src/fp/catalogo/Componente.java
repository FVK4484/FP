package fp.catalogo;

import java.util.HashSet;
import java.util.Objects;
import java.util.Set;

import fp.utiles.Checkers;


public class Componente implements Comparable<Componente> {
	
	private String nombre;
	private TipoComponente tipoComponente;
	private String suministrador;
	private Integer demora;
	private Double precio;
	private Double descuento;
	private Set<String> combinadores;
	
	public Componente(String nombre, TipoComponente tipoComponente, String suministrador, Integer demora, Double precio,
			Double descuento, Set<String> combinadores) {
		Checkers.check("La demora no debe superar los 45 días.", 
				demora <= 45);
		Checkers.check("Los combinadores no deben incluir al componente en cuestión (es decir, ningún componente se combina consigo mismo).", 
				!combinadores.contains(nombre));
		this.nombre = nombre;
		this.tipoComponente = tipoComponente;
		this.suministrador = suministrador;
		this.demora = demora;
		this.precio = precio;
		setDescuento(descuento);
		this.combinadores = new HashSet<>(combinadores);
	}
	
	public Double getPrecioDescontado() {
		return precio * descuento / 100;
	}

	public Double getPrecio() {
		return precio;
	}

	public void setPrecio(Double precio) {
		this.precio = precio;
	}

	public Double getDescuento() {
		return descuento;
	}

	public void setDescuento(Double descuento) {
		Checkers.check("El descuento es un porcentaje (comprendido entre 0.0 y 100.0).",
				descuento >= 0.0 && descuento <= 100.0);
		this.descuento = descuento;
	}

	public String getNombre() {
		return nombre;
	}

	public TipoComponente getTipoComponente() {
		return tipoComponente;
	}

	public String getSuministrador() {
		return suministrador;
	}

	public Integer getDemora() {
		return demora;
	}

	public Set<String> getCombinadores() {
		return new HashSet<>(combinadores);
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
		Componente other = (Componente) obj;
		return Objects.equals(nombre, other.nombre);
	}

	public int compareTo(Componente c) {
		Integer res = nombre.compareTo(c.getNombre());
		return res;
	}

	public String toString() {
		return "Componente [nombre=" + nombre + ", tipoComponente=" + tipoComponente + ", suministrador="
				+ suministrador + ", demora=" + demora + ", precio=" + precio + ", descuento=" + descuento
				+ ", combinadores=" + combinadores + "]";
	}
	
}
