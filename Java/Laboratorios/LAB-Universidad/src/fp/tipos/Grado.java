package fp.tipos;

import java.util.ArrayList;
import java.util.Collections;
import java.util.HashSet;
import java.util.List;
import java.util.Objects;
import java.util.Set;

public class Grado implements Comparable<Grado>{
	private String nombre;
	private Set<Asignatura> asignaturasObligatorias;
	private Set<Asignatura> asignaturasOptativas;
	private Integer numeroCreditosOptativos;
	
	public Grado(String nombre, Set<Asignatura> asignaturasObligatorias, Set<Asignatura> asignaturasOptativas,
			Integer numeroCreditosOptativos) {
		checkAsignaturasOptativas(asignaturasOptativas);
		checkCreditosAsignaturasOptativas(asignaturasOptativas, numeroCreditosOptativos);
		this.nombre = nombre;
		this.asignaturasObligatorias = new HashSet<>(asignaturasObligatorias);
		this.asignaturasOptativas = new HashSet<>(asignaturasOptativas);
		this.numeroCreditosOptativos = numeroCreditosOptativos;
	}
	
	private void checkCreditosAsignaturasOptativas(Set<Asignatura> asignaturasOptativas,
			Integer numeroCreditosOptativos) {
		Double sumaCreditos = sumaCreditosAsignaturas(asignaturasOptativas);
		if (!(numeroCreditosOptativos > 0 && numeroCreditosOptativos <= sumaCreditos)) {
			throw new IllegalArgumentException();
		}
		
	}

	private Double sumaCreditosAsignaturas(Set<Asignatura> asignaturasOptativas2) {
		Double result = 0.0;
		for (Asignatura a : asignaturasOptativas) {
			result += a.creditos();
		}
		return result;
	}

	private void checkAsignaturasOptativas(Set<Asignatura> optativas) {
		Boolean condicion = todasMismoNumeroCreditos(optativas);
		if (!condicion) {
			throw new IllegalArgumentException();
		}
	}

	private Boolean todasMismoNumeroCreditos(Set<Asignatura> optativas) {
		Boolean result = true;
		List<Double> creditos = new ArrayList<>();
		for (Asignatura a : optativas) {
			creditos.add(a.creditos());
		}
		if (!(creditos.isEmpty() || Collections.frequency(creditos, 
				creditos.getFirst()) == creditos.size())) {
			result = false;
		}
		return result;
	}

	public String getNombre() {
		return nombre;
	}

	public Set<Asignatura> getAsignaturasObligatorias() {
		return new HashSet<>(asignaturasObligatorias);
	}

	public Set<Asignatura> getAsignaturasOptativas() {
		return new HashSet<>(asignaturasOptativas);
	}

	public Integer getNumeroCreditosOptativos() {
		return numeroCreditosOptativos;
	}

	public int hashCode() {
		return Objects.hash(nombre);
	}

	public boolean equals(Object obj) {
		if (this == obj)
			return true;
		if (obj == null)
			return false;
		if (getClass() != obj.getClass())
			return false;
		Grado other = (Grado) obj;
		return Objects.equals(nombre, other.nombre);
	}

	public String toString() {
		return nombre;
	}

	public int compareTo(Grado g) {
		Integer res = getNombre().compareTo(g.getNombre());
		return res;
	}
	
}
