package fp.tipos.test;

import fp.tipos.Asignatura;
import fp.tipos.Nota;
import fp.tipos.TipoAsignatura;
import fp.tipos.TipoConvocatoria;

public class TestNota {

	public static void main(String[] args) {
		Asignatura asignatura = new Asignatura("Fundamentos de Programación", "0000230",
				12.0, TipoAsignatura.ANUAL, 1);
		System.out.println(asignatura);
		Nota nota = new Nota(asignatura, 2025, TipoConvocatoria.PRIMERA, 9.5, true);
		System.out.println(nota);
	}

}
