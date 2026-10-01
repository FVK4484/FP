package fp.juego;

import java.util.Objects;

import fp.utiles.Checkers;

public class Personaje {
	private String nombre;
	private Integer nivel, numeroVidas;
	
	public Personaje(String nombre, Integer nivel, Integer numeroVidas) {
		Checkers.check("El número de vidas no puede ser negativo.", numeroVidas >= 0);
		this.nombre = nombre;
		this.nivel = nivel;
		this.numeroVidas = numeroVidas;
	}	

	public String getNombre() {
		return nombre;
	}


	public Integer getNivel() {
		return nivel;
	}


	public Integer getNumeroVidas() {
		return numeroVidas;
	}

	// Como modifican el estado del objeto, ponemos void.
	
	public void perderVida() {
		Checkers.check("El número de vidas no puede ser negativo.", numeroVidas > 0);
		numeroVidas --;
	}
	
	public void vidasExtra(Integer vidasExtra) {
		Checkers.check("El número de vidas no puede ser negativo.", vidasExtra >= 0);
		numeroVidas += vidasExtra;
	}
	
	public String atacar() {
		return "Este personaje no ataca.";
	}

	public String toString() {
		return "nombre=" + nombre + ", nivel=" + nivel + ", numeroVidas=" + numeroVidas + "";
	}

	public int hashCode() {
		return Objects.hash(nivel, nombre, numeroVidas);
	}

	public boolean equals(Object obj) {
		if (this == obj)
			return true;
		if (obj == null)
			return false;
		if (getClass() != obj.getClass())
			return false;
		Personaje other = (Personaje) obj;
		return Objects.equals(nivel, other.nivel) && Objects.equals(nombre, other.nombre)
				&& Objects.equals(numeroVidas, other.numeroVidas);
	}	
}
