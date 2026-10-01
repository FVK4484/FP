package fp.curso.test;

import java.time.LocalDate;
import java.time.format.DateTimeFormatter;

import fp.curso.CursoOnline;
import fp.curso.NivelDificultad;
import fp.curso.TipoCertificacion;

public class TestCursoOnline {

	public static void main(String[] args) {
		CursoOnline c1 = 
				new CursoOnline("CUO12345",
						"Aprender a programar en Python",
						"Coursera",
						LocalDate.of(2023, 2, 14),
						LocalDate.of(2023, 5, 14),
						60, TipoCertificacion.CURSO,
						6.5, NivelDificultad.AVANZADO,
						1200, false);
		
		System.out.println(c1);
		
		CursoOnline c2 = 
				new CursoOnline("CUO12345",
						"Aprender a programar en Python",
						"Coursera",
						LocalDate.of(2023, 1, 14),
						LocalDate.parse("14/08/2023",
								DateTimeFormatter.ofPattern("dd/MM/yyyy")),
						60, TipoCertificacion.CURSO,
						6.5, NivelDificultad.AVANZADO,
						1200, false);
		
		System.out.println(c2);
		
		try {
			c1.setFechaFin(LocalDate.of(2020, 2, 14));
		} catch(Exception e) {
			System.out.println("Error capturado: " +
					e.getMessage());
		}
		
		System.out.println(c1);
		System.out.println(c1.getMediaHorasSemanales());
		System.out.println(c1.getEstado());
		System.out.println(c2.compareTo(c1));

	}

}
