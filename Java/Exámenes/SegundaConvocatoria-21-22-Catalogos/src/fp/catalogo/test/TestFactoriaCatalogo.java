package fp.catalogo.test;

import java.util.Map;

import fp.catalogo.Catalogo;
import fp.catalogo.FactoriaCatalogo;
import fp.catalogo.TipoComponente;

public class TestFactoriaCatalogo {

	public static void main(String[] args) {
		
		Catalogo catalogo = FactoriaCatalogo.leerCatalogo("./data/catalogo.csv");
//		System.out.println(catalogo);
		
		testNumeroComponentesPorTipoDeSuministrador(catalogo, "suministrador1");
		testComponentesConCombinadoresConPrecioMaximo(catalogo, 12.);

	}
	
	private static void testNumeroComponentesPorTipoDeSuministrador(Catalogo catalogo, String suministrador) {
		System.out.println(" ---Ejercicio1-------");
		for (Map.Entry<TipoComponente, Long> par : catalogo.numeroComponentesPorTipoDeSuministrador(suministrador).entrySet()) {
			System.out.println("   " + par.getKey() + "=" + par.getValue());
		}
	}
	
	private static void testComponentesConCombinadoresConPrecioMaximo(Catalogo catalogo, Double precio) {
		System.out.println(" ---Ejercicio2-------");
		for (String componente : catalogo.componentesConCombinadoresConPrecioMaximo(precio)) {
			System.out.println("   " + componente);
		}
	}

}