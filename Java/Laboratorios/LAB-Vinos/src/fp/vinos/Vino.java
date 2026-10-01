package fp.vinos;

import fp.utiles.Checkers;

public record Vino(String pais, String region, Integer puntos,
		Double precio, String uva) {
	public Vino {
		Checkers.check("Los puntos deben estar entre cero y cien.", 
				puntos >= 0 && puntos <= 100);
		Checkers.check("El precio debe ser mayor que cero.", 
				precio > 0.);
	}
	
	public Double calidadPrecio() {
		return puntos / precio;
	}
}
