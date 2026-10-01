package fp.juego;

public class Mago extends Personaje{
	private Integer mana;

	public Mago(String nombre, Integer nivel, Integer numeroVidas, Integer mana) {
		super(nombre, nivel, numeroVidas);
		this.mana = mana;
	}

	public Integer getMana() {
		return mana;
	}
	
	public String atacar() {
		return getNombre() + " lanza un hechizo usando 120 de maná " + mana + "!";
	}
	
	public String toString() {
		return "Mago: " + super.toString() + ", maná=" + mana;	
		}
	
	public boolean equals(Object obj) {
		boolean result = false;
		if (obj instanceof Mago) {
			Mago g = (Mago) obj;
			result = super.equals(g) && mana.equals(g.mana);
		}
		return result;
	}
	
	public int hashCode() {
		return 31 * (super.hashCode() + mana.hashCode());
	}
}
