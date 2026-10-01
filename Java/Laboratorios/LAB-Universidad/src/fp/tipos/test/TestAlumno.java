package fp.tipos.test;

import java.time.LocalDate;

import fp.tipos.Alumno;
import fp.tipos.Asignatura;
import fp.tipos.TipoAsignatura;

public class TestAlumno {

	public static void main(String[] args) {
		
		Alumno a =new Alumno("28864657W", "Juan", "Sin Miedo", 
				LocalDate.of(2007, 6, 3), "juan.sin.miedo@alum.us.es");
		Asignatura asi = new Asignatura("Fundamento De Programacion", "0000230", 12.0, TipoAsignatura.ANUAL, 1);
		a.matriculaAsignatura(asi);
		
		System.out.println(a);
		System.out.println(asi);

	}

}
