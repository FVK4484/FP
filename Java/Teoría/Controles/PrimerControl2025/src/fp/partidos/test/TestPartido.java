package fp.partidos.test;

import java.time.LocalDate;
import java.util.ArrayList;
import java.util.List;

import fp.partidos.Competicion;
import fp.partidos.Partido;
import fp.partidos.Resultado;

public abstract class TestPartido {

	public static void main(String[] args) {
		Resultado r1 = Resultado.parse("22-0-1");
		Resultado r2 = Resultado.parse("42-1-1");
		Resultado r3 = Resultado.parse("17-2-1");
		Resultado r4 = Resultado.parse("0-0-0");
		List<Resultado> l1 = new ArrayList<>();
		List<Resultado> l2 = new ArrayList<>();
		l1.add(r1);
		l1.add(r2);
		l1.add(r3);
		l2.add(r4);
		
		try {
		Partido p1 = new Partido(LocalDate.of(2023, 4, 29), "Celta de Vigo", "Villareal", 14467L, Competicion.LIGA, l1);
		System.out.println(p1);
		
		Partido p2 = new Partido(LocalDate.of(2023, 3, 21), "Mallorca", "Espanyol", 13780L, Competicion.LIGA, l2);
		System.out.println(p2);
		} catch (Exception e){
			System.out.println("Excepción capturada: ");
			System.out.println(e.getMessage());
		}
		Partido p3 = new Partido(LocalDate.of(2023, 4, 29), "Celta de Vigo", "Villareal", 14467L, Competicion.LIGA, l2);
		System.out.println(p3);
	}

}
