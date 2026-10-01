package fp.publicaciones;

import java.util.Objects;

import fp.utiles.Checkers;

public record Autor(String nombre, String afiliacion, Boolean correspondencia) {
	
	public Autor {
		Checkers.check("El nombre del autor (" + nombre +") no puede empezar por asterisco."
				, !nombre.startsWith("*"));
	}

	public int hashCode() {
		return Objects.hash(afiliacion, nombre);
	}

	public boolean equals(Object obj) {
		if (this == obj)
			return true;
		if (obj == null)
			return false;
		if (getClass() != obj.getClass())
			return false;
		Autor other = (Autor) obj;
		return Objects.equals(afiliacion, other.afiliacion) && Objects.equals(nombre, other.nombre);
	}	

}
