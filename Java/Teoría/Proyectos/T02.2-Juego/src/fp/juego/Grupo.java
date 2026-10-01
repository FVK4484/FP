package fp.juego;

import java.util.ArrayList;
import java.util.List;
import java.util.Objects;

public class Grupo {
	private String nombre;
	private List<Personaje> personajes;
	
	public Grupo(String nombre) {
		this.nombre = nombre;
		this.personajes = new ArrayList<>();
	}

	public String getNombre() {
		return nombre;
	}

	public List<Personaje> getPersonajes() {
		return personajes;
	}
	
	public Integer getNumeroPersonajes() {
		return personajes.size();
	}

	public void agregarMiembro(Personaje personaje) {
		List<Personaje> miembros = getPersonajes();
		if (!personajes.contains(personaje)) {
			miembros.add(personaje);
		}
	}
	
	public String atacarTodos() {
		String resultado = "🔥 ¡El ejército EjercitoFP entra en batalla! 🔥 \n";
		for (Personaje personaje : personajes) {
			resultado += personaje.atacar() + "\n";
		}
		return resultado;
	}

	public String toString() {
		String resultado = "Ejercito " + nombre + ": " + getNumeroPersonajes() + "miembros\n";
		for (Personaje personaje : personajes) {
			resultado += personaje.toString() + "\n";
		}
		return resultado;
	}

	public int hashCode() {
		return Objects.hash(nombre, personajes);
	}

	public boolean equals(Object obj) {
		if (this == obj)
			return true;
		if (obj == null)
			return false;
		if (getClass() != obj.getClass())
			return false;
		Grupo other = (Grupo) obj;
		return Objects.equals(nombre, other.nombre) && Objects.equals(personajes, other.personajes);
	}
}
