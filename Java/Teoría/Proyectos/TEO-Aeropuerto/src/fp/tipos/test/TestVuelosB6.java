package fp.tipos.test;

import java.util.List;
import java.util.Map;
import java.util.Optional;

import fp.tipos.FactoriaVuelos;
import fp.tipos.Vuelo;
import fp.tipos.VuelosB6;

public class TestVuelosB6 {

	public static void main(String[] args) {
		List<Vuelo> listaVuelos = FactoriaVuelos.leeVuelos("./data/aeropuerto.csv");
		VuelosB6 vuelos = new VuelosB6("Nombre", listaVuelos);
		
		testGetVueloMasBaratoPorDestino1(vuelos);
		testGetVueloMasBaratoPorDestino2(vuelos);
		testGetCodigoVueloMasBaratoPorDestino(vuelos);
		
	}
	
	private static void testGetVueloMasBaratoPorDestino1(VuelosB6 vuelos) {
		System.out.println(" EJERCICIO1=======================");
		System.out.println(" ===testGetVueloMasBaratoPorDestino1 ==========");
		System.out.println(" El vuelo más barato por destino es:");
		for (Map.Entry<String, Optional<Vuelo>> par : vuelos.getVueloMasBaratoPorDestino1().entrySet()) {
			System.out.println("    " + par.getKey() + "=" + par.getValue());
		}
	}
	
	private static void testGetVueloMasBaratoPorDestino2(VuelosB6 vuelos) {
		System.out.println(" EJERCICIO1=======================");
		System.out.println(" ===testGetVueloMasBaratoPorDestino2 ==========");
		System.out.println(" El vuelo más barato por destino es:");
		for (Map.Entry<String, Vuelo> par : vuelos.getVueloMasBaratoPorDestino2().entrySet()) {
			System.out.println("    " + par.getKey() + "=" + par.getValue());
		}
	}
	
	private static void testGetCodigoVueloMasBaratoPorDestino(VuelosB6 vuelos) {
		System.out.println(" EJERCICIO2=======================");
		System.out.println(" ===testGetCodigoVueloMasBaratoPorDestino ==========");
		System.out.println(" El código del vuelo más barato por destino es:");
		for (Map.Entry<String, String> par : vuelos.getCodigoVueloMasBaratoPorDestino().entrySet()) {
			System.out.println("    " + par.getKey() + "=" + par.getValue());
		}
	}

}
