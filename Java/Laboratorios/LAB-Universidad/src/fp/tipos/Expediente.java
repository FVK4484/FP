package fp.tipos;

import java.util.ArrayList;
import java.util.List;
import java.util.Objects;

public class Expediente {
	private List<Nota> notas;
	
	public Expediente(List<Nota> notas) {
		super();
		this.notas = new ArrayList<>();
	}
	
	public Double notaMedia(Integer valorNumerico) {
		Double res = 0.;
		if(valorNumerico >= 5) {
			res = (double) notas.size()/2;
		}
		else {
			res = 0.0;
		}
		return res;
		}
	
	public String toString() {
		return "[" + notas + "]";
	}
	
	public boolean equals(Object o) {
		boolean res = false;
		if(o instanceof Expediente) {
			Expediente r = (Expediente) o;
			res = notas.equals(r.notas);
		}
		return res;
	}
	
	public int hashCode() {
		return Objects.hash(notas);
	}
	
	public void nuevaNota(Nota n) {
//		Añade la nota n al expediente. 
//		Si en el expediente ya existe una 
//		nota para la misma asignatura, convocatoria 
//		y curso académico (es decir, otra nota igual 
//				según el criterio de igualdad del tipo
//				Nota), se elimina la nota antigua y se
//		añade la nueva. Las notas se añaden siempre al
//		final de la lista.
		if (notas.contains(n)) {
			notas.remove(n);
		} else {
			notas.add(n);
		}
		
	}

	public List<Nota> getNotas() {
		return new ArrayList<Nota>(notas);
	}

}