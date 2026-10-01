package fp.tipos;

import java.util.HashSet;
import java.util.Set;

import fp.utiles.Checkers;

public class Despacho extends Espacio{
	
	private Set<Profesor> profesores;

	public Despacho(String nombre, Integer capacidad, Integer planta, Set<Profesor> profesores) {
		super(TipoEspacio.OTRO, nombre, capacidad, planta);
		Checkers.check("El número de profesores que ocupan un despacho no puede superar la capacidad del mismo",
				profesores.size() <= capacidad);
		this.profesores = new HashSet<>(profesores);
	}

	
	public Despacho(TipoEspacio tipoEspacio, String nombre, Integer capacidad, Integer planta) {
		this(nombre, capacidad, planta, new HashSet<Profesor>());
	}

	public Set<Profesor> getProfesores() {
		return profesores;
	}

	public void setProfesores(Set<Profesor> profesores) {
		Checkers.check("El número de profesores que ocupan un despacho no puede superar la capacidad del mismo",
				profesores.size() <= getCapacidad());
		this.profesores = new HashSet<>(profesores);
	}	
	
	public void setTipo(TipoEspacio nuevoTipo) {
		throw new UnsupportedOperationException();
	}

}
