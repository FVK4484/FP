package fp.figuras.test;

import fp.figuras.TrianguloImpl;
import fp.figuras.Cuadrado;
import fp.figuras.CuadradoImpl;
import fp.figuras.Triangulo;

public class TestFiguras {

	public static void main(String[] args) {
		
		TrianguloImpl triangulo1 = new TrianguloImpl();
		Triangulo triangulo2 = new TrianguloImpl();
		Cuadrado cuadrado1 = new CuadradoImpl();
		
		triangulo1.hacerVisible();
		triangulo2.hacerVisible();
		cuadrado1.hacerVisible();
		
	}

}
