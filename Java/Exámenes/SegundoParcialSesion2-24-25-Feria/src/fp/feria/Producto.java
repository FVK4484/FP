package fp.feria;

import fp.utiles.Checkers;

public record Producto(String nombre, Double precio) {
	
	public Producto {
		
		Checkers.checkNoNull(nombre, precio);
		Checkers.check("El precio no puede ser negativo.", precio > 0);
		
	}
	
}
