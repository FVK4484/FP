package fp.tipos.test;

import fp.tipos.Asignatura;
import fp.tipos.TipoAsignatura;

public class TestAsignatura {

	public static void main(String[] args) {
		Asignatura asignatura = new Asignatura("Fundamentos de Programación", "0000230",
				12.0, TipoAsignatura.ANUAL, 1);
		System.out.println(asignatura);
		System.out.println(asignatura.getAcronimo());
	}

}
