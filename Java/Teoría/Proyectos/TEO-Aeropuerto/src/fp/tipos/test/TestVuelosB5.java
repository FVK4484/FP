package fp.tipos.test;

import java.time.LocalDate;

import java.util.List;
import java.util.Map;
import java.util.Set;

import fp.tipos.FactoriaVuelos;
import fp.tipos.Vuelo;
import fp.tipos.VuelosB5;

public class TestVuelosB5 {

	public static void main(String[] args) {
		List<Vuelo> listaVuelos = FactoriaVuelos.leeVuelos("./data/aeropuerto.csv");
		VuelosB5 vuelos = new VuelosB5("Nombre", listaVuelos);
		
		testGetNumDestinosDiferentesFecha(vuelos, LocalDate.of(2023, 6, 4));
		testGetVuelosOrdenados(vuelos);
		testGetDestinosOrdenados(vuelos, Character.valueOf('B'));
		testGetDestinosOrdenadosPorLongitud(vuelos);
		testGetVuelosPorFecha(vuelos);
		testGetVuelosPorFecha2(vuelos);
		testGetNumVuelosPorFecha(vuelos);
		testGetNumPlazasPorDestino(vuelos);
		testGetPrecioMedioPorDestino(vuelos);
		testGetFechasPorDestino(vuelos);

	}
	
	private static void testGetNumDestinosDiferentesFecha(VuelosB5 vuelos, LocalDate f) {
		System.out.println(" ===testGetNumDestinosDiferentesFecha ==========");
		System.out.println(" Hay " + vuelos.getNumDestinosDiferentesFecha(f) + " destinos distintos en la fecha " + f + ".");
	}
	
	private static void testGetVuelosOrdenados(VuelosB5 vuelos) {
		System.out.println(" ===testGetVuelosOrdenados ==========");
		System.out.println(" Los vuelos ordenados son:");
		for (Vuelo vuelo : vuelos.getVuelosOrdenados()) {
			System.out.println("   " + vuelo);
		}
	}
	
	private static void testGetDestinosOrdenados(VuelosB5 vuelos, Character l) {
		System.out.println(" ===testGetDestinosOrdenados ==========");
		System.out.println(" Los destinos ordenados son:");
		for (String destino : vuelos.getDestinosOrdenados(l)) {
			System.out.println("    " + destino);
		}
	}
	
	private static void testGetDestinosOrdenadosPorLongitud(VuelosB5 vuelos) {
		System.out.println(" ===testGetDestinosOrdenadosPorLongitud ==========");
		System.out.println(" Los destinos ordenados por destino son:");
		for (String destino : vuelos.getDestinosOrdenadosPorLongitud()) {
			System.out.println("    " + destino);
		}
	}
	
	private static void testGetVuelosPorFecha(VuelosB5 vuelos) {
		System.out.println(" ===testGetVuelosPorFecha ==========");
		System.out.println(" Los vuelos por fecha son:");
		for (Map.Entry<LocalDate, List<Vuelo>> par : vuelos.getVuelosPorFecha().entrySet()) {
			LocalDate fecha = par.getKey();
			List<Vuelo> listaVuelos = par.getValue();
			System.out.println("   " + fecha + "=" + listaVuelos);
		}
		
	}
	
	private static void testGetVuelosPorFecha2(VuelosB5 vuelos) {
		System.out.println(" ===testGetVuelosPorDestino ==========");
		System.out.println(" Los vuelos por destino son:");
		for (Map.Entry<LocalDate, Set<Vuelo>> par : vuelos.getVuelosPorFecha2().entrySet()) {
			System.out.println("   " + par.getKey() + "=" + par.getValue());
		}
	}
	
	private static void testGetNumVuelosPorFecha(VuelosB5 vuelos) {
		System.out.println(" ===testGetNumVuelosPorFecha ==========");
		System.out.println(" El número de vuelos por fecha es:");
		for (Map.Entry<LocalDate, Integer> par : vuelos.getNumVuelosPorFecha().entrySet()) {
			System.out.println("   " + par.getKey() + "=" + par.getValue());
		}
	}
	
	private static void testGetNumPlazasPorDestino(VuelosB5 vuelos) {
		System.out.println(" ===testGetNumPlazasPorDestino ==========");
		System.out.println(" El número de plazas por destino es:");
		for (Map.Entry<String, Integer> par : vuelos.getNumPlazasPorDestino().entrySet()) {
			System.out.println("   " + par.getKey() + "=" + par.getValue());
		}
	}
	
	private static void testGetPrecioMedioPorDestino(VuelosB5 vuelos) {
		System.out.println(" ===testGetPrecioMedioPorDestino ==========");
		System.out.println(" El precio medio por destino es:");
		for (Map.Entry<String, Double> par : vuelos.getPrecioMedioPorDestino().entrySet()) {
			System.out.println("   " + par.getKey() + "=" + par.getValue());
		}
	}
	
	private static void testGetFechasPorDestino(VuelosB5 vuelos) {
		System.out.println(" ===testGetFechasPorDestino() ==========");
		System.out.println(" Las fechas por destino son:");
		for (Map.Entry<String, Set<LocalDate>> par : vuelos.getFechasPorDestino().entrySet()) {
			System.out.println("   " + par.getKey() + "=" + par.getValue());
		}
	}

}
