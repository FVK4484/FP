package fp.tipos;

import java.time.DayOfWeek;
import java.time.Duration;
import java.time.LocalTime;
import java.util.Objects;

public record Tutoria(DayOfWeek diaSemana, LocalTime horaComienzo, 
		LocalTime horaFin) implements Comparable<Tutoria>{
	
	public Tutoria {
		checkDiaSemana(diaSemana);
		checkDuracion(horaComienzo, horaFin);
	}
	
	public Tutoria(DayOfWeek diaSemana, LocalTime horaInicio, Integer duracionMinutos) {
		this(diaSemana, horaInicio, horaInicio.plusMinutes(duracionMinutos));
	}
	
	public Integer getDuracion() {
		Long duracion = Duration.between(horaComienzo, horaFin).toMinutes();
		return duracion.intValue();
	}
	
	private String getInicialDia(DayOfWeek dia) {
		String res = "";
		if(dia == DayOfWeek.MONDAY) {
			res = "L";
		} else if(dia == DayOfWeek.TUESDAY) {
			res = "M";
		} else if(dia == DayOfWeek.WEDNESDAY) {
			res = "X";
		} else if(dia == DayOfWeek.THURSDAY) {
			res = "J";
		} else if(dia == DayOfWeek.FRIDAY) {
			res = "V";
		}
		return res;
	}
	
	private void checkDiaSemana(DayOfWeek diaSemana) {
		if (diaSemana.equals(DayOfWeek.SATURDAY) || 
				diaSemana.equals(DayOfWeek.SUNDAY)) {
			throw new IllegalArgumentException
			("Sólo puede darse de lunes a viernes.");
		}
	}
	
	private void checkDuracion(LocalTime horaComienzo, LocalTime horaFin) {
		Long duracion = Duration.between(horaComienzo, horaFin).toMinutes();
		if (duracion.intValue() < 15) {
			throw new IllegalArgumentException
			("Duración de al menos 15 minutos.");
		}
	}

	public String toString() {
		return getInicialDia(diaSemana) + " " + horaComienzo + "-" + horaFin;
	}

	public int hashCode() {
		return Objects.hash(diaSemana, horaComienzo);
	}

	public boolean equals(Object obj) {
		if (this == obj)
			return true;
		if (obj == null)
			return false;
		if (getClass() != obj.getClass())
			return false;
		Tutoria other = (Tutoria) obj;
		return diaSemana == other.diaSemana 
				&& Objects.equals(horaComienzo, other.horaComienzo);
	}

	public int compareTo(Tutoria t) {
		Integer res = diaSemana.compareTo(t.diaSemana);
		if (res == 0) {
			res = horaComienzo.compareTo(t.horaComienzo);
		}
		return res;
	}
	
}
