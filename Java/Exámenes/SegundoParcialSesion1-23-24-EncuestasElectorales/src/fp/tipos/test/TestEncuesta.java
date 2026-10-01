package fp.tipos.test;

import java.time.LocalDate;
import java.util.ArrayList;
import java.util.List;

import fp.tipos.Encuesta;
import fp.tipos.Resultado;
import fp.tipos.TipoEncuesta;

public class TestEncuesta {
	
	public static void testEncuesta() {
		List<Resultado> lista = new ArrayList<>();
		
		Resultado resultado1 = new Resultado("Partido 1", 42.29);
		Resultado resultado2 = new Resultado("Partido 2", 49.52);
		Resultado resultado3 = new Resultado("Partido 3", 6.01);
		Resultado resultado4 = new Resultado("Partido 4", 1.76);
		Resultado resultado5 = new Resultado("Partido 5", 0.18);
		Resultado resultado6 = new Resultado("Partido 6", 0.23);
		
		lista.add(resultado1);
		lista.add(resultado2);
		lista.add(resultado3);
		lista.add(resultado4);
		lista.add(resultado5);
		lista.add(resultado6);
		
		Encuesta encuesta = new Encuesta("Consultora B",
				LocalDate.of(2024, 5, 18), 
				LocalDate.of(2024, 5, 27), 
				3203,
				"Espana",
				TipoEncuesta.INTERNET,
				16.15,
				lista);
		
		System.out.println(encuesta);
		System.out.println(encuesta.getRatioEncuestadosDia());
	}

	public static void main(String[] args) {
		try {
		testEncuesta();
		} catch (Exception e) {
			System.out.println("Excepción capturada: ");
			System.out.println(e.getMessage());
		}
	}

}
