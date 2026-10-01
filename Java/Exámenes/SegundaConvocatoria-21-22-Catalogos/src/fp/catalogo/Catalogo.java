package fp.catalogo;

import java.util.HashSet;
import java.util.Map;
import java.util.Objects;
import java.util.Set;
import java.util.stream.Collectors;

public class Catalogo {
	
	private Set<Componente> componentes;
	
	public Catalogo() {
		
	}
	
	public Catalogo(Set<Componente> componentes) {
		this.componentes = new HashSet<>(componentes);
	}

	public Set<Componente> getComponentes() {
		return new HashSet<>(componentes);
	}

	public int hashCode() {
		return Objects.hash(componentes);
	}

	public boolean equals(Object obj) {
		if (this == obj)
			return true;
		if (obj == null)
			return false;
		if (getClass() != obj.getClass())
			return false;
		Catalogo other = (Catalogo) obj;
		return Objects.equals(componentes, other.componentes);
	}
	
	public String toString() {
		return "Catalogo [componentes=" + componentes + "]";
	}

	public void añadirComponente(Componente c) {
		componentes.add(c);
	}
	
	public void eliminarComponente(String n) {
		for (Componente comp : componentes) {
			if (comp.getNombre().equals("n")) {
				componentes.remove(comp);
			}
		}
	}
	
	// 1. Map<Tipo, Long> numeroComponentesPorTipoDeSuministrador(String suministrador): 
	// relaciona cada tipo de componente con el número de componentes de dicho tipo 
	// suministrados por suministrador. (1 punto)
	public Map<TipoComponente, Long> numeroComponentesPorTipoDeSuministrador(String suministrador) {
		return componentes.stream()
				.filter(c -> c.getSuministrador().equals(suministrador))
				.collect(Collectors.groupingBy(Componente::getTipoComponente, Collectors.counting()));
	}
	
	// 2. Set<String> componentesConCombinadoresConPrecioMaximo(Double precio): obtiene los 
	// nombres de los componentes que cumplen la siguiente propiedad: un componente pertenecerá 
	// al resultado si y solo si cada uno de sus combinadores no supera el precio dado como parámetro 
	// (el precio considerado es sin descuento). (1.25 puntos)
	public Set<String> componentesConCombinadoresConPrecioMaximo(Double precio) {
		Set<String> result = new HashSet<>();
		Boolean res = componentes.stream()
				.filter(c -> c.getCombinadores().contains(c.getNombre()))
				.allMatch(c -> c.getPrecio() < precio);
		if (res) {
			result = componentes.stream()
					.map(Componente::getNombre)
					.collect(Collectors.toSet());
		}
		return result;
	}
	
}
