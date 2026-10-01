package fp.partidos.test;

import fp.partidos.Resultado;

public class TestResultado {

	public static void main(String[] args) {
		
		// Resultado
		Resultado r1 = new Resultado(34, 2, 1);
		System.out.println(r1);
		
		// Checkers
		try {
		Resultado r2  = new Resultado(-2, 2, 1);
		System.out.println(r2);
		} catch(Exception e) {
			System.out.println("Excepción capturada: ");
			System.out.println(e.getMessage());
		}
		
		try {
		Resultado r3  = new Resultado(4, -2, 1);
		System.out.println(r3);
		} catch(Exception e) {
			System.out.println("Excepción capturada: ");
			System.out.println(e.getMessage());
		}
		
		// Operación parse
		String res = "22-0-1";
		System.out.println(Resultado.parse(res));
		
	}

}
