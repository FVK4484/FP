package fp.tipos.test;

import java.time.DayOfWeek;
import java.time.LocalTime;

import fp.tipos.Tutoria;

public class TestTutoria {

	public static void main(String[] args) {
		LocalTime horaComienzo = LocalTime.of(10, 30);
		LocalTime horaFin = LocalTime.of(12, 30);
		Tutoria tutoria1 = new Tutoria(DayOfWeek.WEDNESDAY, horaComienzo, horaFin);
		Tutoria tutoria2 = new Tutoria(DayOfWeek.FRIDAY, horaComienzo, 240);
		System.out.println(tutoria1);
		System.out.println(tutoria1.getDuracion());
		System.out.println(tutoria2);
		System.out.println(tutoria2.getDuracion());
	}

}
