package fp.tipos;

import fp.utiles.Checkers;

public class FactoriaProductos {
	public static Producto parseaProducto(String productoStr) {
		Checkers.checkNoNull(productoStr);
		String [] trozos = productoStr.split(";");
		String nombre = trozos[0].trim();
		Double precio = Double.valueOf(trozos[1].trim());
		Integer cantidadDisponible = Integer.valueOf(trozos[2].trim());
		return new Producto(nombre, precio, cantidadDisponible);
	}
}
