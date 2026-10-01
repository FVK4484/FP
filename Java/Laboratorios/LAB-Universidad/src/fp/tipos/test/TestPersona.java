package fp.tipos.test;

import java.time.LocalDate;

import fp.tipos.Persona;

public class TestPersona {

	public static void main(String[] args) {
		try {
		LocalDate fecha = LocalDate.of(1998, 9, 15);
		Persona p1 = new Persona("28864888E", "Pascual", "García Vaquero", 
				fecha, "pascual@gmail.com");
		System.out.println(p1);
		System.out.println(p1.getEdad());
		
		Persona p2 = new Persona("28864678W", "Pascual", "García Vaquero", 
				fecha);
		System.out.println(p2);
		System.out.println(p2.getEdad());
		} catch (Exception e) {
			System.out.println("Excepcion capturada: ");
			System.out.println(e.getMessage());
		}

	}

}
