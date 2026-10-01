package fp.tipos.test;

import java.util.List;

import fp.tipos.FactoriaVuelos;
import fp.tipos.Vuelo;

import fp.tipos.VuelosB4;

public class TestVuelosB4 {

	public static void main(String[] args) {
		List<Vuelo> listaVuelos = FactoriaVuelos.leeVuelos("./data/aeropuerto.csv");
		VuelosB4 vuelos = new VuelosB4("Nombre", listaVuelos);
		
		testExisteVueloDestino(vuelos, "Madrid");

	}
	
private static void testExisteVueloDestino(VuelosB4 vuelos, String destino) {
		
		System.out.println("===testExisteVueloDestino ===");
		System.out.println("Existe vuelo a " + destino + ": " + vuelos.getExisteVueloDestino(destino));
		
	}
	
}

