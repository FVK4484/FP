package fp.tipos;

import java.util.Objects;

public record Nota(Asignatura asignatura, Integer anyoInicioCurso, TipoConvocatoria convocatoria, 
		Double valorNumerico, Boolean mencionHonor) implements Comparable <Nota>{
	public Nota {
		checkValorNumerico(valorNumerico);
		checkMencionHonor(mencionHonor);
	}
	
	public Calificacion getCalificacion() {
		Calificacion result;
		if (valorNumerico < 5) {
			result = Calificacion.SUSPENSO;
		} else if (valorNumerico >= 5 && valorNumerico < 7) {
			result = Calificacion.APROBADO;
		} else if (valorNumerico >= 7 && valorNumerico < 9) {
			result = Calificacion.NOTABLE;
		} else if (valorNumerico >= 9 && !mencionHonor) {
			result = Calificacion.SOBRESALIENTE;
		} else {
			result = Calificacion.MATRICULA_HONOR;
		}
		return result;
	}
	
	private void checkValorNumerico(Double valorNumerico) {
		if (valorNumerico < 0 || valorNumerico > 10) {
			throw new IllegalArgumentException
			("El valor numérico debe estar comprendido entre 0 y 10.");
		}
		
	}
	
	private void checkMencionHonor(Boolean mencionHonor) {
		if (valorNumerico < 9 && mencionHonor == true) {
			throw new IllegalArgumentException
			("Una nota sólo puede tener mención de honor si su valor numérico es igual o superior a 9.");
		}
		
	}

	public String toString() {
		return asignatura.toString() + ", " + anyoInicioCurso + "-"+ ((anyoInicioCurso % 100) + 1) +", " 
	+ convocatoria + " " + valorNumerico + ", " + getCalificacion();
	}

	public int hashCode() {
		return Objects.hash(anyoInicioCurso, asignatura, convocatoria);
	}

	public boolean equals(Object obj) {
		if (this == obj)
			return true;
		if (obj == null)
			return false;
		if (getClass() != obj.getClass())
			return false;
		Nota other = (Nota) obj;
		return Objects.equals(anyoInicioCurso, other.anyoInicioCurso) && Objects.equals(asignatura, other.asignatura)
				&& convocatoria == other.convocatoria;
	}

	public int compareTo(Nota n) {
		Integer res = anyoInicioCurso.compareTo(n.anyoInicioCurso);
		if (res == 0) {
			res = asignatura.compareTo(n.asignatura);
			if (res == 0) {
				res = convocatoria.compareTo(n.convocatoria);
			}
		} 
		return res;
	}
	
}
