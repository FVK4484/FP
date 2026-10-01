package fp.tipos.test;

import java.time.LocalDate;
import java.util.List;

import fp.tipos.Encuesta;
import fp.tipos.EstadisticasEncuestas;
import fp.tipos.FactoriaEncuestas;
import fp.tipos.TipoEncuesta;

public class TestEstadisticasEncuestas {
	
	public static void main(String[] args) {
		List<Encuesta> est1 = FactoriaEncuestas.leeEncuestas("./data/encuestas_electorales.csv");
		EstadisticasEncuestas est = new EstadisticasEncuestas(est1.stream());
//		testCreaEstadisticas(est);
		
		System.out.println("EJ1" + " =".repeat(80));
		testGetMediaNumEncuestadosConsultorayFecha(est, "Consultora A", 
				LocalDate.of(2024, 5, 29)); 
		testGetMediaNumEncuestadosConsultorayFecha(est, "Consultora B", 
				LocalDate.of(2024, 5, 26));
		
		System.out.println("EJ2" + " =".repeat(80));
		testGetEncuestaMasEncuestadosPorDia(est, TipoEncuesta.TELEFONICA);
		
		System.out.println("EJ3" + " =".repeat(80));
		testGetPartidosMasFrecuentesOrdenados(est, 5);
		
	 } 
	 
//	 private static void testCreaEstadisticas(EstadisticasEncuestas est) {
//		 try {
//			 List<Encuesta> encuestas = est.getEncuestas();
//			 System.out.println(String.format("Leidas %d encuestas", 
//					 encuestas.size())); 
//			 int i = 0; 
//			 for (Encuesta e: encuestas) {
//				 System.out.println("\t" + (i++) + "-" + e); 
//			 } 
//		 } catch (Exception e) {
//			 System.out.println(e.getMessage()); 
//		 } 
//	 } 
	 
	 private static void testGetMediaNumEncuestadosConsultorayFecha(EstadisticasEncuestas est, String consultora, LocalDate fechaMaxima){ 
		 try {
			 Double m = est.getMediaNumEncuestadosConsultorayFecha(consultora, fechaMaxima); 
			 String msg = String.format("La media de la consultora %s con fecha de fin anterior a %s es %f", consultora, fechaMaxima, m); 
			 System.out.println(msg); 
		 } catch (Exception e) { 
			 System.out.println(e.getMessage()); 
		 } 
	 } 
	 
	 private static void testGetEncuestaMasEncuestadosPorDia(EstadisticasEncuestas est, TipoEncuesta tipo) {
		 try { 
			 	Encuesta m = est.getEncuestaMasEncuestadosPorDia(tipo); 
			 	String msg = String.format("\tLa encuesta de tipo %s con mayor ratio de encuestados por día es :\n%s ", tipo, m); 
			 	System.out.println(msg); 
		} catch (Exception e) { 
				 System.out.println(e.getMessage()); 
		} 
	}
	 
	 private static void testGetPartidosMasFrecuentesOrdenados(EstadisticasEncuestas est, Integer n) {
		 try {
			 List<String> m = est.getPartidosMasFrecuentesOrdenados(n);
			 String msg = String.format("\tLos %s partidos más frecuentes en las encuestas son:\n%s ", n, m); 
			 System.out.println(msg);
		 } catch (Exception e) {
			 System.out.println(e.getMessage());
		 }
	 }
	 
}
