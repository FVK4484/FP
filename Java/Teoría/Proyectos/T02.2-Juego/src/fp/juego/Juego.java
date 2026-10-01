package fp.juego;

public class Juego {
	
	public static void testPersonajes() {
		Personaje guerrero = new Guerrero("Arthur", 10, 100, 80);
		Personaje mago = new Mago("Merlín", 12, 80, 120);
		Personaje arquero = new Arquero("Robin", 11, 90, 95);
		System.out.println(guerrero);
		System.out.println(guerrero.atacar());
		System.out.println(mago);
		System.out.println(mago.atacar());
		System.out.println(arquero);
		System.out.println(arquero.atacar());
	}
	
	public static void testGrupo() {
		Personaje guerrero = new Guerrero("Arthur", 10, 100, 80);
		Personaje mago = new Mago("Merlín", 12, 80, 120);
		Personaje arquero = new Arquero("Robin", 11, 90, 95);
		Grupo grupo = new Grupo("EjercitoFP");
		grupo.agregarMiembro(guerrero);
		grupo.agregarMiembro(mago);
		grupo.agregarMiembro(arquero);
		System.out.println(grupo);
		System.out.println();
		System.out.println();
		System.out.println(grupo.atacarTodos());
	}

	public static void main(String[] args) {
		testPersonajes();
		System.out.println();
		System.out.println();
		testGrupo();
	}

}
