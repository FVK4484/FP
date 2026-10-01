package fp.tipos;

import java.time.Duration;
import java.util.SortedMap;

public class TestAgenciaBus {
	private static void testGetMaximaDuracion(AgenciaBus agencia) {
		try {
			Duration res = agencia.getMaximaDuracion();
			String msg = String.format("La duración máxima es %s", res);
			System.out.println(msg);
		} catch (Exception e) {
			System.out.println("Capturada excepcion inesperada " + e.getMessage());
				}
	}
	
	private static void testAñadirTiempoDescanso(AgenciaBus agencia, String parada, Integer minutos) {
		try {
			String msg = String.format("Se van a añadir %d minutos a los viajes con la parada %s, que son", minutos, parada);
			System.out.println(msg);
			mostrar_viajes_con_parada(agencia, parada);
			agencia.añadirTiempoDescanso(parada, minutos);
			System.out.println("Los viajes tras la modificación son");
			mostrar_viajes_con_parada(agencia, parada);
			} catch (Exception e) {
				System.out.println("Capturada excepcion inesperada " + e.getMessage());
				}
	}
	

	private static void mostrar_viajes_con_parada(AgenciaBus agencia, String parada) {
		// TODO Auto-generated method stub
		
	}

	private static void testGetDuracionMinimaPorDestino(AgenciaBus agencia, TipoViaje tipo){
		try {
			String msg = String.format("La duración minima por cada destino para "
					+ "viajes de tipo %s es ", tipo);
			System.out.println(msg);
			SortedMap<String, Duration> res = agencia.getDuracionMinimaPorDestino(tipo);
			res.entrySet().stream()
			.forEach(System.out::println);
			} catch (Exception e) {
				System.out.println("Capturada excepcion inesperada " +
						e.getMessage());
			}
	
}	

	public static void main(String[] args) {
		AgenciaBus agencia = FactoriaViajes.leerViajes("Flixbus", "data/viajes.csv");
		System.out.println("Test 4.1 ==============================================");
		testGetMaximaDuracion(agencia);
		System.out.println("Test 4.2 =============================================");
		String parada = "Bilbao";
		Integer minutos = 30;
		testAñadirTiempoDescanso(agencia, parada, minutos);
		TipoViaje tipo = TipoViaje.CANCELADO;
		testGetDuracionMinimaPorDestino(agencia, tipo);
	}

}
