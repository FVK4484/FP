package fp.tipos;
import java.time.LocalDate;
import java.util.List;
import java.util.Objects;
import java.time.Period;

import fp.utiles.Checkers;

import java.util.ArrayList;

public class Encuesta implements Comparable<Encuesta>{
	private String nombre;
	private LocalDate fechaComienzo;
	private LocalDate fechaFin;
	private Integer numeroEncuestados;
	private String pais;
	private TipoEncuesta tipoEncuesta;
	private Double porcentajeIndecisos;
	private List<Resultado> resultados;
	
	public Encuesta(String nombre, LocalDate fechaComienzo, LocalDate fechaFin, Integer numeroEncuestados, String pais,
			TipoEncuesta tipoEncuesta, Double porcentajeIndecisos, List<Resultado> resultados) {
		Checkers.check("La fecha de fin no puede ser anterior a la fecha de comienzo."
				, fechaComienzo.isBefore(fechaFin));
		Checkers.check("La lista de resultados no puede estar vacía."
				, !resultados.isEmpty());
		this.nombre = nombre;
		this.fechaComienzo = fechaComienzo;
		this.fechaFin = fechaFin;
		setNumeroEncuestados(numeroEncuestados);
		this.pais = pais;
		this.tipoEncuesta = tipoEncuesta;
		this.porcentajeIndecisos = porcentajeIndecisos;
		this.resultados = new ArrayList<>(resultados);
	}

	public Integer getNumeroEncuestados() {
		return numeroEncuestados;
	}

	public void setNumeroEncuestados(Integer numeroEncuestados) {
		Checkers.check("El número de encuestados debe ser mayor o igual que cero."
				, numeroEncuestados >= 0);
		this.numeroEncuestados = numeroEncuestados;
	}

	public Double getPorcentajeIndecisos() {
		return porcentajeIndecisos;
	}

	public void setPorcentajeIndecisos(Double porcentajeIndecisos) {
		this.porcentajeIndecisos = porcentajeIndecisos;
	}

	public String getNombre() {
		return nombre;
	}

	public LocalDate getFechaComienzo() {
		return fechaComienzo;
	}

	public LocalDate getFechaFin() {
		return fechaFin;
	}

	public String getPais() {
		return pais;
	}

	public TipoEncuesta getTipoEncuesta() {
		return tipoEncuesta;
	}

	public List<Resultado> getResultados() {
		return new ArrayList<>(resultados);
	}
	
	public Double getRatioEncuestadosDia() {
		return numeroEncuestados * 1.0 / (Period.between(fechaComienzo, fechaFin).getDays());
	}

	public String toString() {
		return "Encuesta [nombre=" + nombre + ", fechaComienzo=" + fechaComienzo + ", fechaFin=" + fechaFin
				+ ", numeroEncuestados=" + numeroEncuestados + ", pais=" + pais + ", tipoEncuesta=" + tipoEncuesta
				+ ", porcentajeIndecisos=" + porcentajeIndecisos + ", resultados=" + resultados + "]";
	}

	public int hashCode() {
		return Objects.hash(fechaComienzo, fechaFin, nombre, numeroEncuestados);
	}

	public boolean equals(Object obj) {
		if (this == obj)
			return true;
		if (obj == null)
			return false;
		if (getClass() != obj.getClass())
			return false;
		Encuesta other = (Encuesta) obj;
		return Objects.equals(fechaComienzo, other.fechaComienzo) && Objects.equals(fechaFin, other.fechaFin)
				&& Objects.equals(nombre, other.nombre) && Objects.equals(numeroEncuestados, other.numeroEncuestados);
	}

	public int compareTo(Encuesta e) {
		Integer res = getFechaComienzo().compareTo(e.getFechaComienzo());
		if (res == 0) {
			res = getFechaFin().compareTo(e.getFechaFin());
			if (res == 0) {
				res = getNombre().compareTo(e.getNombre());
				if (res == 0) {
					res = getNumeroEncuestados().compareTo(e.getNumeroEncuestados());
				}
			}
		}
		return res;
	}	
	
}
