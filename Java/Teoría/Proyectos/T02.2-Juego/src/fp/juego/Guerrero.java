package fp.juego;

import java.util.Objects;

public class Guerrero extends Personaje{
	private Integer fuerza;
	
	public Guerrero(String nombre, Integer nivel, Integer numeroVidas, Integer fuerza) {
		super(nombre, nivel, numeroVidas);
		this.fuerza = fuerza;
	}

	public Integer getFuerza() {
		return fuerza;
	}
	
	public String atacar() {
		return getNombre() + " ataca con su espada con fuerza " + fuerza + "!";
	}
	
	public String toString() {
		return "Guerrero: " + super.toString() + ", fuerza=" + fuerza;	
		}

	public boolean equals(Object obj) {
		boolean result = false;
		if (obj instanceof Guerrero) {
			Guerrero g = (Guerrero) obj;
			result = super.equals(g) && fuerza.equals(g.fuerza);
		}
		return result;
	}
	
	public int hashCode() {
		return 31 * (super.hashCode() + fuerza.hashCode());
	}
}
