package fp.curso;


import java.time.LocalDate;
import java.time.temporal.ChronoUnit;
import java.util.Objects;

import fp.utiles.Checkers;

public class CursoOnline implements Comparable<CursoOnline>{
	
	private String identificador;
	private String titulo;
	private String organizacion;
	private LocalDate fechaInicio;
	private LocalDate fechaFin;
	private Integer duracion;
	private TipoCertificacion tipoCertificacion;
	private Double valoracionPromedio;
	private NivelDificultad nivelDificultad;
	private Integer numeroEstudiantes;
	private Boolean gratuito;
	
	public CursoOnline(String identificador, String titulo, String organizacion, LocalDate fechaInicio, LocalDate fechaFin,
			Integer duracion, TipoCertificacion tipoCertificacion, Double valoracionPromedio,
			NivelDificultad nivelDificultad, Integer numeroEstudiantes, Boolean gratuito) {
		
		Checkers.check("El identificador no puede estar vacío", !identificador.isEmpty());
//		checkIdentificador(identificador);
		Checkers.check("El identificador debe tener 8 caracteres: 3 letras seguidas de 5 números.", esIdValido(identificador));
		Checkers.check("La fecha de inicio "
				+ "debe ser anterior a la fecha de fin", fechaInicio.isBefore(fechaFin));
		Checkers.check("La duracion debe ser mayor que 0", duracion > 0);
		
		this.identificador = identificador;
		this.titulo = titulo;
		this.organizacion = organizacion;
		this.fechaInicio = fechaInicio;
		this.fechaFin = fechaFin;
		this.duracion = duracion;
		this.tipoCertificacion = tipoCertificacion;
		this.valoracionPromedio = valoracionPromedio;
		this.nivelDificultad = nivelDificultad;
		this.numeroEstudiantes = numeroEstudiantes;
		this.gratuito = gratuito;
	}
	
//	private void checkIdentificador(String identificador) {
//	    if (identificador.length() != 8 || !identificador.matches("^[a-zA-Z]{3}[0-9]{5}$")) {
//	        throw new IllegalArgumentException(
//	            "El identificador debe tener 8 caracteres: 3 letras seguidas de 5 números."
//	        );
//	    }
//	}
	
	private Boolean esIdValido(String identificador) {
		// ¿Para todos los elementos se cumple una condicion?
		Boolean res = true;
		// ¿Tiene 8 caracteres?
		res = identificador.length() == 8;
 		// 3 letras
		if(res == true) {
			for (int i = 0; i < 3; i++) {
				Character c = identificador.charAt(i);
				if (!Character.isLetter(c)) {
					res = false;
					break;
				}
			}	
		}
		// 5 dígitos
		if(res == true) {
			for (int i = 3; i < identificador.length(); i++) {
				Character c = identificador.charAt(i);
				if(!Character.isDigit(c)) {
					res = false;
					break;
				}
			}
		}
		return res;
	}

	public LocalDate getFechaInicio() {
		return fechaInicio;
	}

	public void setFechaInicio(LocalDate fechaInicio) {
		Checkers.check("La fecha de inicio "
				+ "debe ser anterior a la fecha de fin", fechaInicio.isBefore(fechaFin));
		this.fechaInicio = fechaInicio;
	}

	public LocalDate getFechaFin() {
		return fechaFin;
	}

	public void setFechaFin(LocalDate fechaFin) {
		this.fechaFin = fechaFin;
	}

	public Integer getDuracion() {
		return duracion;
	}

	public void setDuracion(Integer duracion) {
		Checkers.check("La duracion debe ser mayor que 0", duracion > 0);
		this.duracion = duracion;
	}

	public Boolean getGratuito() {
		return gratuito;
	}

	public void setGratuito(Boolean gratuito) {
		this.gratuito = gratuito;
	}

	public String getIdentificador() {
		return identificador;
	}

	public String getTitulo() {
		return titulo;
	}

	public String getOrganizacion() {
		return organizacion;
	}

	public TipoCertificacion getTipoCertificacion() {
		return tipoCertificacion;
	}

	public Double getValoracionPromedio() {
		return valoracionPromedio;
	}

	public NivelDificultad getNivelDificultad() {
		return nivelDificultad;
	}

	public Integer getNumeroEstudiantes() {
		return numeroEstudiantes;
	}
	
	// Propiedades derivadas
	public Double getMediaHorasSemanales() {
		Long semana= 
				ChronoUnit.WEEKS
				.between(fechaInicio, fechaFin);
		return duracion*1./semana;
	}
			
	public EstadoCurso getEstado() {
		LocalDate hoy = LocalDate.now();
		EstadoCurso res= null;
		if (fechaFin.isBefore(hoy)) {
			res= EstadoCurso.FINALIZADO;
		} else if (fechaInicio.isAfter(hoy)) {
			res=EstadoCurso.PROXIMO;
		} else {
			res=EstadoCurso.EN_CURSO;
		}
		return res;
	}
	
	public String toString() {
		return titulo + " (" + identificador + ")";
	}
	
	public int hashCode() {
		return Objects.hash(fechaInicio, fechaFin, identificador, numeroEstudiantes, titulo);
	}

	public boolean equals(Object obj) {
		if (this == obj)
			return true;
		if (obj == null)
			return false;
		if (getClass() != obj.getClass())
			return false;
		CursoOnline other = (CursoOnline) obj;
		return Objects.equals(fechaInicio, other.fechaInicio) && Objects.equals(fechaFin, other.fechaFin) && Objects.equals(identificador, other.identificador)
				&& Objects.equals(numeroEstudiantes, other.numeroEstudiantes) && Objects.equals(titulo, other.titulo);
	}

	public int compareTo(CursoOnline c) {
		Integer res = getFechaInicio().compareTo(c.getFechaInicio());
		if (res == 0) {
			res = getFechaFin().compareTo(c.getFechaFin());
			if (res == 0) {
				res = getDuracion().compareTo(c.getDuracion());
			}
		}
		return res;
	}
	
}
