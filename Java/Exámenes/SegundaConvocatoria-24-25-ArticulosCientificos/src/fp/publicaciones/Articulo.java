package fp.publicaciones;

import java.time.LocalDate;
import java.util.ArrayList;
import java.util.List;
import java.util.Objects;
import java.util.SortedSet;
import java.util.TreeSet;

import fp.utiles.Checkers;

public class Articulo implements Comparable<Articulo>{
	String titulo;
	List<Autor> autores;
	LocalDate fechaPublicacion;
	String revista;
	TipoPublicacion tipoPublicacion;
	Integer numeroCitas;
	SortedSet<String> keywords;
	
	public Articulo(String titulo, List<Autor> autores, LocalDate fechaPublicacion, String revista,
			TipoPublicacion tipoPublicacion) {
		
		this.titulo = titulo;
		this.autores = new ArrayList<>(autores);
		setFechaPublicacion(fechaPublicacion);
		this.revista = revista;
		this.tipoPublicacion = tipoPublicacion;
		this.numeroCitas = 0;
		this.keywords = new TreeSet<>();
		
		Checkers.check("El artículo debe tener obligatoriamente solo un autor de correspondencia."
				, soloAutorCorrespondencia(autores));
		
	}

	public LocalDate getFechaPublicacion() {
		return fechaPublicacion;
	}

	public void setFechaPublicacion(LocalDate fechaPublicacion) {
		Checkers.check("La fecha de publicación debe ser anterior o igual a la fecha actual."
				, fechaPublicacion.isBefore(LocalDate.now()) || fechaPublicacion.isEqual(LocalDate.now()));
		this.fechaPublicacion = fechaPublicacion;
	}

	public Integer getNumeroCitas() {
		return numeroCitas;
	}

	public void setNumeroCitas(Integer numeroCitas) {
		Checkers.check("El número de citas debe ser mayor o igual que cero."
				, numeroCitas >= 0);
		this.numeroCitas = numeroCitas;
	}

	public String getTitulo() {
		return titulo;
	}

	public List<Autor> getAutores() {
		return new ArrayList<>(autores);
	}

	public String getRevista() {
		return revista;
	}

	public TipoPublicacion getTipoPublicacion() {
		return tipoPublicacion;
	}

	public SortedSet<String> getKeywords() {
		return new TreeSet<>(keywords);
	}
	
	public void agregaKeyword(String keyword) { 
		keywords.add(keyword.toLowerCase()); 
	}
	
	public String getPrimerAutor() {
		return autores.getFirst().nombre();
	}
	
	public Autor getAutorCorrespondencia() {
		Autor res = null;
		for (Autor a : autores) {
			if (a.correspondencia()) {
				res = a;
				break;
			}
		}
		return res;
	}
	
	public Integer getNumeroAutores() {
		return autores.size();
	}
	
	public Boolean soloAutorCorrespondencia(List<Autor> autores) {
		Integer cont = 0;
		for (Autor a : autores) {
			if (a.correspondencia()) {
				cont += 1;
			}
		}
		return cont.equals(1);	
	}

	public String toString() {
		return "Articulo [titulo=" + titulo + ", autores=" + autores + ", fechaPublicacion=" + fechaPublicacion
				+ ", revista=" + revista + ", tipoPublicacion=" + tipoPublicacion + ", numeroCitas=" + numeroCitas
				+ ", keywords=" + keywords + "]";
	}

	public int hashCode() {
		return Objects.hash(fechaPublicacion, revista, titulo);
	}

	public boolean equals(Object obj) {
		if (this == obj)
			return true;
		if (obj == null)
			return false;
		if (getClass() != obj.getClass())
			return false;
		Articulo other = (Articulo) obj;
		return Objects.equals(fechaPublicacion, other.fechaPublicacion) && Objects.equals(revista, other.revista)
				&& Objects.equals(titulo, other.titulo);
	}

	public int compareTo(Articulo a) {
		Integer res = getFechaPublicacion().compareTo(a.getFechaPublicacion());
		if (res == 0) {
			res = getTitulo().compareTo(a.getTitulo());
			if (res == 0) {
				res = getRevista().compareTo(a.getRevista());
			}
		}
		return res;			
	}	
	
}
