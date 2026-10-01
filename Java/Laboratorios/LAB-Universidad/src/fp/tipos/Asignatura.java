package fp.tipos;

import java.util.Objects;

public record Asignatura (String nombre, String codigo, Double creditos, 
		TipoAsignatura tipoAsignatura, Integer curso) implements Comparable<Asignatura>{
	public Asignatura{
		checkCodigo(codigo);
		checkCreditos(creditos);
		checkCurso(curso);
	}
	
	public String getAcronimo() {
		String result = "";
//		Integer i = 0;
//		for (i = 0; i < nombre.length(); i++) {
//			if (Character.isUpperCase(nombre.charAt(i))) {
//				result += nombre.charAt(i);
//			}
//		}
		for (Character c : nombre.toCharArray()) {
			if (Character.isUpperCase(c)) {
				result += c;
			}
		}
		return result;
	}
	
	private void checkCodigo(String codigo) {
		if (codigo.length() != 7) {
			throw new IllegalArgumentException
			("El código debe tener 7 dígitos.");
		}
	}
	
	private void checkCreditos(Double creditos) {
		if (creditos <= 0) {
			throw new IllegalArgumentException
			("Los créditos deben ser mayor que cero.");
		}
	}
	
	private void checkCurso(Integer curso) {
		if (curso <= 0 || curso > 4) {
			throw new IllegalArgumentException
			("Los grados constan de 4 años.");
		}
	}

	public String toString() {
		return codigo + " " + nombre;
	}

	public int hashCode() {
		return Objects.hash(codigo);
	}

	public boolean equals(Object obj) {
		if (this == obj)
			return true;
		if (obj == null)
			return false;
		if (getClass() != obj.getClass())
			return false;
		Asignatura other = (Asignatura) obj;
		return Objects.equals(codigo, other.codigo);
	}

	public int compareTo(Asignatura a) {
		Integer res = codigo.compareTo(a.codigo);
		return res;
	}
	
}
