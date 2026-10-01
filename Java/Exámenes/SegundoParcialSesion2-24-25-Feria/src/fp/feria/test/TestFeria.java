package fp.feria.test;

import java.util.Set;
import fp.feria.CasetaFeria;
import fp.feria.FactoriaFeria;
import fp.feria.FeriaGestion;
import fp.feria.TipoCaseta;

public class TestFeria {

	public static void main(String[] args) {
		Set<CasetaFeria> casetas = FactoriaFeria.leeCasetas("./data/CSV de la sesión 2.csv");
		
//		for(CasetaFeria caseta : casetas) {
//			System.out.println(caseta);
//		}
		
		FeriaGestion fg = new FeriaGestion(casetas);
		
		System.out.println(" FACTORÍA = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = ");
		System.out.println(" Nº de casetas en la feria " + casetas.size());
		
		System.out.println(" EJ1 = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =");
		testGetPrecioMaxProducto(fg, TipoCaseta.PUBLICA);
		System.out.println(" EJ2 = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =");
		testgetValoracionMediaTipoCasetaAccesible(fg, TipoCaseta.PRIVADA, true);
		testgetValoracionMediaTipoCasetaAccesible(fg, TipoCaseta.PUBLICA, true);
		testgetValoracionMediaTipoCasetaAccesible(fg, TipoCaseta.PRIVADA, false);
		testgetValoracionMediaTipoCasetaAccesible(fg, TipoCaseta.PUBLICA, false);
		System.out.println(" EJ3 = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =");
		testGetNombresProductos(fg, 5.00);
		testGetNombresProductos(fg, 10.00);
		
		
	}
	
	public static void testGetPrecioMaxProducto(FeriaGestion fg, TipoCaseta tipoCaseta) {
		System.out.println(" El precio máximo encontrado para cada producto en las casetas de tipo PUBLICA es: " + fg.getPrecioMaxProducto(tipoCaseta));
	}
	
	public static void testgetValoracionMediaTipoCasetaAccesible(FeriaGestion fg, TipoCaseta tipoCaseta, Boolean accesibilidad) {
		System.out.println(" La valoración media para las casetas con accesibilidad = " + accesibilidad + " y de tipo " + tipoCaseta + " es: " + fg.getValoracionMediaTipoCasetaAccesible(tipoCaseta, accesibilidad));
	}
	
	public static void testGetNombresProductos(FeriaGestion fg, Double umbral) {
		System.out.println(" Los nombres de los productos cuyo precio no superan en alguna caseta los " + umbral + " euros son:");
		System.out.println(fg.getNombresProductos(umbral));
	}

}
