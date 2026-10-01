package fp.examenes.test;

import java.time.Duration;
import java.time.LocalDateTime;
import java.util.ArrayList;
import java.util.List;

import fp.examenes.Aula;
import fp.examenes.Examen;
import fp.examenes.TipoExamen;

public class TestExamen {
	public static void testExamen() {
		List<Aula> aulas = new ArrayList<>();
		Aula aula1 = new Aula("I2.35", 22);
		Aula aula2 = new Aula("A1.10", 50);
		aulas.add(aula1);
		aulas.add(aula2);
		Examen examen = new Examen("HUM", 4, LocalDateTime.of(2024, 6, 15, 19, 0), 
				Duration.ofHours(179), 
				TipoExamen.PRACTICO, 74, 
				false, aulas);
		System.out.println(examen);
		System.out.println(examen.getPuestos());
		System.out.println(examen.getCapacidadMaxima());
		System.out.println(examen.getPorcentajeAsistentes());
		System.out.println(examen.usaAula("I2.35"));
	}
	public static void main(String[] args) {
		try {
		testExamen();
		} catch (Exception e) {
			System.out.println("Excepción capturada: ");
			System.out.println(e.getMessage());
		}

	}

}
