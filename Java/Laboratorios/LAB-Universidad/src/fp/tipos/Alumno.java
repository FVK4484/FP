package fp.tipos;

import java.time.LocalDate;

import java.util.ArrayList;
import java.util.Collections;
import java.util.HashMap;
import java.util.Set;
import java.util.SortedMap;
import java.util.TreeMap;

import fp.utiles.Checkers;

import java.util.List;
import java.util.Map;
import java.util.HashSet;

public class Alumno extends Persona{
	
	private Set<Asignatura> asignaturas;
	private Expediente expediente;
	
	public Alumno(String dNI, String nombre, String apellidos, LocalDate fechaNacimiento, String email) {
		super(dNI, nombre, apellidos, fechaNacimiento, email);
		Checkers.check("el email debe de terminar en @alum.us.es", !email.isEmpty() && email.endsWith("@alum.us.es"));
		this.asignaturas = new HashSet<>();
		this.expediente = expediente;
	}
	
	public Set<Asignatura> getAsignaturas() {
		return new HashSet<Asignatura>(asignaturas);
	}
	
	private Integer getCurso() {
		Integer res = 0;
		List<Integer> cursos = new ArrayList<>();
		for(Asignatura a: asignaturas) {
			cursos.add(a.curso());
		}
		if(!cursos.isEmpty()) {
			res = Collections.max(cursos);
		}
		return res;
	}
	
	public boolean equals(Object o) {
		boolean res =false;
		if(o instanceof Grado) {
			res = super.equals(o);
		}
		return res;
	}
	
	public int HashCode() {
		return super.hashCode();
	}
	
	public String toString() {
		return "("+ getCurso() + ")º " + super.toString();
	}
	
	// OPERACIONES.
	
	public void matriculaAsignatura(Asignatura a){
		Checkers.check("", !estaMatriculado(a));
		asignaturas.add(a);
	}
	
	public boolean estaMatriculado(Asignatura a) {
		return asignaturas.contains(a);
	}
	
	public void eliminaAsginatura(Asignatura a) {
		Checkers.check("", estaMatriculado(a));
		asignaturas.remove(a);
	}
	
//  OPERACIONES
	
//	getCalificacionPorAsignatura, que devuelve un SortedMap<Asignatura, Calificacion> que hace corresponder a cada asignatura que aparece 
//	en el expediente del alumno la calificación máxima obtenida en ella.
	
	public SortedMap<Asignatura, Calificacion> getCalificacionPorAsignatura() {
		SortedMap<Asignatura, Calificacion> dicc = new TreeMap<>();
		for(Nota nota : expediente.getNotas()) {
			Asignatura clave = nota.asignatura();
			Calificacion valor = nota.getCalificacion();
			if(!dicc.containsKey(clave)) {
				dicc.put(clave, valor);
			} else {
				Calificacion valorAntiguo = dicc.get(clave);
				dicc.put(clave, valorAntiguo.compareTo(valor) < 0 ?valor:valorAntiguo);
			}
		}
		return dicc;
	}
	
//	getNumAsignaturasPorCurso, que devuelve un Map<Integer, Integer> que asocia un curso y el número de asignaturas de ese curso en las que 
//	está matriculado el alumno.	
	
	public Map<Integer, Integer> getNumAsignaturasPorCurso() {
		Map<Integer, Integer> dicc = new HashMap<>();
		for(Asignatura a : asignaturas) {
			Integer clave = a.curso();
			if(!dicc.containsKey(clave)) {
				dicc.put(clave, 1);
			}
			else {
				Integer valor = dicc.get(clave);
				valor++;
				dicc.put(clave, valor);
			}
		}
		return dicc;
	}
	
	
	
	
	
	

}