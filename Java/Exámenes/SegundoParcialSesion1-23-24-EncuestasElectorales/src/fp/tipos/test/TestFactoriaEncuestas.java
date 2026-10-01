package fp.tipos.test;

import java.util.List;

import fp.tipos.Encuesta;
import fp.tipos.FactoriaEncuestas;

public class TestFactoriaEncuestas {
	public static void testFactoriaEncuestas() {
		List<Encuesta> encuestas = FactoriaEncuestas.leeEncuestas("./data/encuestas_electorales.csv");
		for (Encuesta encuesta : encuestas) {
			System.out.println(encuesta);
		}
	}

	public static void main(String[] args) {
		try {
			testFactoriaEncuestas();
		} catch (Exception e) {
			System.out.println("Excepción capturada: ");
			System.out.println(e.getMessage());
		}
	}

}
