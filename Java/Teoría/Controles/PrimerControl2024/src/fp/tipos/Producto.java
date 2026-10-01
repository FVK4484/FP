package fp.tipos;

public record Producto(String nombre, Double precio, Integer cantidadDisponible) {
	public Boolean getNoDisponible() {
		Boolean res = false;
		if (cantidadDisponible == 0) {
			res = true;
		}
		return res;
	}
}
