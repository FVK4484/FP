package fp.tipos;

import java.time.DayOfWeek;
import java.time.LocalDate;
import java.time.LocalTime;
import java.util.Collection;
import java.util.HashMap;
import java.util.List;
import java.util.ArrayList;
import java.util.Map;
import java.util.SortedSet;
import java.util.TreeSet;

import fp.utiles.Checkers;

public class Profesor extends Persona{
	private Categoria categoria;
	private SortedSet<Tutoria> tutorias;
	private Map<Asignatura, Double> creditosPorAsignatura;
	
	public Profesor(Categoria categoria, String DNI, String nombre, String apellidos, LocalDate fechaNacimiento, String email) {
		super(DNI, nombre, apellidos, fechaNacimiento, email);
		Checkers.check("", fechaNacimiento.until(LocalDate.now()).getYears() >= 18);
		this.categoria = categoria;
		this.tutorias = new TreeSet<>();
		this.creditosPorAsignatura = new HashMap<Asignatura, Double>();
	}
	
	public Categoria getCategoría() {
		return categoria;
	}
	public void setCategoría(Categoria categoría) {
		this.categoria = categoría;
	}
	public SortedSet<Tutoria> getTutorias() {
		return new TreeSet<>(tutorias);
	}
	
	public void borraTutorias() {
		tutorias.clear();
	}
	
	public void borraTutoria(LocalTime inicio, DayOfWeek dia) {
		LocalTime fin = inicio.plusMinutes(30);
		Tutoria tutoria = new Tutoria(dia, inicio, fin);
		tutorias.remove(tutoria);
	}
	
	public void añadeTutoria(LocalTime inicio, DayOfWeek dia, Integer duracion) {
		LocalTime fin = inicio.plusMinutes(duracion);
		Tutoria tutoria = new Tutoria(dia, inicio, fin);
		tutorias.add(tutoria);
	}
	
	public boolean equals(Object o) {
		boolean res = false;
		if (o instanceof Profesor) {
			res = super.equals(o);
		}
		return res;
	}
	
	public int HashCode() {
		return super.hashCode();
		}
	
	public String toString() {
		return super.toString() + " (" + getCategoría() + ")";
	}
	
//OPERACIONES
	
//	imparteAsignatura, que dadas una asignatura y una dedicación (el número de créditos que el profesor 
//	imparte en la asignatura), añade la asignatura a las asignaturas que imparte el profesor. 
	
//	Si la asignatura ya era impartida por el profesor, se actualiza la dedicación. Un profesor puede impartir una asignatura si la dedicación es mayor 
//	a cero, no supera el número de créditos de la asignatura y el total de créditos que imparte no puede superar los 24 créditos.
	
	public void imparteAsignaturas(Asignatura a, Double creditos) {
		Checkers.check("", creditos > 0);
		Checkers.check("", creditos < a.creditos());
		Checkers.check("", getDedicacionTotal() + creditos <= 24);
		this.creditosPorAsignatura.put(a, creditos);
	}
	
//	getDedicacionTotal, que devuelve el total de créditos que imparte el profesor, que se calculan como la suma los créditos de dedicación a las asignaturas.

	public Double getDedicacionTotal() {
		Double result = 0.0;
//		for(Asignatura clave : creditosPorAsignatura.keySet()) {
//			result += creditosPorAsignatura.get(clave);
//		}
		Collection<Double> valores = creditosPorAsignatura.values();
		for(Double creditos : valores) {
			result += creditos;
		}
		return result;
	}
	
//	eliminaAsignatura, que dada una asignatura, elimina la asignatura de las asignaturas que imparte el profesor. Si la asignatura no está registrada, la operación no tiene efecto.

	public void eliminaAsignatura(Asignatura a) {
		creditosPorAsignatura.remove(a);
	}
	
//	getAsignaturas, devuelve una lista con las asignaturas en las que está involucrado el profesor.
	
	public List<Asignatura> getAsignatura(){
		return new ArrayList<>(creditosPorAsignatura.keySet());
	}
	
//	getCreditos, devuelve una lista de valores Double con los créditos impartidos por el profesor.
	
	public List<Double> getCreditos(){
		return new ArrayList<>(creditosPorAsignatura.values());
	}
	
//	dedicacionAsignatura, que dada una asignatura, devuelve el número de créditos impartidos en esa asignatura. Si el profesor no la imparte, devuelve 0.0.
	
	public Double dedicacionAsignatura(Asignatura clave) {
		return creditosPorAsignatura.getOrDefault(clave, 0.0);
	}
	
}