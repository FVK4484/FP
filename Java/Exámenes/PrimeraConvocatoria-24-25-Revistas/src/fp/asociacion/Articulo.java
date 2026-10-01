package fp.asociacion;

import fp.utiles.Checkers;

public record Articulo(String titulo, String categoria, Integer paginas) {
	
	
	public static final Integer MINIMO_PAGINAS = 10;
	
	public Articulo {
		Checkers.check("El título no puede estar vacío."
				, !titulo.isEmpty());
		Checkers.check("El número de páginas debe ser mayor que 0."
				, paginas > 0);
	}
	
	public Boolean articuloLargo() {
		Boolean res = false;
		if (paginas >= MINIMO_PAGINAS) {
			res = true;
		}
		return res;
	}
	
}
