package fp.examenes;

import java.time.LocalDateTime;
import java.time.Duration;
import java.util.*;
import java.util.stream.Collectors;

import fp.utiles.Checkers;

public class Examen implements Comparable<Examen> {
	private String asignatura;
	private Integer curso;
	private LocalDateTime fechaHora;
	private Duration duracion;
	private TipoExamen tipoExamen;
	private Integer asistentes;
	private Boolean inscripcion;
	private List<Aula> aulas;
	
	public Examen(String asignatura, Integer curso, LocalDateTime fechaHora, Duration duracion, TipoExamen tipoExamen,
			Integer asistentes, Boolean inscripcion, List<Aula> aulas) {
		this.asignatura = asignatura;
		this.curso = curso;
		this.fechaHora = fechaHora;
		setDuracion(duracion);
		this.tipoExamen = tipoExamen;
		setAsistentes(asistentes);
		this.inscripcion = inscripcion;
		this.aulas = new ArrayList<>(aulas);
	}
	
	public Duration getDuracion() {
		return duracion;
	}
	public void setDuracion(Duration duracion) {
		Checkers.check("La duración debe ser como mínimo de una hora."
				, duracion.toHours() >= 1);
		this.duracion = duracion;
	}
	public Integer getAsistentes() {
		return asistentes;
	}
	public void setAsistentes(Integer asistentes) {
		Checkers.check("El número de asistentes debe ser mayor que 0."
				, asistentes > 0);
		this.asistentes = asistentes;
	}
	public String getAsignatura() {
		return asignatura;
	}
	public Integer getCurso() {
		return curso;
	}
	public LocalDateTime getFechaHora() {
		return fechaHora;
	}
	public TipoExamen getTipoExamen() {
		return tipoExamen;
	}
	public Boolean getInscripcion() {
		return inscripcion;
	}
	public List<Aula> getAulas() {
		return new ArrayList<>(aulas);
	}
	
	public List<Integer> getPuestos() {
		List<Integer> puestos = new ArrayList<>();
		for (Aula aula : aulas) {
			puestos.add(aula.capacidad());
		}
		return puestos;
	}
	
	public Integer getCapacidadMaxima() {
		Integer capacidades = 0;
		for (Aula aula : aulas) {
			capacidades += aula.capacidad();
		}
		return capacidades;
	}
	
	public Double getPorcentajeAsistentes() {
		return (asistentes * 100.0) / getCapacidadMaxima();
	}

	public String toString() {
		return "Examen [asignatura=" + asignatura + ", curso=" + curso + ", fechaHora=" + fechaHora + ", duracion="
				+ duracion + ", tipoExamen=" + tipoExamen + ", asistentes=" + asistentes + ", inscripcion="
				+ inscripcion + ", aulas=" + aulas + "]";
	}

	public int hashCode() {
		return Objects.hash(asignatura, curso, fechaHora);
	}

	public boolean equals(Object obj) {
		if (this == obj)
			return true;
		if (obj == null)
			return false;
		if (getClass() != obj.getClass())
			return false;
		Examen other = (Examen) obj;
		return Objects.equals(asignatura, other.asignatura) && Objects.equals(curso, other.curso)
				&& Objects.equals(fechaHora, other.fechaHora);
	}

	public int compareTo(Examen e) {
		Integer res = getFechaHora().compareTo(e.getFechaHora());
		if (res == 0) {
			res = getCurso().compareTo(e.getCurso());
			if (res == 0) {
				res = getAsignatura().compareTo(e.getAsignatura());
			}
		}
		return res;
	}
	
	public Boolean usaAula(String nombreAula) {
		Boolean res = false;
		for (Aula aula : aulas) {
			if (nombreAula.equals(aula.nombre())) {
				res = true;
				break;
			}
		}
		return res;
	}	
}