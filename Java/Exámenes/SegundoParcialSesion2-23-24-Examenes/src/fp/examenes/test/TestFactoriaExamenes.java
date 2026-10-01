package fp.examenes.test;

import java.util.List;

import fp.examenes.Examen;
import fp.examenes.FactoriaExamenes;

public class TestFactoriaExamenes {
	
	public static void testFactoriaExamenes() {
		
			List<Examen> examenes = FactoriaExamenes.leeExamenes("./data/CSV de la sesión 2");
		
			System.out.println("Se han leído " + examenes.size() + " exámenes.");
			for (Examen examen : examenes) {
				System.out.println(examen);
			}
			
	}
	
	public static void main(String[] args) {
		try {
			testFactoriaExamenes();
		} catch(Exception e) {
			System.out.println("Excepción capturada: ");
			System.out.println(e.getMessage());
		}
	}

}
