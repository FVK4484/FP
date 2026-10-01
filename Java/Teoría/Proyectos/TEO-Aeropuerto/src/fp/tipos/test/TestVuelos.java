package fp.tipos.test;

import java.util.List;

import fp.tipos.FactoriaVuelos;
import fp.tipos.Vuelo;
import fp.tipos.Vuelos;

public class TestVuelos {

	public static void main(String[] args) {
		
		List<Vuelo> listaVuelos = FactoriaVuelos.leeVuelos("./data/aeropuerto.csv");
		
		// 2. Creamos el objeto contenedor (la clase que queremos probar)
		Vuelos misVuelos = new Vuelos("Air Europa", listaVuelos);
		
		// 3. Llamamos a los métodos de prueba
		testConstructorYToString(misVuelos);
		testGetNumeroVuelos(misVuelos);
		testGetNumeroPasajeros(misVuelos);
		testGetPrecioMedio(misVuelos);
		testGetNumeroDestinos(misVuelos);
		testExisteVueloDestino(misVuelos);
		testGetNumPasajerosDestino(misVuelos);
		
		// Estas operaciones modifican la lista, las dejamos para el final
		testIncorporaVuelo(misVuelos);
		testEliminaVuelo(misVuelos);
		testOrdena(misVuelos);
		
	}

	private static void testConstructorYToString(Vuelos vuelos) {
		System.out.println("\n### Test Constructor y toString ###");
		System.out.println(vuelos);
	}

	private static void testGetNumeroVuelos(Vuelos vuelos) {
		System.out.println("\n### Test getNumeroVuelos ###");
		System.out.println("Número total de vuelos: " + vuelos.getNumeroVuelos());
	}

	private static void testGetNumeroPasajeros(Vuelos vuelos) {
		System.out.println("\n### Test getNumeroPasajeros ###");
		System.out.println("Total pasajeros: " + vuelos.getNumeroPasajeros());
	}

	private static void testGetPrecioMedio(Vuelos vuelos) {
		System.out.println("\n### Test getPrecioMedio ###");
		// Usamos printf para mostrar solo 2 decimales y que quede bonito
		System.out.printf("Precio medio: " + vuelos.getPrecioMedio() + " €");
	}
	
	private static void testGetNumeroDestinos(Vuelos vuelos) {
		System.out.println("\n### Test getNumeroDestinos ###");
		System.out.println("Destinos distintos: " + vuelos.getNumeroDestinos());
	}
	
	private static void testExisteVueloDestino(Vuelos vuelos) {
		System.out.println("\n### Test existeVueloDestino ###");
		String destino1 = "Barcelona";
		String destino2 = "Marte";
		System.out.println("¿Existe vuelo a " + destino1 + "?: " + vuelos.existeVueloDestino(destino1));
		System.out.println("¿Existe vuelo a " + destino2 + "?: " + vuelos.existeVueloDestino(destino2));
	}
	
	private static void testGetNumPasajerosDestino(Vuelos vuelos) {
		System.out.println("\n### Test getNumPasajerosDestino ###");
		String destino = "Barcelona";
		System.out.println("Pasajeros a " + destino + ": " + vuelos.getNumPasajerosDestino(destino));
	}

	private static void testIncorporaVuelo(Vuelos vuelos) {
		System.out.println("\n### Test incorporaVuelo ###");
		System.out.println("Vuelos antes: " + vuelos.getNumeroVuelos());
		
		// Cogemos el primer vuelo de la lista y lo volvemos a añadir (para no crear uno a mano)
		Vuelo v = vuelos.getVuelos().get(0); 
		vuelos.incorporaVuelo(v);
		
		System.out.println("Vuelos después: " + vuelos.getNumeroVuelos());
	}

	private static void testEliminaVuelo(Vuelos vuelos) {
		System.out.println("\n### Test eliminaVuelo ###");
		System.out.println("Vuelos antes: " + vuelos.getNumeroVuelos());
		
		// Eliminamos el primer vuelo que haya
		Vuelo v = vuelos.getVuelos().get(0);
		vuelos.eliminaVuelo(v);
		
		System.out.println("Vuelos después: " + vuelos.getNumeroVuelos());
	}
	
	private static void testOrdena(Vuelos vuelos) {
		System.out.println("\n### Test ordena ###");
		System.out.println("--- Primeros 3 vuelos ANTES de ordenar ---");

		vuelos.getVuelos().stream()
		.limit(3)
		.forEach(System.out::println);
		
		vuelos.ordena();
		
		System.out.println("--- Primeros 3 vuelos DESPUÉS de ordenar ---");
		vuelos.getVuelos().stream()
		.limit(3)
		.forEach(System.out::println);
	}
	
}