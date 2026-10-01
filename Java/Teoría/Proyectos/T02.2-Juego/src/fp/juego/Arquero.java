package fp.juego;

public class Arquero extends Personaje{
	private Integer precision;

	public Arquero(String nombre, Integer nivel, Integer numeroVidas, Integer precision) {
		super(nombre, nivel, numeroVidas);
		this.precision = precision;
	}

	public Integer getPrecision() {
		return precision;
	}
	
	public String atacar() {
		return getNombre() + " dispara una flecha con precisión de " + precision + "!";
	}
	
	public String toString() {
		return "Arquero: " + super.toString() + ", precisión=" + precision;	
		}
	
	public boolean equals(Object obj) {
		boolean result = false;
		if (obj instanceof Arquero) {
			Arquero g = (Arquero) obj;
			result = super.equals(g) && precision.equals(g.precision);
		}
		return result;
	}
	
	public int hashCode() {
		return 31 * (super.hashCode() + precision.hashCode());
	}
}
