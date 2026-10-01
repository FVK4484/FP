package fp.tipos.test;

import java.util.List;


import fp.tipos.FactoriaVuelos;
import fp.tipos.Vuelo;
import fp.tipos.VuelosB2;

public class TestVuelosB2 {

	public static void main(String[] args) {
		
		List<Vuelo> listaVuelos = FactoriaVuelos.leeVuelos("./data/aeropuerto.csv");
		VuelosB2 vuelos = new VuelosB2("Nombre", listaVuelos);
		
		testGetNumPasajerosDestino(vuelos, "Madrid");
		testGetNumPasajerosDestinoPrefijo(vuelos, "Barcelona");
		testGetRecaudacionDestino(vuelos, "Barcelona");
		testGetPrimerVueloDestino(vuelos, "Paris");
		testGetPrimerVueloDestinoMenorPrecio(vuelos, "Madrid");
		
	}
	
	private static void testGetNumPasajerosDestino(VuelosB2 vuelos, String destino) {
		
		System.out.println("===testGetNumPasajerosDestino ===");
		System.out.println("Pasajeros con destino " + destino + ": " + vuelos.getNumPasajerosDestino(destino));
		
	}
	
	private static void testGetNumPasajerosDestinoPrefijo(VuelosB2 vuelos, String s) {
		
		System.out.println("===testGetNumPasajerosDestinoPrefijo ===");
		System.out.println("Pasajeros con destino que empieza por " + s + ": " + vuelos.getNumPasajerosDestinoPrefijo(s));
		
	}
	
	private static void testGetRecaudacionDestino(VuelosB2 vuelos, String destino) {
		
		System.out.println("===testGetRecaudacionDestino ===");
		System.out.println("Recaudación de los vuelos a " + destino + ": " + vuelos.getRecaudacionDestino(destino));
		
	}
	
	private static void testGetPrimerVueloDestino(VuelosB2 vuelos, String destino) {
		
		System.out.println("===testGetPrimerVueloDestino ===");
		System.out.println("Primer vuelo a " + destino + ": " + vuelos.getPrimerVueloDestino(destino));
		
	}
	
	private static void testGetPrimerVueloDestinoMenorPrecio(VuelosB2 vuelos, String destino) {
		
		System.out.println("===testGetPrimerVueloDestinoMenorPrecio ===");
		System.out.println("Primer vuelo a " + destino + " con menor precio: " + vuelos.getPrimerVueloDestinoMenorPrecio(destino));
		
	}

}
