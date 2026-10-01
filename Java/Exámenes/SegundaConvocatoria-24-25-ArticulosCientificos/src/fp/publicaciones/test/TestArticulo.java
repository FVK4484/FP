package fp.publicaciones.test;

import fp.publicaciones.FactoriaArticulos;
import java.util.List;
import fp.publicaciones.Articulo;


public class TestArticulo {

	public static void main(String[] args) {
		List<Articulo> articulos = FactoriaArticulos.leeArticulos("./data/articulos.csv");
		System.out.println("Se han leido " + articulos.size() + " articulos");
		for (Articulo a : articulos) {
			System.out.println(a);
		}
		
	}

}
