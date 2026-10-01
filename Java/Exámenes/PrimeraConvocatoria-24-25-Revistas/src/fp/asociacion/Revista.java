package fp.asociacion;

import java.time.DayOfWeek;
import java.time.LocalDate;
import java.util.ArrayList;
import java.util.List;
import java.util.Objects;

import fp.utiles.Checkers;


public class Revista implements Comparable<Revista> {
	
	String numero;
	LocalDate fechaPublicacion;
	Integer ejemplares;
	Integer paginasFijas;
	Integer anuncios;
	List<Articulo> articulos;
	
	public Revista(String numero, LocalDate fechaPublicacion, Integer ejemplares, Integer paginasFijas,
			Integer anuncios, List<Articulo> articulos) {
		
		Checkers.check("Debe haber al menos un artículo en la revista."
				, articulos.size() > 0);
		Checkers.check("La fecha de publicación de la revista debe ser un lunes."
				, fechaPublicacion.getDayOfWeek().equals(DayOfWeek.MONDAY));
		
		this.numero = numero;
		setFechaPublicacion(fechaPublicacion);
		setEjemplares(ejemplares);
		this.paginasFijas = paginasFijas;
		this.anuncios = anuncios;
		this.articulos = new ArrayList<>(articulos);
		
		Checkers.check("El número total de páginas de la revista debe ser múltiplo de 8."
				, (getNumeroTotalPaginas() % 8) == 0);
		
	}

	public LocalDate getFechaPublicacion() {
		return fechaPublicacion;
	}

	public void setFechaPublicacion(LocalDate fechaPublicacion) {
		this.fechaPublicacion = fechaPublicacion;
	}

	public Integer getEjemplares() {
		return ejemplares;
	}

	public void setEjemplares(Integer ejemplares) {
		this.ejemplares = ejemplares;
	}

	public String getNumero() {
		return numero;
	}

	public Integer getPaginasFijas() {
		return paginasFijas;
	}

	public Integer getAnuncios() {
		return anuncios;
	}

	public List<Articulo> getArticulos() {
		return new ArrayList<>(articulos);
	}
	
	public Integer getNumeroTotalPaginas() {
		Integer res = paginasFijas;
		for (Articulo a : articulos) {
			res += a.paginas();
		}
		return res;
	}
	
	public Boolean getRevistaTematica() {
		Boolean res = false;
		for (Articulo a : articulos) {
			if (a.articuloLargo()) {
				res = true;
				break;
			}
		}
		return res;
	}
	
	public Extension getExtension() {
		Extension res = Extension.ALTA;
		if (getNumeroTotalPaginas() < 32) {
			res = Extension.BAJA;
		} else if (32 <= getNumeroTotalPaginas() && getNumeroTotalPaginas() <= 64) {
			res = Extension.MEDIA;
		}	
		return res;	
	}

	public String toString() {
		return "Revista [numero=" + numero + ", fechaPublicacion=" + fechaPublicacion + ", ejemplares=" + ejemplares
				+ ", paginasFijas=" + paginasFijas + ", anuncios=" + anuncios + ", articulos=" + articulos + "]";
	}

	public int hashCode() {
		return Objects.hash(numero);
	}

	public boolean equals(Object obj) {
		if (this == obj)
			return true;
		if (obj == null)
			return false;
		if (getClass() != obj.getClass())
			return false;
		Revista other = (Revista) obj;
		return Objects.equals(numero, other.numero);
	}

	public int compareTo(Revista r) {
		return numero.compareTo(r.getNumero());
	}

}
