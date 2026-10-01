package fp.tipos;

import java.time.LocalDate;
import java.util.ArrayList;
import java.util.List;
import java.util.Objects;

import fp.utiles.Checkers;

public class Jugador implements Comparable<Jugador> {
	private String nombre;
	private LocalDate fechaNacimiento;
	private TipoPosicion tipoPosicion;
	private Integer goles;
	private Integer asistencias;
	private Equipo equipo;
	private List<String> lesiones;
	
	public Jugador(String nombre, LocalDate fechaNacimiento, TipoPosicion tipoPosicion,
			Integer goles, Integer asistencias, Equipo equipo, List<String> lesiones) {
		Checkers.check("La fecha de nacimiento no puede ser anterior al 1970-01-01."
				, fechaNacimiento.isAfter(LocalDate.of(1970, 01, 01)));
		Checkers.check("Los goles y asistencias deben ser números mayores o iguales a 0.", goles >= 0 && asistencias >= 0);
		this.nombre = nombre;
		this.fechaNacimiento = fechaNacimiento;
		this.tipoPosicion = tipoPosicion;
		this.goles = goles;
		this.asistencias = asistencias;
		this.equipo = equipo;
		this.lesiones = new ArrayList<>(lesiones);
	}

	public String getNombre() {
		return nombre;
	}

	public LocalDate getFechaNacimiento() {
		return fechaNacimiento;
	}

	public TipoPosicion getTipoPosicion() {
		return tipoPosicion;
	}

	public Integer getGoles() {
		return goles;
	}

	public Integer getAsistencias() {
		return asistencias;
	}

	public Equipo getEquipo() {
		return equipo;
	}

	public List<String> getLesiones() {
		return new ArrayList<>(lesiones);
	}
	
	public Boolean getCampeon() {
		Boolean res = false;
		if (equipo.clasificacion() == 1) {
			res = true;
		}
		return res;
	}
	
	public Boolean getMismaLesionConsecutiva() {
		Boolean res = false;
		if (lesiones.size() > 1) {
			for (int i = 0; i < lesiones.size() - 1; i++) {
				if (lesiones.get(i).equals(lesiones.get(i + 1))) {
					res = true;
				}
			}	
		}
		return res;
	}
	
	public Integer getEdad() {
		return LocalDate.now().getYear() - fechaNacimiento.getYear();
	}

	public String toString() {
		return "Jugador [nombre=" + nombre + ", fechaNacimiento=" + fechaNacimiento + ", tipoPosicion=" + tipoPosicion + ", goles=" + goles + ", asistencias=" + asistencias + ", equipo="
				+ equipo + ", lesiones=" + lesiones + "]";
	}

	public int hashCode() {
		return Objects.hash(fechaNacimiento, nombre);
	}

	public boolean equals(Object obj) {
		if (this == obj)
			return true;
		if (obj == null)
			return false;
		if (getClass() != obj.getClass())
			return false;
		Jugador other = (Jugador) obj;
		return Objects.equals(fechaNacimiento, other.fechaNacimiento) && Objects.equals(nombre, other.nombre);
	}

	public int compareTo(Jugador j) {
		Integer res = getFechaNacimiento().compareTo(j.getFechaNacimiento());
		if (res == 0) {
			res = getNombre().compareTo(j.getNombre());
		}
		return 0;
	}
	
}
