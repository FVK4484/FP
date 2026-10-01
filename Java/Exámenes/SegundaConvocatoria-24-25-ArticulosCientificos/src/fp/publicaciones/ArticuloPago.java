package fp.publicaciones;

import java.time.LocalDate;
import java.util.List;

import fp.utiles.Checkers;

public class ArticuloPago extends Articulo{
	
	Double precio;

	public ArticuloPago(String titulo, List<Autor> autores
			, LocalDate fechaPublicacion, String revista, Double precio) {
		super(titulo, autores, fechaPublicacion, revista, TipoPublicacion.PAGO);
		setPrecio(precio);
	}

	public Double getPrecio() {
		return precio;
	}

	public void setPrecio(Double precio) {
		Checkers.check("El precio del artículo tiene que ser mayor o igual que cero.", precio >= 0);
		this.precio = precio;
	}
	
//	public String toString() {
//		return super.toString() + ", precio=" + precio + "]";
//	}
	
	public String toString() {
		return "Articulo [titulo=" + titulo + ", autores=" + autores + ", fechaPublicacion=" + fechaPublicacion
				+ ", revista=" + revista + ", tipoPublicacion=" + tipoPublicacion + ", numeroCitas=" + numeroCitas
				+ ", keywords=" + keywords + ", precio=" + precio + "]";
	}
	
}
